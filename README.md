# CAPI
Sujet Capi (Conception agile M1-INFO)
Binôme B3-1 (**Hicham Belghachem** et **Samantha Schneibel**)

## Fichiers de l'app :

- **app.py** : Gère l'interface graphique (saisie du pseudo, boutons pour créer ou rejoindre un salon, affichage de la liste des joueurs connectés).
- **fonctionnement_app.py** : Contient les fonctions de création de salon avec code aléatoire et d'ajout de joueur sans doublon.
- **tests_unitaires.py** : Contient l'ensemble des tests unitaires avec pytest qui contrôle que nos critères d'acceptation sont bien respectés au sein de notre code (DoD)
- **requirements.txt** : Contient l'ensemble des dépendances nécessaires au bon fonctionnement du code sur machine

## Utilisation en local sur machine

Après avoir cloné le dépôt (git clone...) :

- Il vous faudra en toute logique python ;) sur un IDE ou autre

- Vous devez installer les différentes dépendances :
  **pip install -r chemin_du_fichier/requirements.txt**

- Pour utiliser l'app en local il vous suffit de faire :
  **python -m streamlit run chemin_du_fichier/app.py**

- Pour lancer les tests unitaires :
  **python -m pytest chemin_du_fichier/tests_unitaires.py**






