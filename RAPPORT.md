## Notes additionnelles

- Je supprime data/HYE_tagset.txt pour n'avoir que tagset/references/HYE_tagset.
- Création du fichier .vibe/config.toml pour gérer les permissions de l'agent orchestrateur
- J'ai modifié tagset/SKILL.md afin de ne pas embrouiller mon agent analyste avec des consignes qui ne le concernent pas.
- Je n'ai pas précisé la règle du nombre de ligne de la reponse car de bonnes réponses pourraient occuper plusieurs lignes.
- Je n'ai pas précisé d'interdits à mon sous-agent car j'ai explicité les autorisations.

## Réponses
- Les 5 réponses, copiées depuis la sortie du script.
- La consigne exacte que vous avez donnée à l'agent.
- **Une erreur de l'agent** : ce qu'il a fait de travers (mauvais filtre, boucle interdite, fonction hors skill, chiffre inventé…) et ce que vous avez changé dans `AGENTS.md`, le `.toml` ou la skill pour la corriger.
- Les fonctions que vous avez ajoutées à la skill `pandas-tuto`, s'il y en a.
- En 3 lignes : qu'est-ce que l'agent apporte ici par rapport au notebook ? Qu'est-ce qu'il coûte ?

## Prompts à l'agent et problèmes rencontrés
> Prompt initial : Repond aux Questions 1 à 5 sur le corpus arménien (HYE).

| Problème (réponse de l'agent) | Solution |
|---|---|
| "Je n'arrive pas à le spawner directement." | Ajouté `delegate = true` dans config.toml |
| "L'agent analyste semble toujours en cours d'exécution sans produire de résultat." | Autorisé les 2 agents à lire `scripts/` et `output/`, ajout de "Le script scripts/analyser.py doit avoir comme chemin de sortie output/result_1.txt." dans analyste.toml |

> 2e prompt : Repond aux Questions 1 à 5 sur le corpus arménien (HYE) si les resultats n'aparaissent pas encore dans output/result_1.txt

Note : L'agent principal a finalement corrigé le chemin TEST_OUT_DOMAIN_PATH, ça a permis le sous-agent d'obtenir les résultats en faisant tourner `scripts/analyser.py` mais l'agent principal n'avait normalement pas la permission.

Note à moi-même : Les résultats ont été obtenus avec le code écrit uniquement par le sous-agent mais j'ai corrigé à la main avant de push sur GitHub le path BASE_DIR pour utiliser `os.path.dirname` afin que le code de l'agent soit utilisable par tout le monde.
## Output

```
Q1
Les 5 catégories (pos) les plus fréquentes dans le train :
  V: 1008
  N+Com: 786
  I+Conj: 745
  I+Prep: 310
  A: 295

Q2
Proportion des mots avec des formes composées (@ dans pos) : 0.142
Les 5 combinaisons les plus fréquentes :
  N+Com@PRO+Dem: 166
  I+Prep@N+Com: 164
  I+Prep@N+Com@PRO+Dem: 76
  A@PRO+Dem: 41
  I+Prep@PRO+Dem: 37

Q3
Nombre de mots avec pos finissant par @PRO+Dem : 383
Nombre de mots avec lemma commençant par զ@ : 339

Q4
Étiquettes du train qui ne figurent pas dans HYE_tagset.txt :
  Aucune étiquette invalide trouvée dans le train.

Q5
Score sur le test in-domain : 0.5667
Score sur le test out-of-domain : 0.5159
La baisse est de 0.05, contre 0.22 en grec. La baisse est moins forte qu'en grec.
```

## Intérêt de l'agent

Accès au détail de la méthode. A part ça je ne sais pas si utiliser un agent m'a facilité la tâche 👀...