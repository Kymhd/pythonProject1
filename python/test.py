#coding: utf-8
from prettytable import PrettyTable
import random
import csv
import datetime
from collections import Counter
import matplotlib.pyplot as plt


"""
Programme qui permet d'ajouter des eleves dans un fichier CSV qui va genenere leur marticule 
automatiquement !
Il y plusierus fonctionnalités, 
Entierement ou presque ecrit par ChatGPT 😁😁😁😁

+----------------------+---------+------------+---------------+-------+---------------+
| Matriculation Number |   Name  | First Name | Study Program | Serie | Date of Birth |
+----------------------+---------+------------+---------------+-------+---------------+
|      2023NK529H      | Zignama |   Abdou    |   Management  |   D   |   25-08-1997  |
|      2023CL287T      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
|      2023FP386P      |  Abdou  |   KAZAD    |  Philosophie  |   D   |   12-02-1999  |
|      2023OX731D      |  Abdou  |   KAZAD    |  Philosophie  |   D   |   12-02-1999  |
|      2023TH189E      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
|      2023XP017E      |  Abdou  |   KAZAD    |  Philosophie  |   D   |   12-02-1999  |
|      2023ZJ712Q      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
|      2023MO450I      |  Abdou  |   KAZAD    |  Philosophie  |   D   |   12-02-1999  |
|      2023MH839Z      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
|      2023IV716U      |  Abdou  |   KAZAD    |  Philosophie  |   D   |   12-02-1999  |
|      2023WH436S      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
|      2023VU205F      |  Abdou  |   KAZAD    |  Philosophie  |   D   |   12-02-1999  |
|      2023EP495F      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
|      2023WB248X      |  Abdou  |   KAZAD    |  Philosophie  |   D   |   12-02-1999  |
|      2023IG315O      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
|      2023WY907X      |  Abdou  |   KAZAD    |  Philosophie  |   D   |   12-02-1999  |
|      2023UG216E      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
|      2023OY209C      |  Abdou  |   KAZAD    |  Philosophie  |   D   |   12-02-1999  |
|      2023XI270D      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
|      2023QW139W      |  Kayoum |   Abdou    |      CMGP     |   D   |   25-02-1998  |
+----------------------+---------+------------+---------------+-------+---------------+

"""
class Student:

    def __init__(self):
        self.info = {
            "Matriculation Number": "Informations incomplètes",
            "Name": None,
            "First Name": None,
            "Study Program": None,
            "Serie": None,
            "Date of Birth": None,
            "institution email": "Informations incomplètes"
        }

    def fill_information(self, name, first_name, study_program, serie, date_of_birth):
        self.info["Name"] = name
        self.info["First Name"] = first_name
        self.info["Study Program"] = study_program
        self.info["Serie"] = serie

        try:
            date_obj = datetime.datetime.strptime(date_of_birth, "%d-%m-%Y")
            self.info["Date of Birth"] = date_obj.strftime("%d-%m-%Y")
        except ValueError:
            print("Erreur: Format de date de naissance incorrect. Utilisez le format dd-mm-yyyy.")

        # Générer la matricule uniquement si toutes les informations sont remplies
        if all(len(value.strip()) > 0 for key, value in self.info.items() if (key != "Matriculation Number") or (key != "institution email")):
            current_year = datetime.date.today().year
            random_letters = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2))
            random_letter = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1))
            random_int = ''.join(random.sample('0123456789', 3))
            self.info["Matriculation Number"] = f"{current_year}{random_letters}{random_int}{random_letter}"
            first_name_no_space = first_name.replace(" ", "").lower()
            name_no_space = name.replace(" ", "").lower()
            self.info["institution email"] = f"{first_name_no_space}.{name_no_space}@udc.edu.km"


    def display_info(self):
        pass  # Aucun besoin de l'afficher individuellement ici

def afficher_tous_les_etudiants(liste_etudiants):
    print("Liste de tous les étudiants :")
    for etudiant in liste_etudiants:
        print(etudiant.info)
        


def chercher_etudiant_par_matricule(matricule):
    # Lire les informations des étudiants depuis le fichier CSV
    students_from_csv = []

    with open('students.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            student = Student()
            student.info = row
            students_from_csv.append(student)

    # Chercher l'étudiant par matricule dans la liste lue depuis le CSV
    for etudiant in students_from_csv:
        if etudiant.info["Matriculation Number"] == matricule:
            return etudiant

    return None  # Renvoie None si l'étudiant n'est pas trouvé

students = []

student1 = Student()
student1.fill_information("Innoussa", "AHAMADI", "Médcine", "C", "1-12-2001")
students.append(student1)

#Ajoutez les étudiants supplémentaires
student2 = Student()
student2.fill_information("Anrifidine", "Asco", "LEA", "A4", "12-06-2000")
students.append(student2)

student3 = Student()
student3.fill_information("Daoulati", "Bere", "Anglais", "G", "8-08-2001")
students.append(student3)

# Afficher tous les étudiants
# afficher_tous_les_etudiants(students)

# Chercher un étudiant par matricule
matricule_recherche = " 2023XE319D  ".upper().strip() # Remplacez par le matricule que vous voulez rechercher
etudiant_trouve = chercher_etudiant_par_matricule(matricule_recherche)

if etudiant_trouve:
    print("Étudiant trouvé :")
    table = PrettyTable()
    table.field_names = ["Matriculation Number", "Name", "First Name", "Study Program", "Serie", "Date of Birth", "institution email"]
    table.add_row([
        etudiant_trouve.info["Matriculation Number"],
        etudiant_trouve.info["Name"],
        etudiant_trouve.info["First Name"],
        etudiant_trouve.info["Study Program"],
        etudiant_trouve.info["Serie"],
        etudiant_trouve.info["Date of Birth"],
        etudiant_trouve.info["institution email"]
    ])
    print(table)
else:
    print(f"Étudiant non trouvé pour le matricule : {matricule_recherche}")


# Créez un tableau unique pour tous les étudiants avec en-tête
table = PrettyTable()
table.field_names = ["Matriculation Number", "Name", "First Name", "Study Program", "Serie", "Date of Birth", "institution email"]

for student in students:
    table.add_row([
        student.info["Matriculation Number"],
        student.info["Name"],
        student.info["First Name"],
        student.info["Study Program"],
        student.info["Serie"],
        student.info["Date of Birth"],
        student.info["institution email"]
    ])

print(table)




def trier_etudiants_depuis_csv(critere_tri, est_serie=True):
    if critere_tri not in ["A1", "A2", "A3", "A4", "C", "D", "G", "CMGP", "Philosophie", "AES"]:
        print(f"Le critère de tri '{critere_tri}' n'est pas valide.")
        return

    # Lire les informations des étudiants depuis le fichier CSV
    students_from_csv = []

    with open('students.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            student = Student()
            student.info = row
            students_from_csv.append(student)

    # Fonction de tri personnalisée pour prendre en compte la casse et les espaces
    def custom_sort_key(etudiant):
        if est_serie:
            return etudiant.info["Serie"]
        else:
            return etudiant.info["Study Program"]

    # Triez les étudiants en utilisant la fonction de tri personnalisée
    students_from_csv.sort(key=custom_sort_key)

    # Affichez les étudiants triés
    critere_label = "Série" if est_serie else "Filière"
    print(f"Étudiants triés par {critere_label} '{critere_tri}' depuis le fichier CSV :")
    table = PrettyTable()
    table.field_names = ["Matriculation Number", "Name", "First Name", "Study Program", "Serie", "Date of Birth", "institution email"]

    for etudiant in students_from_csv:
        if (est_serie and etudiant.info["Serie"] == critere_tri) or \
           (not est_serie and etudiant.info["Study Program"] == critere_tri):
            table.add_row([
                etudiant.info["Matriculation Number"],
                etudiant.info["Name"],
                etudiant.info["First Name"],
                etudiant.info["Study Program"],
                etudiant.info["Serie"],
                etudiant.info["Date of Birth"],
                student.info["institution email"]
            ])

    print(table)

print()
# Utilisation de la fonction pour trier les étudiants par série depuis le fichier CSV
tri_critere_serie = "A1"  # Remplacez par la série que vous souhaitez utiliser
trier_etudiants_depuis_csv(tri_critere_serie, est_serie=True)

# Utilisation de la fonction pour trier les étudiants par filière depuis le fichier CSV
# tri_critere_filiere = "Géstion"  # Remplacez par la filière que vous souhaitez utiliser
# trier_etudiants_depuis_csv(tri_critere_filiere, est_serie=False)




def afficher_tendances_filieres():
    # Lire les informations des étudiants depuis le fichier CSV
    students_from_csv = []

    with open('students.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            student = Student()
            student.info = row
            students_from_csv.append(student)

    # Extraire les filières des étudiants et compter leur fréquence
    filieres = [etudiant.info["Study Program"] for etudiant in students_from_csv]
    tendances_filieres = Counter(filieres)

    # Créer un graphique à barres pour les tendances des filières
    filieres_labels = list(tendances_filieres.keys())
    nombre_etudiants = list(tendances_filieres.values())

    plt.figure(figsize=(10, 6))  # Définir la taille du graphique
    plt.barh(filieres_labels, nombre_etudiants, color='skyblue')
    plt.xlabel('Nombre d\'étudiants')
    plt.ylabel('Filière')
    plt.title('Tendances des filières pour les étudiants inscrits')
    plt.gca().invert_yaxis()  # Inverser l'axe y pour afficher les filières les plus populaires en haut

    plt.show()



# Utilisation de la fonction pour afficher les tendances des filières avec un graphique
afficher_tendances_filieres()



def afficher_moyenne_age_etudiants_depuis_csv():
    # Lire les informations des étudiants depuis le fichier CSV
    students_from_csv = []

    with open('students.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            student = Student()
            student.info = row
            students_from_csv.append(student)

    # Calculer l'âge de chaque étudiant et stocker les âges dans une liste
    ages = []
    for etudiant in students_from_csv:
        date_naissance_str = etudiant.info["Date of Birth"]
        try:
            date_naissance = datetime.datetime.strptime(date_naissance_str, "%d-%m-%Y")
            age = datetime.datetime.now().year - date_naissance.year
            ages.append(age)
        except ValueError:
            print(f"Erreur de format de date de naissance pour l'étudiant : {etudiant.info['Name']}")

    # Calculer la moyenne d'âge
    if len(ages) > 0:
        moyenne_age = sum(ages) / len(ages)
        print("\nMoyenne d'âge des étudiants:")
        print("=" * 30)
        print(f"{moyenne_age:.2f} ans")
        print("=" * 30)
    else:
        print("Aucune date de naissance valide trouvée pour calculer la moyenne d'âge.")




# Écrire les informations des étudiants dans un fichier CSV
with open('students.csv', mode='a', newline='') as csv_file:
    fieldnames = ["Matriculation Number", "Name", "First Name", "Study Program", "Serie", "Date of Birth", "institution email"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Écrit l'en-tête uniquement si le fichier est vide
    if csv_file.tell() == 0:
        writer.writeheader()

    for student in students:
        writer.writerow(student.info)

# Lire les informations des étudiants depuis le fichier CSV
students_from_csv = []

with open('students.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        student = Student()
        student.info = row
        students_from_csv.append(student)

# Afficher les étudiants lus à partir du fichier CSV
for student in students_from_csv:
    print("Matriculation Number:", student.info["Matriculation Number"])
    print("Name:", student.info["Name"])
    print("First Name:", student.info["First Name"])
    print("Study Program:", student.info["Study Program"])
    print("Serie:", student.info["Serie"])
    print("Date of Birth:", student.info["Date of Birth"])
    print("institution email:", student.info["institution email"])
    print("-" * 20)


# print()

afficher_moyenne_age_etudiants_depuis_csv()