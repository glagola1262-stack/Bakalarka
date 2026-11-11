
# Prehľad odbornej literatúry

Tento dokument obsahuje prehľad odborných publikácií súvisiacich s detekciou abusive language, hate speech, AI-generovaným obsahom a odolnosťou jazykových modelov voči adversariálnym príkladom.

## 1. Andrusyak et al. (2018)

**Názov:** Detection of Abusive Speech for Mixed Sociolects of Russian and Ukrainian Languages

**Autori:** Bohdan Andrusyak, Mykhailo Rimel, Roman Kern

**Rok:** 2018

**Publikácia:** RASLAN 2018

**Zdroj:** https://nlp.fi.muni.cz/raslan/2018/paper04-Andrusyak.pdf

### Zameranie práce

Autori sa venujú automatickej detekcii abusive speech v ruskom a ukrajinskom jazyku. Navrhujú nesupervidovaný pravdepodobnostný prístup založený na počiatočnom slovníku urážlivých výrazov.

### Metodika

Metóda postupne rozširuje počiatočný slovník o nové výrazy. Autori využívajú pravdepodobnostné hodnotenie kandidátnych slov a sledujú zmenu výsledkov klasifikácie pomocou metriky F1.

### Hlavné zistenia

Článok poukazuje na problémy spojené so slovotvorbou, zmiešaným používaním jazykov a maskovaním urážlivých výrazov. Experimenty ukazujú, že stemming môže zvýšiť recall, ale zároveň znížiť precision.

### Súvis s bakalárskou prácou

Publikácia poskytuje východiská pre pochopenie detekcie urážlivého obsahu v slovanských jazykoch a problémov spojených s obchádzaním jednoduchších detekčných metód.

---

## 2. Vidgen et al. (2021)

**Názov:** Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection

**Autori:** Bertie Vidgen, Tristan Thrush, Zeerak Waseem, Douwe Kiela

**Rok:** 2021

**Publikácia:** ACL-IJCNLP 2021

**Zdroj:** https://aclanthology.org/2021.acl-long.132/

### Zameranie práce

Práca skúma dynamický spôsob vytvárania datasetov na zlepšenie detekcie hate speech. Autori využívajú prístup human-and-model-in-the-loop.

### Metodika

Ľudskí anotátori vytvárajú náročné textové príklady, ktoré majú odhaliť slabiny aktuálneho modelu. Nové príklady sa následne používajú na opätovné trénovanie modelu. Proces prebieha vo viacerých kolách.

### Hlavné zistenia

Autori ukazujú, že dynamický zber náročných príkladov môže pomôcť zlepšiť robustnosť modelov voči textom, ktoré boli vytvorené s cieľom oklamať detektor.

### Súvis s bakalárskou prácou

Prístup Dynabench je relevantný pre skúmanie taktík obchádzania detekčných algoritmov a pre prípravu náročných testovacích príkladov.

---

## 3. Shen et al. (2025)

**Názov:** HateBench: Benchmarking Hate Speech Detectors on LLM-Generated Content and Hate Campaigns

**Autori:** Xinyue Shen et al.

**Rok:** 2025

**Publikácia:** USENIX Security 2025

**Zdroj:** https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-893-shen.pdf

### Zameranie práce

Autori skúmajú schopnosť existujúcich detektorov rozpoznávať hate speech v obsahu generovanom veľkými jazykovými modelmi.

### Metodika

Práca predstavuje benchmark HateBench, ktorý obsahuje LLM-generované texty a adversariálne scenáre. Hodnotí viacero detektorov a skúma ich správanie pri rôznych typoch obsahu.

### Súvis s bakalárskou prácou

Táto publikácia je priamo relevantná pre tému AI-generovaných urážok a možností obchádzania detekčných systémov. Dataset HateBench predstavuje kandidáta na ďalšiu analýzu a experimentálne využitie.

---

## 4. Predbežné porovnanie prístupov

| Publikácia | Rok | Hlavný prístup | Význam |
|---|---|---|---|
| Andrusyak et al. | 2018 | Slovníkovo-pravdepodobnostná detekcia | Detekcia abusive speech v slovanských jazykoch |
| Vidgen et al. | 2021 | Dynamický adversariálny zber dát | Zlepšovanie robustnosti modelov |
| Shen et al. | 2025 | Benchmark LLM-generovaného obsahu | Hodnotenie detektorov na AI-generovaných textoch |

## 5. Predbežné zhrnutie

Preštudované publikácie predstavujú vývoj rôznych prístupov k detekcii urážlivého a nenávistného obsahu. Staršia práca sa zameriava na slovníkovo-pravdepodobnostnú metódu, zatiaľ čo novšie práce skúmajú dynamické vytváranie náročných príkladov a detekciu obsahu generovaného veľkými jazykovými modelmi.

Tieto poznatky tvoria teoretický základ pre ďalšie skúmanie fine-tuningu jazykových modelov a ich odolnosti voči adversariálnym textom.
