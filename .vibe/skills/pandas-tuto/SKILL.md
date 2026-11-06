---
name: pandas-tuto
description: Fonctions autorisées dans l'élaboration de scripts/analyser.py pour extraire les informations des fichiers data/ 
---

Seules les fonctions pandas ci-dessous sont autorisées. On travaille sur des colonnes
entières : pas de boucle `for` sur les lignes d'un tableau.

| Je veux… | pandas |
|---|---|
| lire un TSV | `pd.read_csv(chemin, sep="\t")` |
| voir le début, la fin | `df.head()`, `df.tail()` |
| connaître la taille, les colonnes | `df.shape`, `df.columns`, `df.info()` |
| un résumé | `df.describe()` |
| une colonne, plusieurs colonnes | `df["col"]`, `df[["col1", "col2"]]` |
| compter les valeurs | `df["col"].value_counts()`, `.nunique()`, `.unique()` |
| filtrer des lignes | `df[df["col"] == valeur]`, `df[(condition1) & (condition2)]` |
| ajouter une colonne | `df["nouvelle"] = ...`, `.str.len()`, `.str.contains("@")` |
| trier | `df.sort_values("col", ascending=False)` |
| calculer par groupe | `df.groupby("col")["autre"].mean()` |
| réunir plusieurs tableaux | `pd.concat(liste_de_tableaux, ignore_index=True)` |
| tableau croisé | `pd.crosstab(df["col1"], df["col2"])` |
| tester l'appartenance | `df["col"].isin(autre_liste)` |
| associer deux tableaux | `df.merge(autre, on="col", how="left")` |
| renommer, dédoublonner | `df.rename(columns={"a": "b"})`, `df.drop_duplicates("col")` |
| enregistrer | `df.to_csv("fichier.csv", index=False)` |