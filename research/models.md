
# Analýza jazykových modelov

Tento dokument obsahuje prehľad jazykových modelov identifikovaných počas rešerše. Zameriava sa na ich architektúru, účel, spôsob trénovania a možné využitie pri detekcii hate speech.

## 1. RoBERTa – Dynabench R4 Target

**Názov modelu:** facebook/roberta-hate-speech-dynabench-r4-target

**Architektúra:** RoBERTa

**Jazyk:** Angličtina

**Typ úlohy:** Text classification

**Zdroj:**
https://huggingface.co/facebook/roberta-hate-speech-dynabench-r4-target

### Charakteristika

Model je fine-tuned verzia architektúry RoBERTa určená na klasifikáciu hate speech. Súvisí s výskumom Dynabench a prácou Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection (Vidgen et al., 2021).

Model bol trénovaný v rámci štvrtého kola (R4) dynamického zberu dát.

### Dynabench – princíp

Dynabench využíva prístup human-and-model-in-the-loop. Ľudia vytvárajú náročné textové príklady, ktorými sa snažia odhaliť slabiny aktuálneho modelu. Následne sa model opätovne trénuje na nových príkladoch.

Zjednodušený postup:

1. Model klasifikuje texty.
2. Ľudia vytvárajú náročné príklady.
3. Identifikujú sa chyby modelu.
4. Nové príklady sa pridajú do tréningových dát.
5. Model sa opätovne trénuje.

### Význam pre bakalársku prácu

Model predstavuje možný referenčný model (baseline) na úvodné testovanie detekcie hate speech. Prístup Dynabench je relevantný pre skúmanie odolnosti modelov voči adversariálnym príkladom.

### Obmedzenia

- Model je určený pre anglický jazyk.
- Jeho vhodnosť pre slovenčinu alebo ukrajinčinu zatiaľ nebola overená.
- Model zatiaľ nebol prakticky otestovaný v rámci projektu.

### Stav analýzy

- [x] Model identifikovaný.
- [x] Model card preskúmaný.
- [x] Súvisiaca výskumná práca identifikovaná.
- [ ] Model spustený a otestovaný.
- [ ] Výsledky klasifikácie zaznamenané.

## 2. Súvisiaca odborná práca

**Názov:** Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection

**Autori:** Vidgen et al.

**Rok:** 2021

**Zdroj:**
https://aclanthology.org/2021.acl-long.132/

Práca predstavuje dynamický spôsob zhromažďovania náročných príkladov na zlepšenie robustnosti modelov pri detekcii hate speech.

## 3. Plán ďalších krokov

1. Spustiť model pomocou knižnice Transformers.
2. Otestovať model na kontrolovaných textových príkladoch.
3. Zaznamenať predikcie a pravdepodobnosti jednotlivých tried.
4. Preskúmať chyby pri adversariálnych a upravených textoch.
5. Posúdiť vhodnosť modelu ako baseline pre ďalšie experimenty.
