"""
ce preogramme est une simulation parfaite pour le jeu de casino, 
le programme demande le nom de joueur et il l'affiche, après il demande
le montant que le joueur veut deposer, puis choisir un chiffre compris entre 0 et 49:
le joueur mise une certaine somme selon son depot.
la roulette tourne, si le joueur a choisi le bon numero sa mise est multipliée par 3, 
s'il tombe sur la bonne couleur, il gagne 50 pourcent de sa mise:
Ecrit par :
            KAYOUM
            le, 20/04/2022
"""

import random #importation de module random
from math import ceil 

depot = 0 #Variable qui va stocker le depot
continue_partie = True #variable qui controle la boucle while, s'il faut continer la partie ou pas
nom = None #Variable qui va stocker le nom, nom = ""


while continue_partie: #boucle qui commence le jeu, 
    
    while not nom or nom.isspace(): #boucle qui force l'utilisateur à mettre son, 
        nom = input("Entrez votre Nom: ")
        print() #print vide pour un peu de lisibité dans la console
        nom = nom.upper()
    print("WELCOME DANS LE CASINO", nom.strip()) #Afiicher le nom du joueur, et supprime les espaces du debut
      
    print() 
    
    #demander le joueur à mettre quelque une somme superieur à 0
    while depot <= 0:
        depot = input("Entrez le Montant de votre depot: ")
        try:
            depot = int(depot)
        except:
            print("Vous n'avez pas entrez un nombre")
            depot = 0
            continue
        if depot <= 0:
            print("le depot doit etre superieur à 0")
            
    print()        
    print(f"Vous Disposez ${depot}") #affiche la somme que le joeur dispose, on affichera chaque fois qu'il joue
    print()
    
    
    #Demander le joueur de choisir un nombre entre 0 à 49
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

    mise = 0
    while mise > depot or mise <= 0:
        mise = input("Entrez le montant que vous souhaitez miser: ")
        try:
            mise = float(mise)
        except:
            print("Vous n'avez pas entré une mise valide")
            mise = 0
            continue
        if mise > depot: 
            print(f"Vous ne pouvez pas miser autant, vous avez ${depot} ")
        if mise <= 0:
            print("Votre mise est nulle ") 
                  
    numero_gagnant = random.randint(0, 49) #nombre tiré au hasard 
    
    print()
    print("le Numero tiré est .....................", numero_gagnant)
    print()
    
    if numero_user == numero_gagnant:
        print(f"BOOOOOOOOOOOM BRAVO! Vous avez gagné, ${mise * 3}")
        depot += mise * 3
        print()
    elif numero_user % 2 == numero_gagnant % 2:
        mise = ceil(mise * 0.5)
        print(f"BOM ! Vous avez misé sur la bonne couleur, vous gagnez ${mise}")
        depot += mise
        print()
    else:
        print("Vous aurez plus de chance la prochaine fois")
        depot -= mise
    print()   
        
        
    if depot <= 0:
        print("Vous ne disposez plus de fonds")
        continue_partie = False   
    else:
        print(f"Vous avez à present ${depot}")
        print()
        quitter = input("Souhaitez-vous quiter le casino Oui/Non ? ")
        if quitter.lower() == "o" or quitter.lower() == "oui":
            continue_partie = False
            
            print(f"Vous quitez le casino avec ${depot} des gains")
        
    