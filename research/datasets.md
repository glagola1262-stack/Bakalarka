
# Analýza datasetov

Tento dokument obsahuje prehľad datasetov identifikovaných počas rešerše pre bakalársku prácu. Zameriava sa na ich pôvod, obsah, spôsob anotácie a možné využitie pri detekcii hate speech a AI-generovaného urážlivého obsahu.

## 1. Andrusyak et al. (2018)

**Názov:** Detection of Abusive Speech for Mixed Sociolects of Russian and Ukrainian Languages

**Rok:** 2018

**Jazyk:** Ruština a ukrajinčina.

**Zdroj:** 
https://nlp.fi.muni.cz/raslan/2018/paper04-Andrusyak.pdf

### Charakteristika

Autori sa zaoberajú detekciou abusive speech v ruskom a ukrajinskom jazyku. Používajú nesupervidovaný pravdepodobnostný prístup založený na počiatočnom slovníku urážlivých výrazov.

Dataset bol vytvorený z komentárov pod 329 videami na YouTube. Po predspracovaní obsahoval viac ako 50 000 komentárov. Z nich bolo 2 000 manuálne označených; 32,7 % označených komentárov obsahovalo abusive language.

### Význam pre bakalársku prácu

Dataset a metodika poskytujú historický kontext detekcie urážlivého obsahu v slovanských jazykoch. Článok opisuje aj problémy s maskovaním urážlivých výrazov pomocou symbolov, eufemizmov a zmien v zápise slov.

### Stav analýzy

- [x] Odborný článok preštudovaný.
- [x] Základná metodika analyzovaná.
- [ ] Dostupnosť pôvodných dát overená.
- [ ] Dataset prakticky otestovaný.

---

## 2. HateBenchSet (2025)

**Názov:** HateBench: Benchmarking Hate Speech Detectors on LLM-Generated Content and Hate Campaigns

**Autori:** Xinyue Shen et al.

**Rok:** 2025

**Jazyk:** Angličtina.

**Dataset:** 
https://huggingface.co/datasets/TrustAIRLab/HateBenchSet

**Odborný článok:** 
https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-893-shen.pdf

### Charakteristika

HateBench je benchmark zameraný na hodnotenie detektorov hate speech pri obsahu generovanom veľkými jazykovými modelmi (LLM).

Dataset obsahuje:
- 7 838 textových vzoriek.
- Obsah vytvorený šiestimi jazykovými modelmi.
- 34 skupín identity.
- Manuálnu anotáciu tromi anotátormi.
- Označenia Hate a Non-Hate.

Medzi dôležité atribúty patria `model`, `status`, `prompt`, `text` a `hate_label`. Atribút `status` rozlišuje pôvodné a jailbreak vzorky.

### Význam pre bakalársku prácu

Dataset je relevantný pre výskum detekcie AI-generovaného hate speech a analýzu príkladov vytvorených v kontexte jailbreak pokusov.

### Stav analýzy

- [x] Odborný článok preštudovaný.
- [x] Dataset identifikovaný.
- [ ] Štruktúra dát prakticky preskúmaná.
- [ ] Rozdelenie tried overené v stiahnutej verzii.
- [ ] Dataset prakticky otestovaný.

---

## 3. Predbežné porovnanie

| Kritérium | Andrusyak (2018) | HateBench (2025) |
|---|---|---|
| Jazyk | Ruština, ukrajinčina | Angličtina |
| Typ obsahu | YouTube komentáre | LLM-generované texty |
| Prístup | Nesupervidovaný | Benchmark a anotované dáta |
| Hlavné zameranie | Abusive speech | Hate speech a LLM obsah |
| Rok | 2018 | 2025 |

## 4. Ďalšie plánované kroky

1. Preskúmať dostupnosť a licencie datasetov.
2. Stiahnuť a preskúmať HateBenchSet.
3. Analyzovať jednotlivé atribúty a rozdelenie tried.
4. Posúdiť vhodnosť datasetu na tréning a testovanie modelu.
5. Vyhľadať ďalšie aktuálne datasety zamerané na adversariálne príklady.
