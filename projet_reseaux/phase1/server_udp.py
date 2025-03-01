import socket

HOST = '0.0.0.0'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"✅ Serveur UDP en attente de messages sur le port {PORT}...")

shutdown_flag = False  # Flag pour arrêter le serveur proprement

try:
    while not shutdown_flag:
        message, client_address = server_socket.recvfrom(1024)
        message = message.decode()
        print(f"📩 Message reçu de {client_address} : {message}")

        if message.lower() == "shutdown":
            print("🚨 Arrêt du serveur UDP demandé !")
            shutdown_flag = True
            server_socket.sendto("🔴 Serveur en cours d'arrêt...".encode(), client_address)
            break  # Sort de la boucle pour fermer le serveur

        server_socket.sendto("Message bien reçu".encode(), client_address)
except KeyboardInterrupt:
    print("\n🔴 Fermeture du serveur UDP...")
except Exception as e:
    print(f"⚠️ Erreur : {e}")
finally:
    server_socket.close()
    print("✅ Serveur fermé proprement.")