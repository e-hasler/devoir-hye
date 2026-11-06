# Mini-analyste pandas : arménien classique (HYE)

Répondre à des questions sur le corpus arménien (HYE) uniquement en écrivant et en lançant un script pandas.

## Règles

- L'agent principal ne calcule pas directement, il délègue absolument tout à l'agent analyste.

- Uniquement le droit de lancer l'agent analyste, et ce trois fois maximum.
- Ne lance aucun script.
- L'agent principal a l'interdiction d'accéder à tout fichier ne se situant pas sous .vibe/, scripts/ ou output/

- Interdiction absolue de modifier .vibe/, scripts/ ou output/, il faut déléguer à l'analyste

- En cas d'impossibilité d'effectuer une tâche, le signaler dans ta réponse avec la tâche impossible, la cause de l’échec, la commande exécutée si pertinente, les fichiers concernés.
## Rôles
- L'agent analyste répond à des questions sur le corpus arménien (HYE) uniquement en écrivant scripts/analyser.py et en le lançant.
- Les résultats de scripts/analyser.py doit apparaître dans output/result_1.py
## Repères
- Données : `data/HYE_train.tsv`, `data/HYE_test_in-domain.tsv`, `data/HYE_test_out-of-domain.tsv`, colonnes `text_form form lemma pos`.
- Tagset : `.vibe/skills/tagset/references/<LANGUE>_tagset.txt` (étiquette, tabulation, définition).
- Questions :
1. Quelles sont les 5 catégories (`pos`) les plus fréquentes dans le train ?
2. Quelle proportion des mots du train sont des formes composées (`@` dans `pos`) ? Quelles sont les 5 combinaisons les plus fréquentes ?
3. Combien de mots du train se terminent par l'article suffixé (`pos` qui finit par `@PRO+Dem`) ? Combien commencent par la préposition `զ` (`lemma` qui commence par `զ@`) ?
4. Quelles étiquettes du train **ne figurent pas** dans `HYE_tagset.txt`, et combien de fois chacune apparaît-elle ? Attention à deux pièges :
   - certains noms d'étiquettes du tagset se terminent par une espace ;
   - une étiquette composée est valide si chacune de ses parties l'est.
5. Refaites le **dictionnaire** de la partie 12 du notebook, avec le train arménien. Quel score obtient-il sur le test `in-domain`, puis sur le test `out-of-domain` ? Le score baisse-t-il autant qu'en grec (0,73 contre 0,51) ?
- Le bon format de sortie signifie que la réponse de chaque question est écrite sous un titre `Q1` à `Q5` avant chaque réponse
- Droit à 3 essais tout au plus. En cas d'échec, décris les difficultés rencontrées de manière concise dans output/result_1.txt