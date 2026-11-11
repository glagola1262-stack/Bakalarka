
# Bakalárska práca

**Fine-tuning modelov na zachytávanie AI generovaných urážok a taktík na obchádzanie algoritmov pre hate speech**

## Cieľ projektu

Preskúmať možnosti využitia fine-tuningu predtrénovaných jazykových modelov na detekciu AI-generovaných urážok a hate speech vrátane textov využívajúcich taktiky obchádzania detekčných algoritmov.

## Aktuálny stav

- Úvodná rešerš odbornej literatúry.
- Analýza datasetu Andrusyak et al. (2018).
- Analýza datasetu HateBench (2025).
- Identifikácia modelu RoBERTa Dynabench R4.
- Príprava dokumentácie a výskumného postupu.

## Plánované činnosti

- Podrobnejšia analýza dostupných datasetov.
- Testovanie existujúceho klasifikačného modelu.
- Príprava experimentov.
- Fine-tuning a vyhodnotenie modelu.

## Štruktúra repozitára

- `Postup prace.docx` – priebežná dokumentácia.
- `README.md` – informácie o projekte.
- `research/` – analýza literatúry, datasetov a modelov.
- `src/` – zdrojový kód experimentov (neskôr).

## Použité zdroje

1. Andrusyak et al. (2018): [Detection of Abusive Speech](https://nlp.fi.muni.cz/raslan/2018/paper04-Andrusyak.pdf)
2. Shen et al. (2025): [HateBench](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-893-shen.pdf)
3. [HateBench Dataset – Hugging Face](https://huggingface.co/datasets/TrustAIRLab/HateBenchSet)
4. [RoBERTa Dynabench R4 – Hugging Face](https://huggingface.co/facebook/roberta-hate-speech-dynabench-r4-target)
5. Vidgen et al. (2021): [Learning from the Worst](https://aclanthology.org/2021.acl-long.132/)
