

import os
import subprocess

while 1: 
    commande = input(os.getcwd() +"> ") 
    if commande == "exit": 
        break

    commande_split = commande.split(" ")

    if len(commande_split) == 2 and commande_split[0] == "cd" :
        try:
            os.chdir(commande_split[1])
        except FileNotFoundError:
            print("Erreur: Ce dossier n'existe pas.")
    else: 
        resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)

        print(resultat.stdout)
        print(resultat.stderr)

