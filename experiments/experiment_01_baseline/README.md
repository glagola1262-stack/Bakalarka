
# Experiment 01 — Initial RoBERTa Baseline

## 1. Objective

The objective of this experiment is to evaluate an existing pretrained
RoBERTa model on AI-generated hate speech examples.

This experiment establishes a baseline for future fine-tuning.

## 2. Dataset

- Name: HateBenchSet
- Source: TrustAIRLab/HateBenchSet
- Evaluation sample: 200 randomly selected examples
- Random seed: 42

## 3. Model

- Model: facebook/roberta-hate-speech-dynabench-r4-target
- Architecture: RoBERTa
- Evaluation mode: Inference
- Fine-tuning: Not performed

## 4. Results

| Metric | Result |
|---|---:|
| Accuracy | 0.8650 |
| Precision | 0.8817 |
| Recall | 0.8367 |
| F1-score | 0.8586 |

- Total samples: 200
- Correct predictions: 173
- Incorrect predictions: 27

## 5. Generated files

- `results/metrics.json`
- `results/predictions.csv`
- `results/misclassified.csv`
- `figures/class_distribution.png`
- `figures/confusion_matrix.png`

## 6. Initial observations

The pretrained RoBERTa model achieved an accuracy of 86.5%
on the selected sample.

The 27 incorrectly classified examples will be examined
to identify potential weaknesses in hate speech detection.

Particular attention will be paid to jailbreak examples
and adversarial text modifications.

## 7. Limitations

This is a preliminary evaluation using 200 randomly
selected examples.

The experiment does not involve model fine-tuning
or direct AI-authorship detection.

The results should not be interpreted as a final
performance benchmark.

## 8. Next steps

1. Analyze incorrectly classified examples.
2. Compare original and jailbreak samples.
3. Prepare training data.
4. Fine-tune a selected pretrained model.
5. Compare the fine-tuned model with this baseline.
