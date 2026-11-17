Labo 5 - Distribution de charge avec nginx

6GEI311 Architecture des logiciels

ALIMI Rayane (ALIR21030509)
ADISSO Allglory (ADIA23010300)

Résumé

On a fait une petite application Flask qui affiche un message avec nos initiales et
l'adresse IP de la machine. On l'a lancée sur nos deux ordinateurs et on a installé nginx
pour envoyer les requêtes sur les deux. On a fait la manip deux fois pour que chacun soit
le membre A une fois (app_RA.py pour Rayane, app_AA.py pour Allglory).

Adresse de Rayane : 192.168.76.168
Adresse d'Allglory : 192.168.76.171

Les deux ordinateurs étaient sur le même Wi-Fi.
Dans la suite, IP_MACHINE_A et IP_MACHINE_B sont ces deux adresses, selon qui était le
membre A (au tour 1 : A = 192.168.76.168 et B = 192.168.76.171, au tour 2 c'est l'inverse).
Ports : 3000 pour l'application de A, 3001 pour la copie de B, 8181 pour nginx.

Ce qu'on a fait

Installation de Flask :

    python -m venv .venv
    .venv\Scripts\activate
    pip install flask

On a aussi ouvert les ports 3000, 3001 et 8181 dans le pare-feu et trouvé notre adresse
avec ipconfig.

Le membre A lance l'application :

    python app_RA.py

On va sur http://IP_MACHINE_A:3000/ et on voit le message.

Ensuite A met le code sur GitHub (git init, add, commit, push) et B le récupère avec
git clone. Dans sa copie, B change l'adresse IP pour la sienne et le port pour 3001, mais
il garde les initiales de A. B lance l'application et vérifie sur http://IP_MACHINE_B:3001/.

Lien du dépôt : https://github.com/Ryan540gh/labo5-RA.git

Le membre A installe nginx dans C:\nginx et modifie conf\nginx.conf. La partie importante :

    upstream labcluster {
      server IP_MACHINE_A:3000;
      server IP_MACHINE_B:3001;
    }
    server {
      listen 8181 default_server;

      location / {
        proxy_pass http://labcluster;
        try_files $uri $uri/ =404;
      }
    }

Puis dans C:\nginx :

    nginx -t
    start nginx

Réponses aux questions

Étape 5 : Oui l'application est démarrée, la page affiche
"Hello, World! From RA: 192.168.76.168" (au tour 1, quand Rayane était le membre A).

Étape 6 : Quand on arrête l'application et qu'on recharge la page, elle ne s'affiche plus.
Le navigateur dit que le site est inaccessible. Il n'y a plus rien qui écoute sur le
port 3000, donc il faut que le programme tourne pour que le site marche.

Étape 16 : Sur http://IP_MACHINE_A:8181/, quand on rafraîchit plusieurs fois, le message
change. Une fois on voit l'adresse de A et une fois celle de B. Les initiales sont les
mêmes parce que c'est le même code, mais ce n'est pas la même machine qui répond. nginx
envoie les requêtes aux deux applications chacune son tour.

Étape 17 : On arrête l'application de A.
a) http://IP_MACHINE_A:3000/ n'est plus accessible, parce que l'application est arrêtée.
b) http://IP_MACHINE_A:8181/ est encore accessible, mais on voit toujours l'adresse de B.
nginx ne peut plus joindre A alors il envoie tout à B. Quand on relance A, ça recommence
à alterner.

Problèmes qu'on a eus

- La commande .venv\Scripts\activate n'était pas reconnue parce qu'on était dans le dossier
  cloné et le .venv était dans le dossier d'avant. Il fallait faire ..\.venv\Scripts\activate
- Quand on change nginx.conf il faut faire nginx -s reload sinon rien ne change.

Ce qu'on a appris

- Une application Flask répond seulement quand le programme Python tourne.
- nginx peut répartir les requêtes entre plusieurs machines. Le client connaît seulement
  l'adresse de nginx, il ne sait pas quelle machine répond.
- Si une machine tombe, l'autre continue de répondre, donc le site reste disponible.
- On peut ajouter des machines s'il y a plus de requêtes, sans changer l'adresse pour
  les clients.
- Ça marche bien ici parce que l'application ne garde aucune donnée. Notre serveur du
  labo 4 garde les tickets en mémoire, donc si on le copiait sur deux machines chaque copie
  aurait ses propres tickets. Il faudrait une base de données commune.
