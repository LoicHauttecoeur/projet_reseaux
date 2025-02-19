import socket

# Paramètres du serveur
HOST = '0.0.0.0'  # Écoute sur toutes les interfaces réseau
PORT = 12345

# Création du socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Permet jusqu'à 5 connexions en attente

print(f"Serveur en attente de connexion sur le port {PORT}...")

# Accepter une connexion
client_socket, client_address = server_socket.accept()
print(f"Connexion acceptée depuis {client_address}")

# Recevoir un message
message = client_socket.recv(1024).decode()
print(f"Message reçu : {message}")

# Envoyer une réponse
client_socket.send("Message bien reçu".encode())

# Fermer la connexion
client_socket.close()
server_socket.close()
