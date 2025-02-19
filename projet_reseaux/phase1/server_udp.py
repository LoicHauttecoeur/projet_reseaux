import socket

# Paramètres du serveur
HOST = '0.0.0.0'
PORT = 12345

# Création du socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Serveur UDP en attente de messages sur le port {PORT}...")

# Réception d'un message
message, client_address = server_socket.recvfrom(1024)
print(f"Message reçu de {client_address} : {message.decode()}")

# Envoi d'une réponse
server_socket.sendto("Message bien reçu".encode(), client_address)

# Fermeture du socket
server_socket.close()
