---
name: tagset
description: Étiquettes POS des langues GRC, HYE, KAT, SYC. À charger pour construire un prompt ou valider des étiquettes.
---

Fichier : `.vibe/skills/tagset/references/<LANGUE>_tagset.txt`
Format : une étiquette par ligne, le nom, une tabulation, puis la définition.

- Lire le nom avec `.strip()`, car certains se terminent par une espace (`"A "`).
- Une étiquette composée (`I+Prep@N+Com`) est valide si chacune de ses parties l'est.

- `INTJ` (SYC), `PRO+Pos3` (HYE) et `∅` figurent dans le gold mais pas dans le tagset : ne pas le compter comme une erreur.