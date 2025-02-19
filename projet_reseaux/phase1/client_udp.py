import socket

# Paramètres du serveur
HOST = '127.0.0.1'
PORT = 12345

# Création du socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envoi d'un message
message = "Hello, Serveur UDP!"
client_socket.sendto(message.encode(), (HOST, PORT))

# Réception de la réponse
response, _ = client_socket.recvfrom(1024)
print(f"Réponse du serveur : {response.decode()}")

# Fermeture du socket
client_socket.close()
