# Projet SNMP, FTP, TLS en Python

Ce projet présente des exemples d'implémentation des protocoles SNMP, FTP et TLS en utilisant Python. Chaque protocole est implémenté dans un module séparé, offrant des fonctionnalités de base pour communiquer avec des équipements réseau, transférer des fichiers via FTP et sécuriser les connexions avec TLS.

## SNMP (Simple Network Management Protocol)

Le SNMP est un protocole de gestion de réseau largement utilisé pour superviser et gérer des équipements réseau tels que des routeurs, des commutateurs, des imprimantes, etc. Le module SNMP dans ce projet fournit une base pour l'envoi de requêtes SNMP à un serveur SNMP et la réception des réponses correspondantes. Vous pouvez personnaliser la logique de traitement des requêtes SNMP dans la fonction `send_snmp_request()` du fichier `client.py` pour effectuer des opérations spécifiques à votre environnement réseau.

Pour en apprendre plus sur SNMP, vous pouvez consulter les ressources suivantes :
- [Wikipedia - SNMP](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol)
- [SNMP Tutorial](https://www.snmpsharpnet.com/snmp-tutorial/)

## FTP (File Transfer Protocol)

Le FTP est un protocole standard pour le transfert de fichiers entre des systèmes distants sur un réseau TCP/IP. Le module FTP dans ce projet fournit une base pour l'envoi de requêtes FTP à un serveur FTP et la gestion du transfert de fichiers. Vous pouvez personnaliser la logique de traitement des requêtes FTP dans la fonction `send_ftp_request()` du fichier `client.py` pour effectuer des opérations de transfert de fichiers spécifiques, telles que l'envoi et la réception de fichiers.

Pour en apprendre plus sur FTP, vous pouvez consulter les ressources suivantes :
- [Wikipedia - File Transfer Protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [FTP Tutorial](https://www.tutorialspoint.com/ftp/index.htm)


## TLS (Transport Layer Security)

Le TLS est un protocole de sécurité qui permet de sécuriser les communications sur un réseau en fournissant un chiffrement de bout en bout et une authentification des parties impliquées. Le module TLS dans ce projet fournit une base pour établir une connexion sécurisée avec un serveur utilisant TLS. Vous pouvez personnaliser la logique de traitement des requêtes TLS dans la fonction `send_tls_request()` du fichier `client.py` pour effectuer des opérations sécurisées spécifiques, telles que l'envoi de données confidentielles sur un canal sécurisé.

Pour en apprendre plus sur TLS, vous pouvez consulter les ressources suivantes :
- [Wikipedia - Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [Mozilla Developer Network - TLS](https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security_TLS)


## Contenu du projet

- `server.py` : Fichier contenant l'implémentation du serveur pour chaque protocole.
- `client.py` : Fichier contenant l'implémentation du client pour chaque protocole.
- `test_client.py` : Fichier contenant les tests unitaires pour les fonctionnalités du client.
- `test_integration.py` : Fichier contenant les tests d'intégration pour vérifier l'interaction correcte entre le client et le serveur.
- `requirements.txt` : Fichier contenant la liste des dépendances Python requises pour exécuter le projet.

## Utilisation

### Utilisation du serveur

Le fichier `server.py` contient l'implémentation du serveur pour chaque protocole. Pour exécuter le serveur, suivez les étapes suivantes :

1. Assurez-vous d'avoir Python installé sur votre système.
2. Ouvrez un terminal et accédez au répertoire du projet.
3. Exécutez la commande suivante : `python server.py`.

Le serveur démarrera et sera en attente de connexions entrantes sur le port spécifié (par exemple, le port 8000). Vous pouvez modifier le port en modifiant la valeur de la variable `server_address` dans le fichier `server.py`.

### Utilisation du client

Le fichier `client.py` contient l'implémentation du client pour chaque protocole. Pour exécuter le client, suivez les étapes suivantes :

1. Assurez-vous d'avoir Python installé sur votre système.
2. Ouvrez un terminal et accédez au répertoire du projet.
3. Exécutez la commande suivante : `python client.py <protocol>`, en remplaçant `<protocol>` par le protocole souhaité (parmi SNMP, FTP et TLS).

Le client se connectera au serveur sur l'adresse et le port spécifiés (par exemple, `localhost:8000`). Vous pouvez modifier ces informations en modifiant les variables `server_address` et `server_port` dans le fichier `client.py`.

Assurez-vous que le serveur est en cours d'exécution avant de lancer le client. Vous pouvez également personnaliser la logique de traitement des requêtes dans les fonctions du serveur et du client pour répondre à vos besoins spécifiques.

N'hésitez pas à explorer les autres fichiers du projet pour voir les détails d'implémentation spécifiques à chaque protocole.
