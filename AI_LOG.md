# AI_LOG.md : journal d'usage de l'IA

> À placer à la racine du dépôt. À remplir **au fil de l'eau**, pas en fin de projet. Une entrée par tâche (pas par message), en 5 lignes.
> Rappel : l'IA est autorisée pour le **code de production** et la **configuration d'outils** uniquement. Qui a fait la demande, les fichiers touchés et les commits se retrouvent dans l'historique Git : ne les recopiez pas.

## Outils utilisés (à remplir une fois)

| Outil | Modèle (si connu) | Mode (autocomplétion, chat, agent) |
|---|---|---|
| Gemini | Argon | chat |

Fichier d'instructions pour agent versionné (`CLAUDE.md`, `AGENTS.md`...) : <oui : chemin / non>

## Entrées

### AAAA-MM-JJ : <tâche en une ligne> (US-xx)

- **Demande (résumé fidèle)** : <ce que vous avez demandé, avec le contexte fourni : fichiers, tests...>
- **Résultat** : <accepté tel quel / modifié / rejeté>
- **Ce que nous avons vérifié** : <tests lancés, lecture ligne à ligne, essai manuel...>
- **Ce que nous avons changé ou rejeté, et pourquoi** :

### 2026-11-08 : <Savoir s'il est possible de créer un planning poker via streamlit et de publier l'app (gratuitement) de sorte qu'on puisse jouer en ligne> (US-011)

- **Demande (résumé fidèle)** : <Savoir s'il est possible de créer un planning poker via streamlit et de publier l'app (gratuitement) de sorte qu'on puisse jouer en ligne>
- **Résultat** : <possible de developper la solution sur streamlit avec l'exigence de la gestion de plusieurs utilisateurs simultané>
- **Ce que nous avons vérifié** : <nous avons tester en créant un salon test pour nous en assurer>
- **Ce que nous avons changé ou rejeté, et pourquoi** :

### 2026-11-08 : <Ecriture fonction de création de salon de planning poker> (US-011)

- **Demande (résumé fidèle)** : <Ecrire une creer_salon(salons, pseudo)` prenant un dictionnaire et un pseudo en paramètres, qui génère un code à 4 chiffres entre 1000 et 9999, stocke {"createur": pseudo, "joueurs": [pseudo]}> 
- **Résultat** : <accepté tel quel>
- **Ce que nous avons vérifié** : <Lecture du code généré et test>
- **Ce que nous avons changé ou rejeté, et pourquoi** :

### 2026-11-08 : <Ecriture fonction d'ajout d'un joueur dans un salon existant> (US-011)

- **Demande (résumé fidèle)** : <Ecrire la fonction rejoindre_salon(salons, code, pseudo) qui vérifie si "code" existe dans le dictionnaire "salons", ajoute "pseudo" une liste salons[code]["joueurs"] uniquement s'il n'est pas déjà présent>
- **Résultat** : <accepté tel quel>
- **Ce que nous avons vérifié** : <Lecture du code généré et test>
- **Ce que nous avons changé ou rejeté, et pourquoi** :

### 2026-11-08 : <Mise en place du système de gestion simultané sur le futur serveur streamlit> (US-011)

- **Demande (résumé fidèle)** : <Après avoir demander comment pouvoir gérer la gestion de plusieurs joueurs en simultané, nous avons un exemple de code puis nous avons adapter avec l'IA le squelette de code à notre besoin>
- **Résultat** : <modifié>
- **Ce que nous avons vérifié** : <Lecture du code généré et test>
- **Ce que nous avons changé ou rejeté, et pourquoi** :

### 2026-11-08 : <Ecran d'accueil Streamlit avec formulaires de création et connexion> (US-011)

- **Demande (résumé fidèle)** : <Utilisation des fonction de "fonctionnement_app.py" avec la demande du pseudo, création de salon (nous avons adapté le code manuellement et en rapportant différentes erreurs...)>
- **Résultat** : <modifié>
- **Ce que nous avons vérifié** : <Lecture du code généré et test>
- **Ce que nous avons changé ou rejeté, et pourquoi** :

### 2026-11-08 : <Ecran du salon de jeu et liste des joueurs connectés> (US-011)

- **Demande (résumé fidèle)** : <Après la création de session, après avoir demander comment rafraichir la page avec les joueurs s'ajoutant à la session, puis nous avons demander à avoir le code de session, un bouton actualiser et pouvoir quitter la session>
- **Résultat** : <accepté tel quel>
- **Ce que nous avons vérifié** : <Lecture du code généré et test>
- **Ce que nous avons changé ou rejeté, et pourquoi** :

### 2026-11-08 : <Aide à l'utilisation de bibliothèque des tests unitaires> (US-011)

- **Demande (résumé fidèle)** : <Aide sur l'utilisation de pytest, assert... Sur des exemples, nous avons ensuite coder l'ensemble des tests à partir de la base fourni par l'IA>
- **Résultat** : <modifié>
- **Ce que nous avons vérifié** : <Lecture du code généré et test>
- **Ce que nous avons changé ou rejeté, et pourquoi** :



## Bilan (à compléter en séance 4, 3 lignes)

- Nombre d'entrées et de propositions rejetées ou corrigées :
- Tâches où l'IA a fait gagner du temps :
- Tâches où l'IA a fait perdre du temps :
