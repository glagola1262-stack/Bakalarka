
import os
import json
import random
import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt

from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

SEED = 42
SAMPLE_SIZE = 200
BATCH_SIZE = 8
MAX_LENGTH = 256

DATASET_ID = "TrustAIRLab/HateBenchSet"
MODEL_ID = "facebook/roberta-hate-speech-dynabench-r4-target"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

device = torch.device("cpu")

print("=" * 60)
print("EXPERIMENT 01 - BASELINE TEST")
print("=" * 60)

print("Device:", device)
print("PyTorch:", torch.__version__)

print("\n[1] Loading HateBenchSet...")

dataset = load_dataset(DATASET_ID, "default")

print("Available splits:", list(dataset.keys()))

split_name = "train" if "train" in dataset else list(dataset.keys())[0]

df = dataset[split_name].to_pandas()

print("Dataset split:", split_name)
print("Total records:", len(df))
print("Columns:", list(df.columns))

required_columns = ["text", "hate_label"]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Missing dataset column: {column}")

df = df.dropna(subset=required_columns).copy()

df["hate_label"] = pd.to_numeric(
    df["hate_label"], errors="coerce"
)

df = df.dropna(subset=["hate_label"]).copy()
df["hate_label"] = df["hate_label"].astype(int)

df = df[df["hate_label"].isin([0, 1])].copy()

print("\n[2] Dataset analysis")

print("\nClass distribution:")
print(df["hate_label"].value_counts().sort_index())

if "status" in df.columns:
    print("\nOriginal / Jailbreak distribution:")
    print(pd.crosstab(df["status"], df["hate_label"]))

df["hate_label"].value_counts().sort_index().plot(
    kind="bar"
)

plt.title("HateBenchSet - Class Distribution")
plt.xlabel("Class (0 = Non-Hate, 1 = Hate)")
plt.ylabel("Number of samples")
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURES_DIR, "class_distribution.png"),
    dpi=200
)

plt.close()

print("\n[3] Selecting sample")

sample_size = min(SAMPLE_SIZE, len(df))

sample = df.sample(
    n=sample_size,
    random_state=SEED
).reset_index(drop=True)

texts = sample["text"].astype(str).tolist()
y_true = sample["hate_label"].tolist()

print("Selected samples:", len(sample))
print("Actual class distribution:")
print(sample["hate_label"].value_counts().to_dict())

print("\n[4] Loading RoBERTa model...")
print("The first download may take several minutes.")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_ID
)

model.to(device)
model.eval()

id2label = {
    int(k): str(v).lower()
    for k, v in model.config.id2label.items()
}

print("Model labels:", id2label)

hate_id = next(
    (k for k, v in id2label.items()
     if "hate" in v and "not" not in v),
    None
)

nonhate_id = next(
    (k for k, v in id2label.items()
     if "nothate" in v or "non-hate" in v),
    None
)

if hate_id is None or nonhate_id is None:
    raise ValueError(
        "Could not identify hate and non-hate model labels."
    )

print("\n[5] Running inference...")

all_predictions = []
all_probabilities = []

for start in range(0, len(texts), BATCH_SIZE):

    batch_texts = texts[start:start + BATCH_SIZE]

    inputs = tokenizer(
        batch_texts,
        padding=True,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt"
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.inference_mode():
        outputs = model(**inputs)

    probabilities = torch.softmax(
        outputs.logits, dim=-1
    )

    predictions = outputs.logits.argmax(dim=-1)

    all_predictions.extend(predictions.cpu().tolist())

    all_probabilities.extend(
        probabilities[:, hate_id].cpu().tolist()
    )

    print(
        f"Processed {min(start + BATCH_SIZE, len(texts))}"
        f" / {len(texts)}"
    )

y_pred = [
    1 if prediction == hate_id else 0
    for prediction in all_predictions
]

print("\n[6] Evaluation")

accuracy = accuracy_score(y_true, y_pred)

precision, recall, f1, _ = (
    precision_recall_fscore_support(
        y_true,
        y_pred,
        average="binary",
        pos_label=1,
        zero_division=0
    )
)

report = classification_report(
    y_true,
    y_pred,
    labels=[0, 1],
    target_names=["Non-Hate", "Hate"],
    output_dict=True,
    zero_division=0
)

cm = confusion_matrix(
    y_true,
    y_pred,
    labels=[0, 1]
)

metrics = {
    "experiment": "Experiment 01 - Baseline",
    "dataset": DATASET_ID,
    "model": MODEL_ID,
    "sample_size": len(sample),
    "random_seed": SEED,
    "accuracy": float(accuracy),
    "precision_hate": float(precision),
    "recall_hate": float(recall),
    "f1_hate": float(f1),
    "classification_report": report,
    "confusion_matrix": cm.tolist(),
    "evaluation_note": (
        "Exploratory random sample, not a definitive "
        "full-dataset benchmark."
    )
}

print("\nRESULTS")
print("-" * 40)
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Non-Hate", "Hate"]
)

disp.plot(cmap="Blues", values_format="d")

plt.title("RoBERTa - Confusion Matrix")
plt.tight_layout()

plt.savefig(
    os.path.join(FIGURES_DIR, "confusion_matrix.png"),
    dpi=200
)

plt.close()

results_df = sample.copy()

results_df["predicted_label"] = y_pred
results_df["predicted_class"] = [
    "Hate" if p == 1 else "Non-Hate"
    for p in y_pred
]

results_df["hate_probability"] = all_probabilities

results_df["correct"] = (
    results_df["hate_label"]
    == results_df["predicted_label"]
)

results_df.to_csv(
    os.path.join(RESULTS_DIR, "predictions.csv"),
    index=False,
    encoding="utf-8-sig"
)

with open(
    os.path.join(RESULTS_DIR, "metrics.json"),
    "w",
    encoding="utf-8"
) as file:
    json.dump(metrics, file, indent=4, ensure_ascii=False)

errors = results_df[
    results_df["correct"] == False
]

errors.to_csv(
    os.path.join(RESULTS_DIR, "misclassified.csv"),
    index=False,
    encoding="utf-8-sig"
)

if "status" in results_df.columns:

    status_results = {}

    for status, group in results_df.groupby("status"):

        if group["hate_label"].nunique() < 2:
            continue

        status_results[str(status)] = {
            "sample_size": int(len(group)),
            "accuracy": float(
                accuracy_score(
                    group["hate_label"],
                    group["predicted_label"]
                )
            ),
            "f1_hate": float(
                precision_recall_fscore_support(
                    group["hate_label"],
                    group["predicted_label"],
                    average="binary",
                    pos_label=1,
                    zero_division=0
                )[2]
            )
        }

    metrics["status_analysis"] = status_results

    with open(
        os.path.join(RESULTS_DIR, "metrics.json"),
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(metrics, file, indent=4, ensure_ascii=False)

print("\n" + "=" * 60)
print("EXPERIMENT COMPLETED")
print("=" * 60)

print("Samples:", len(results_df))
print("Correct predictions:", int(results_df["correct"].sum()))
print("Incorrect predictions:", len(errors))

print("\nResults saved in:", RESULTS_DIR)
print("Figures saved in:", FIGURES_DIR)

print("\nGenerated files:")
print("- metrics.json")
print("- predictions.csv")
print("- misclassified.csv")
print("- class_distribution.png")
print("- confusion_matrix.png")
