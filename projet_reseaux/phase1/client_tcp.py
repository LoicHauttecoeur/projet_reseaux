import socket

# Paramètres du serveur
HOST = '127.0.0.1'  # Adresse du serveur
PORT = 12345

# Création du socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Envoi d'un message
client_socket.send("Hello, Serveur!".encode())

# Réception de la réponse
response = client_socket.recv(1024).decode()
print(f"Réponse du serveur : {response}")

# Fermeture du socket
client_socket.close()
