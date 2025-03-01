import socket

HOST = '213.223.220.44'
PORT = 8889

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("✅ Connexion au serveur TCP réussie.")

    while True:
        message = input("💬 Entrez un message (ou 'exit' pour quitter, 'shutdown' pour éteindre le serveur) : ")
        if message.lower() in ['exit', 'shutdown']:
            client_socket.send(message.encode())
            break
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"📩 Réponse du serveur : {response}")

except ConnectionRefusedError:
    print("❌ Impossible de se connecter au serveur. Assurez-vous qu'il est en cours d'exécution.")
except Exception as e:
    print(f"⚠️ Erreur : {e}")
finally:
    client_socket.close()
    print("🔴 Connexion fermée proprement.")
