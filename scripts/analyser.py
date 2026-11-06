import pandas as pd
import os

# Chemins vers les fichiers
#BASE_DIR = "/Users/eleonore.hasler/Documents/enc_year_1/git_class/devoir-hye"
# utiliser os.path.join pour construire les chemins de manière portable
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # correspond à devoir-hye
TRAIN_PATH = os.path.join(BASE_DIR, "data", "HYE_train.tsv")
TEST_IN_DOMAIN_PATH = os.path.join(BASE_DIR, "data", "HYE_test_in-domain.tsv")
TEST_OUT_DOMAIN_PATH = os.path.join(BASE_DIR, "data", "HYE_test_out-of--domain.tsv")
TAGSET_PATH = os.path.join(BASE_DIR, ".vibe", "skills", "tagset", "references", "HYE_tagset.txt")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "result_1.txt")

# Lire les données
train = pd.read_csv(TRAIN_PATH, sep="\t")
test_in_domain = pd.read_csv(TEST_IN_DOMAIN_PATH, sep="\t")
test_out_domain = pd.read_csv(TEST_OUT_DOMAIN_PATH, sep="\t")

# Lire le tagset
tagset_lines = open(TAGSET_PATH, "r", encoding="utf-8").readlines()
tagset = [line.split("\t")[0].strip() for line in tagset_lines]

# ----- Q1: 5 catégories (pos) les plus fréquentes dans le train -----
q1_result = train["pos"].value_counts().head(5)

# ----- Q2: Proportion des mots du train avec des formes composées (@ dans pos) -----
# Filtrer les lignes où pos contient @
composees = train[train["pos"].str.contains("@")]
proportion_composees = len(composees) / len(train)

# 5 combinaisons les plus fréquentes
composees_counts = composees["pos"].value_counts().head(5)

# ----- Q3: Mots du train avec pos finissant par @PRO+Dem et lemma commençant par զ@ -----
# Mots avec pos finissant par @PRO+Dem
view_pro_dem = train[train["pos"].str.endswith("@PRO+Dem")]
count_pro_dem = len(view_pro_dem)

# Mots avec lemma commençant parզ@
lemma_z = train[train["lemma"].str.startswith("զ@")]
count_lemma_z = len(lemma_z)

# ----- Q4: Étiquettes du train qui ne figurent pas dans HYE_tagset.txt -----
# Fonction pour vérifier si une étiquette est valide
def est_valide(etiquette, tagset):
    # Si l'étiquette est dans le tagset, elle est valide
    if etiquette in tagset:
        return True
    # Si l'étiquette est composée, vérifier chaque partie
    if "@" in etiquette:
        parties = etiquette.split("@")
        return all(partie in tagset for partie in parties)
    return False

# Exceptions mentionnées dans le skill tagset
# INTJ (SYC), PRO+Pos3 (HYE) et ∅ figurent dans le gold mais pas dans le tagset : ne pas les compter comme une erreur.

# Récupérer toutes les étiquettes uniques dans le train
etiquettes_train = train["pos"].unique()

# Filtrer les étiquettes qui ne sont pas valides
# et qui ne sont pas dans la liste des exceptions
exceptions = ["PRO+Pos3", "∅"]
etiquettes_invalides = []
for etiquette in etiquettes_train:
    if etiquette in exceptions:
        continue  # Ignorer les exceptions
    if not est_valide(etiquette, tagset):
        etiquettes_invalides.append(etiquette)

# Compter les occurrences de chaque étiquette invalide
invalides_counts = train[train["pos"].isin(etiquettes_invalides)]["pos"].value_counts()

# ----- Q5: Dictionnaire de la partie 12 du notebook -----
# Créer le dictionnaire à partir du train
# Une ligne par forme (drop_duplicates garde la première rencontrée)
dico = train[["form", "pos"]].drop_duplicates("form")
dico = dico.rename(columns={"pos": "pos_dico"})

# Associer le dictionnaire au test in-domain
resultat_in = test_in_domain.merge(dico, on="form", how="left")
# Calculer le score : proportion de lignes où pos == pos_dico
score_in_domain = (resultat_in["pos"] == resultat_in["pos_dico"]).mean()

# Associer le dictionnaire au test out-of-domain
resultat_out = test_out_domain.merge(dico, on="form", how="left")
# Calculer le score : proportion de lignes où pos == pos_dico
score_out_domain = (resultat_out["pos"] == resultat_out["pos_dico"]).mean()

# Vérifier si la baisse est aussi forte qu'en grec (0.73 contre 0.51)
# La baisse en grec est de 0.73 - 0.51 = 0.22
baisse_hye = round(score_in_domain - score_out_domain, 2)
baisse_grc = 0.22

# ----- Écrire les résultats dans output/result_1.txt -----
# Créer le dossier output s'il n'existe pas
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Formater les résultats
resultats = []

# Q1
resultats.append("Q1")
resultats.append("Les 5 catégories (pos) les plus fréquentes dans le train :")
for pos, count in q1_result.items():
    resultats.append(f"  {pos}: {count}")

# Q2
resultats.append("\nQ2")
resultats.append(f"Proportion des mots avec des formes composées (@ dans pos) : {round(proportion_composees, 4)}")
resultats.append("Les 5 combinaisons les plus fréquentes :")
for pos, count in composees_counts.items():
    resultats.append(f"  {pos}: {count}")

# Q3
resultats.append("\nQ3")
resultats.append(f"Nombre de mots avec pos finissant par @PRO+Dem : {count_pro_dem}")
resultats.append(f"Nombre de mots avec lemma commençant par զ@ : {count_lemma_z}")

# Q4
resultats.append("\nQ4")
resultats.append("Étiquettes du train qui ne figurent pas dans HYE_tagset.txt :")
if len(invalides_counts) == 0:
    resultats.append("  Aucune étiquette invalide trouvée dans le train.")
else:
    for etiquette, count in invalides_counts.items():
        resultats.append(f"  {etiquette}: {count}")

# Q5
resultats.append("\nQ5")
resultats.append(f"Score sur le test in-domain : {round(score_in_domain, 4)}")
resultats.append(f"Score sur le test out-of-domain : {round(score_out_domain, 4)}")
resultats.append(f"La baisse est de {baisse_hye}, contre 0.22 en grec. La baisse est {'aussi forte' if baisse_hye >= 0.20 else 'moins forte'} qu'en grec.")

# Écrire dans le fichier
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(resultats))

print("Script exécuté avec succès. Résultats enregistrés dans :", OUTPUT_PATH)
