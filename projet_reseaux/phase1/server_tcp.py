import socket
import threading

# Paramètres du serveur
HOST = '0.0.0.0'
PORT = 8889

# Création du socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"✅ Serveur TCP en attente de connexions sur le port {PORT}...")

# Liste des threads pour fermer proprement
client_threads = []
shutdown_event = threading.Event()  # Flag pour arrêter le serveur

def handle_client(client_socket, client_address):
    print(f"🔗 Connexion acceptée depuis {client_address}")
    try:
        while not shutdown_event.is_set():
            message = client_socket.recv(1024).decode()
            if not message:
                print(f"❌ Client {client_address} déconnecté.")
                break

            print(f"📩 Message reçu de {client_address} : {message}")

            if message.lower() == "shutdown":
                print("🚨 Arrêt du serveur demandé !")
                shutdown_event.set()  # Active l'arrêt du serveur
                client_socket.send("🔴 Serveur en cours d'arrêt...".encode())
                break  # Quitte la boucle pour fermer ce client

            client_socket.send("Message bien reçu".encode())
    except Exception as e:
        print(f"⚠️ Erreur avec {client_address} : {e}")
    finally:
        client_socket.close()

# Thread principal pour accepter les connexions
def accept_connections():
    while not shutdown_event.is_set():
        try:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
            client_threads.append(client_thread)
        except OSError:
            break  # Sort de la boucle si le socket est fermé

# Lancer le thread d'écoute des connexions
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()

# Attendre un signal d'arrêt
try:
    while not shutdown_event.is_set():
        pass  # Attente active

except KeyboardInterrupt:
    print("\n🔴 Fermeture du serveur TCP demandée par l'utilisateur...")

finally:
    print("📌 Fermeture des connexions en cours...")
    shutdown_event.set()  # Déclenche l'arrêt propre des threads
    server_socket.close()
    accept_thread.join()
    for thread in client_threads:
        thread.join()
    print("✅ Serveur fermé proprement.")