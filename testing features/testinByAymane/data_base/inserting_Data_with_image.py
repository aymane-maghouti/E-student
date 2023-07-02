from tkinter import Tk, Label, Entry, Button
from tkinter.filedialog import askopenfilename

import mysql.connector


# Fonction pour insérer les données et l'image dans la base de données
def insert_student_data():
    # Connexion à la base de données MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MG1234",
        database="gestion_etudiant"
    )
    mycursor = mydb.cursor()

    # Création de la table 'students' si elle n'existe pas déjà
    mycursor.execute("CREATE TABLE if not exists students (name VARCHAR(255), age INT,Filier Varchar(25), image BLOB)")

    # Ouverture et lecture du fichier image
    with open(filename, "rb") as image_file:
        binary_data = image_file.read()

    # Insertion des données et de l'image dans la base de données
    name = name_entry.get()
    age = age_entry.get()
    filier = filier_entry.get()
    sql = "INSERT INTO students (Full_name, age, Filier, image) VALUES (%s, %s, %s, %s)"
    val = (name, age, filier, binary_data)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


# Fonction pour sélectionner le fichier image à partir de la machine de l'utilisateur
def select_image_file():
    global filename
    Tk().withdraw()
    filename = askopenfilename()


# Création de la fenêtre Tkinter
root = Tk()
root.title("Insertion de données étudiant")

# Création des étiquettes et des champs de saisie pour les données de l'étudiant
name_label = Label(root, text="Nom de l'étudiant:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

age_label = Label(root, text="Âge de l'étudiant:")
age_label.pack()
age_entry = Entry(root)
age_entry.pack()

filier_label = Label(root, text="Filière de l'étudiant:")
filier_label.pack()
filier_entry = Entry(root)
filier_entry.pack()

# Bouton pour sélectionner le fichier image
select_image_button = Button(root, text="Sélectionner une image", command=select_image_file)
select_image_button.pack()

# Bouton pour insérer les données et l'image dans la base de données
insert_button = Button(root, text="Insérer les données", command=insert_student_data)
insert_button.pack()

root.mainloop()
