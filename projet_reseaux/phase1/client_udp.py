import socket

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        message = input("💬 Entrez un message (ou 'exit' pour quitter, 'shutdown' pour éteindre le serveur) : ")
        if message.lower() in ['exit', 'shutdown']:
            client_socket.sendto(message.encode(), (HOST, PORT))
            break
        client_socket.sendto(message.encode(), (HOST, PORT))
        response, _ = client_socket.recvfrom(1024)
        print(f"📩 Réponse du serveur : {response}")

except Exception as e:
    print(f"⚠️ Erreur : {e}")
finally:
    client_socket.close()
    print("🔴 Connexion fermée proprement.")