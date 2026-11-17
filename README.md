 Laboratoire 5 — Déploiement et distribution de charge
6GEI311 — Architecture des logiciels

Membres de l’équipe :
- Rayane Alimi
- ADISSO Allglory

1. Résumé des apprentissages lors du lab 

Ce laboratoire nous a permis de déployer une application web Flask
sur nos deux machines et de configurer Nginx comme distributeur de charge.
Nous avons utilisé GitHub pour partager le code entre les membres
de l’équipe.

Nous avons appris à distinguer l’accès direct à une instance Flask
de l’accès au service par Nginx. Les manipulations nous ont permis
d’observer la distribution des requêtes entre les deux instances
ainsi que le maintien du service lorsqu’une instance est arrêtée.

Chaque membre a joué le rôle A pour son propre code et le rôle B
pour le code de son coéquipier.

2. Réponses aux questions

 Étape 6 — Arrêt de l’application Flask

Après avoir arrêté l’application Python, nous avons essayé d’accéder
de nouveau à http://IP_MACHINE_A:3000/.

La page n’était plus accessible : le navigateur ne pouvait plus
se connecter à l’application. En effet, l’arrêt du programme Flask
arrête le serveur qui répond aux requêtes sur le port 3000.

 Étape 16 — Actualisations de la page accessible par Nginx

En accédant à http://IP_MACHINE_A:8181/ et en actualisant plusieurs
fois la page, nous avons constaté que l’adresse IP affichée dans
le message changeait entre celle de la machine A et celle de la
machine B.

Cela montre que Nginx distribuait les requêtes entre les deux instances
Flask. L’adresse dans la barre du navigateur restait celle de Nginx,
mais la réponse pouvait provenir de l’une ou l’autre des machines.

Étape 17 — Arrêt de l’instance sur la machine A

 a) Accès direct : http://IP_MACHINE_A:3000/

L’application n’était plus accessible à cette adresse, puisque
l’instance Flask de la machine A était arrêtée.

 b) Accès par Nginx : http://IP_MACHINE_A:8181/

Le service restait accessible par Nginx grâce à l’instance Flask
qui fonctionnait encore sur la machine B. La page affichait alors
l’adresse IP de la machine B.

Cette expérience illustre la tolérance à la panne d’une instance
applicative. Nginx devait toutefois rester en fonctionnement
sur la machine A : nous avions arrêté Flask, et non la machine
complète ou Nginx.

3. Conclusion

La distribution de charge permet de répartir les requêtes entre
plusieurs instances d’une application. Elle améliore également
la disponibilité du service lorsqu’une instance devient indisponible,
à condition qu’une autre instance et le distributeur de charge
restent opérationnels.
