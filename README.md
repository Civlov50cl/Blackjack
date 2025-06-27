Blackjack

Projet Blackjack en ligne de commande écrit en Python
1 joueur contre le croupier, avec règles simplifiées pour la version 1

Règles :

- Le joueur et le croupier reçoivent 2 cartes
- Le joueur peut "tirer" (hit) ou "rester" (stand)
- Si l’un dépasse 21 → il perd
- Le plus proche de 21 gagne

Systeme de mise :

-Solde initial : 1000
-Tu choisis ta mise en debut de partie
-Gain : tu gagne le double de ta mise
-Perte : tu perds ta mise
-Egalite : tu recupères ta mise


Lancer le jeu :

python3 -m venv .venv
source .venv/bin/activate
python blackjack.py
