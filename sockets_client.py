from datetime import time
import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connexion sur {HOST_IP}, port {HOST_PORT}.")
while 1: 
    try: 
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError: 
        print("Erreur: imposible de se connecter au serveur.\nReconnexion...")
        time.sleep(4)
    else: 
        print("Connecté au serveur")
        break
while 1:
    data_recues = s.recv(MAX_DATA_SIZE)
    if not data_recues:
        break
    print("Messages ", data_recues.decode())
    text_envoye = input("Vous: ")
    s.sendall((text_envoye).encode())

# else: 
#     print("Aucune data")
s.close()