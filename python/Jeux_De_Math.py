"""
Jeu de math, l'objectif de ce jeux est de demander à l'utilisateur d'effectuer des calculs,
et verifier si ses reponses sont correctes ou non, et enfin afficher la note qu'il a eue.
on peut adapter le nombre de questions !
ceci est un programme de debutant, ça m'a permis d'apprendre les bases du langage PYTHON !

"""
import random

nbr_min = 2
nbr_max = 5

NOMBRE_DE_QUESTION = 4

def poser_question():
    a = random.randint(nbr_min, nbr_max)
    b = random.randint(nbr_min, nbr_max)
    o = random.randint(0, 3) #melange les operateurs + - *

    if o == 1:
       operateur_str = "-"
    elif o == 2:
        operateur_str = "+"
    else:
        operateur_str = "*"

    user = 0 #poser la question à l'utilisateur, avec l'obligation de mettre un chiffre
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

    if user == calcul: #Verification si l'utilisateur donne le bonne reponse
        return True

    return False

note = 0
for i in range(0, NOMBRE_DE_QUESTION): #la boucle quicontrole le nombre des questions, et qui verifie les reponses
    print(f"La question Numero {i+1} sur {NOMBRE_DE_QUESTION}")
    if poser_question():
        note += 1
        print("CORRECTE")
    else:
        print("INCORECT")
    print()

print(f"Votre note Finale est de : {note} / {NOMBRE_DE_QUESTION}") #affichage du note obtenue par l"user

"""
verification si l'utilisateur a eu la moyenne ou pas, et aussi, s'il a trouvé toutes les réponses !
"""

if note == NOMBRE_DE_QUESTION:
    print("EXELLENT")
elif note >= NOMBRE_DE_QUESTION / 2:
    print("Bravo !Vous avez eu la moyenne")
elif note == 0:
    print("Revisser vos cours de math")
else:
    print("Fournir,un peu d'effort")
