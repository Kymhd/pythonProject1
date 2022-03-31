""" 
un petit projet qui permet de manipuler les listes et se
familiariser avec les slices et les fonctions de listes
"""

def tri_personalise(t): #fonction tri personalisé
    return len(t)

#LA fonction qui affiche les Pizzas

def affiche(collection, nombre=-1):
    if len(collection) == 0: #si la Collection est vide
        print("AUCUN PIZZA")
        return

    collection.sort(reverse=True, key=tri_personalise) #Tri personalisé qui appele la fonction definie tout en haut
    
    print(f"---LISTE DE PIZZA ({len(collection)})---") #Afiiche le nombre de pizzas que contient la collection

    collection_n = collection
    if nombre != -1: #nombre est un paramettre optionnel
        collection_n = collection[0:nombre] #affiche les pizzas selon le parametre optionel, sinon affiche les toutes

    for i in collection_n:
        print(i)
    print()
    print(f"Premier pizza : {collection_n[0]}") #1er pizza
    print(f"Dernière pizza : {collection_n[-1]}") #2em pizza

"PIZZA a ajouter"
#la fonction qui ajoute une pizza dans la collection

def ajouter(collection):
    user = input("Ajouter une Pizza : ")
    if user.lower() in collection :
        print("Cette pizza existe deja")
        return
    else:
        collection.append(user)


pizza = ["4 Frommage", "vegetarien", "hawei", "clazone"]
ajouter(pizza)
affiche(pizza)








