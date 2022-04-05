"""
generateur de mot de passe, 
"""

import random #importer random

print("Welcome in passeword generation") #affiche le message 
print()
caract = "azertyuiopqsdfghjklmwxcvbn0123456789AZERTYUIOPQSDFGHJKLMWXCVBN&é(-è_çà)=,;:!<>." #les caracteres qui vont permettre generer le mot de passe

longueur = input("Quelle sera la longueur de votre passeword: ") #mettez la longueur du mot de passe que vous voulez
longueur = int(longueur)

nombre = input("Combien de mot de passe voulez vous: ") #combien de mot de passes voulez-vous generer
nombre = int(nombre)

#la boucle qui genere 
for md in range(nombre):
    passeword = ""
    for i in range(longueur):
        passeword += random.choice(caract) #melange de caracteres
    print(passeword)
