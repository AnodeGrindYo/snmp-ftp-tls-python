import socket
import sys

# Fonction pour envoyer une requête SNMP au serveur
def send_snmp_request():
    # Exemple d'envoi de requête SNMP au serveur
    client_socket.send('SNMP'.encode())
    response = client_socket.recv(1024).decode()
    print('Réponse SNMP du serveur:', response)

# Fonction pour envoyer une requête FTP au serveur
def send_ftp_request():
    # Exemple d'envoi de requête FTP au serveur
    client_socket.send('FTP'.encode())
    response = client_socket.recv(1024).decode()
    print('Réponse FTP du serveur:', response)

# Fonction pour envoyer une requête TLS au serveur
def send_tls_request():
    # Exemple d'envoi de requête TLS au serveur
    client_socket.send('TLS'.encode())
    response = client_socket.recv(1024).decode()
    print('Réponse TLS du serveur:', response)

# Point d'entrée principal du client
if __name__ == "__main__":
    # Vérification des arguments de ligne de commande
    if len(sys.argv) < 2:
        print("Usage: python client.py <protocol>")
        sys.exit(1)
    
    # Récupération du protocole à partir des arguments
    protocol = sys.argv[1]
    
    # Création du socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8000)
    client_socket.connect(server_address)
    
    # Envoi du protocole souhaité au serveur
    client_socket.send(protocol.encode())

    # Appel de la fonction correspondant au protocole souhaité
    if protocol == 'SNMP':
        send_snmp_request()
    elif protocol == 'FTP':
        send_ftp_request()
    elif protocol == 'TLS':
        send_tls_request()

    # Fermeture du socket client
    client_socket.close()