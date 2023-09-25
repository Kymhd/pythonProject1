
import random
from math import ceil


def depot():
     deposit = 0
     while deposit <= 0:
        deposit = input("Entrez le Montant de votre depot: ")
        try:
            deposit = int(deposit)
        except:
            print("Vous n'avez pas entrez un nombre")
            deposit = 0
            continue
        if deposit <= 0:
            print("le deposit doit etre superieur à 0")        

     print(f"Vous Disposez ${deposit}") #affiche la somme que le joeur dispose, on affichera chaque fois qu'il joue
     return deposit


depot_ = depot()

def numero_joueur (): 
    numero_user = -1 
    
    while numero_user < 0 or numero_user > 49:
        numero_user = input("Enrez votre numero entre <= 0 ------- à ----- 49:=> ")
        try:
            numero_user = int(numero_user)
        except:
            print("Vous n'avez pas entrez un nombre")
            numero_user = -1
            continue
        if numero_user > 49:
            print("Ce numéro est superieur à 49")
        if numero_user < 0:
            print("Ce numéro est négatif")

    return numero_user

joueur_numero = numero_joueur()