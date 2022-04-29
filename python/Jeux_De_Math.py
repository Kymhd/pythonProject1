"""
Jeu de math, l'objectif de ce jeux est de demander à l'utilisateur d'effectuer des calculs,
et verifier si ses reponses sont correctes ou non, et enfin afficher la note qu'il a eue.
on peut adapter le nombre des questions !
ceci est un programme de debutant, ça m'a permis d'apprendre les bases du langage PYTHON !

"""
import random #importation du module random

#Varibles qui vont stocker les nombre min et max, cela s'adaptera selon le niveau de l'user
# ces deux variables sont globals
nbr_max = 0 
nbr_min = 0

#une petite liste qui stock les differents niveaux à afficher
liste = [
    "Débutant",
    "Intermediaire",
    "Gourou"
]
print()

print("BIENVENUE DANS LE JEU DE MATH")
print()

print("Quel est votre niveau parmis les 3 ?".upper())

#boucle qui va parcourrir la liste et afficher les niveaux de l'USER
for compter, i in enumerate(liste): #enumerte pour afficher les elements de la liste avec des numeros d'orde 1 2 3
    print(f"{i.upper()} ==> {compter+1}") # on affiche les elements en majiscule i.upper()


print() #print vide

#fonction qui va demander le niveau de l'USER
def niveau():
    """
    
    """
    global nbr_min
    global nbr_max
    niveau = 0
    while niveau <= 0 or niveau > 3:
        niveau = input("ENTREZ VOTRE NIVEAU 1, 2 ou 3 ! ")
        try:
            niveau = int(niveau)
        except ValueError:
            print("VOUS N'AVEZ PAS ENTREZ UN NOMBRE")
            niveau = -1
            continue
        print()
        if niveau > 3:
            print(f"{niveau} NE FAIT PAS PARTIE ! CHOISISEZ ENTRE 1, 2 et 3")
            print()
        if niveau <= 0:
            print("CHOISISSEZ ENTRE 1, 2 et 3")

    if niveau == 1:
        nbr_min = 2
        nbr_max = 7

    elif niveau == 2:
        nbr_min = 2
        nbr_max = 16

    else:
        nbr_min = 2
        nbr_max = random.randint(9, 60)

    return nbr_min, nbr_max


def poser_question():
    a = random.randint(nbr_min, nbr_max)
    b = random.randint(nbr_min, nbr_max)
    o = random.randint(0, 3)  # melange les operateurs + - *

    if o == 1:
        operateur_str = "-"
    elif o == 2:
        operateur_str = "+"
    else:
        operateur_str = "*"

    user = 0  # poser la question à l'utilisateur, avec l'obligation de mettre un chiffre
    while user == 0:
        user_str = input(f"{a} {operateur_str} {b} = ")
        try:
            user = int(user_str)
        except ValueError:
            print("ERREUR ! Vous devez entre un chiffre pour ce jeux")

    calcul = a + b
    if o == 1:
        calcul = a - b
    elif o == 2:
        calcul = a + b
    else:
        calcul = a * b

    if user == calcul:  # Verification si l'utilisateur donne le bonne reponse
        return True

    return False


def demander_nbr_question():
    nbre = 0
    while nbre <= 0:
        nbre = input("Entrez le nombre de question que vous souhaitez jouer: ")
        try:
            nbre = int(nbre)
        except ValueError:
            print("Vous n'avez pas entre un chiffre")
            nbre = -1
            continue
        if nbre < 0:
            print("Vous avez entrez un nombre negatif")
        if nbre == 0:
            print("ERREUR, Vous avez entrez 0")
    return nbre


nombre_max, nombre_min = niveau()
NOMBRE_DE_QUESTION = demander_nbr_question()

print()
note = 0
# la boucle quicontrole le nombre des questions, et qui verifie les reponses
for i in range(0, NOMBRE_DE_QUESTION):
    print(f"La question Numero {i+1} sur {NOMBRE_DE_QUESTION}")
    if poser_question():
        note += 1
        print("CORRECTE")
    else:
        print("INCORECT")
    print()

# affichage du note obtenue par l"user
print(f"Votre note Finale est de : {note} / {NOMBRE_DE_QUESTION}")

"""
verification si l'utilisateur a eu la moyenne ou pas !
"""

if note == NOMBRE_DE_QUESTION:
    print("EXELLENT")
elif note >= NOMBRE_DE_QUESTION / 2:
    print("Bravo !Vous avez eu la moyenne")
elif note == 0:
    print("Revisser vos cours de math")
else:
    print("Fournir,un peu d'effort")
