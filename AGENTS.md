# Mini-analyste pandas : arménien classique (HYE)

Répondre à des questions sur le corpus arménien (HYE) uniquement en écrivant et en lançant un script pandas.

## Règles

- L'agent principal ne calcule pas directement, il délègue absolument tout à l'agent analyste.

- Uniquement le droit de lancer l'agent analyste.
- Ne lance aucun script.
- L'agent principal a l'interdiction d'accéder à tout fichier ne se situant pas sous .vibe/

- Interdiction absolue de modifier .vibe/

- En cas d'impossibilité d'effectuer une tâche, le signaler dans ta réponse avec la tâche impossible, la cause de l’échec,
la commande exécutée si pertinente, 
les fichiers concernés.
## Rôles
- L'agent analyste répond à des questions sur le corpus arménien (HYE) uniquement en écrivant et en lançant un script python.
## Repères
- Données : `data/HYE_train.tsv`, `data/HYE_test_in-domain.tsv`, `data/HYE_test_out-of-domain.tsv`, colonnes `text_form form lemma pos`.
- Tagset : `.vibe/skills/tagset/references/<LANGUE>_tagset.txt` (étiquette, tabulation, définition).