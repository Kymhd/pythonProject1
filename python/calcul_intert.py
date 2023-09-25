# # def calculer_taux_simple(montant, taux, periode):
# #     return f"{(montant)*(taux/360)*(periode)}%"


# # def calcul_taux_compose(montant, taux, annee):
# #     valeur = 100 * (1 + taux)**annee
# #     return f"{round(valeur, 0)}%"

# # # print(calcul_taux_compose(100, 0.1, 10))
# # # print(calculer_taux_simple(1000, 0.05, 360))

# # print("--Bienvenue dans cette app qui permet de caclculer le taux d'interet--")


# def extraire_nombre_pourcentage(chaîne):

#     if chaîne.isdigit():
#         return int(chaîne)
#     elif '%' in chaîne:
#         pourcentage, _ = chaîne.split('%')  # Divise la chaîne au symbole '%'
        
#         try:
#             nombre_entier = int(pourcentage)  # Tente de convertir la partie entière en nombre entier
#             return nombre_entier
#         except ValueError:
#             return None  # Retourne None si la conversion échoue
#     else:
#         return None

# # Exemple d'utilisation
# pourcentage_saisi = input("Entrez un pourcentage (par exemple 50%) : ")
# nombre_entier = extraire_nombre_pourcentage(pourcentage_saisi)

# if nombre_entier is not None:
#     print("Le nombre entier extrait est :", nombre_entier * 2)
# else:
#     print("La saisie n'est pas un pourcentage valide.")

def calculer_interet_simple(capital, taux, duree_jours):
    interet = (capital * taux * duree_jours) / 100
    montant_final = capital + interet
    return montant_final

def calculer_interet_compose(capital, taux, duree_jours):
    montant_final = capital * (1 + taux / 100) ** duree_jours
    return montant_final

def saisir_nombre_positif(message):
    while True:
        try:
            nombre = float(input(message))
            if nombre >= 0:
                return nombre
            else:
                print("Le nombre doit être positif.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def mois_en_jours(mois):
    return mois * 30  # Suppose que chaque mois a 30 jours

def main():
    print("Bienvenue dans le calculateur d'intérêts !")
    capital = saisir_nombre_positif("Entrez le montant du capital : ")
    taux = saisir_nombre_positif("Entrez le taux d'intérêt (%) : ")
    
    duree_type = input("Choisissez le type de durée (jours/mois) : ").lower()
    
    if duree_type == "jours":
        duree = saisir_nombre_positif("Entrez la durée en jours : ")
    elif duree_type == "mois":
        mois = saisir_nombre_positif("Entrez la durée en mois : ")
        duree = mois_en_jours(mois)
    else:
        print("Type de durée non valide. Veuillez choisir 'jours' ou 'mois'.")
        return
    
    print("\nChoisissez le type d'intérêt :")
    print("1. Intérêt simple")
    print("2. Intérêt composé")
    
    choix = input("Entrez le numéro de votre choix : ")
    
    if choix == "1":
        montant_final = calculer_interet_simple(capital, taux, duree)
        print(f"Le montant final avec intérêt simple est : {montant_final:.2f}")
    elif choix == "2":
        montant_final = calculer_interet_compose(capital, taux, duree)
        print(f"Le montant final avec intérêt composé est : {montant_final:.2f}")
    else:
        print("Choix non valide. Veuillez choisir 1 ou 2.")

if __name__ == "__main__":
    main()
