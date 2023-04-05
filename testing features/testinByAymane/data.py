import tkinter as tk
from tkinter import filedialog
import mysql.connector

# Se connecter à la base de données MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MG1234",
  database="gestion_etudiant"
)

# Fonction pour ajouter un utilisateur à la base de données
def ajouter_utilisateur(nom, prenom, age, image):
    mycursor = mydb.cursor()
    sql = "INSERT INTO exemple (nom, prenom, age, image) VALUES (%s, %s, %s, %s)"
    val = (nom, prenom, age, image)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "utilisateur inséré.")

# Fonction appelée lorsque le bouton "Ajouter" est cliqué
def ajouter_clic():
    nom = nom_entree.get()
    prenom = prenom_entree.get()
    age = age_entree.get()
    image = image_entree.get()

    with open(image, 'rb') as f:
        image_data = f.read()

    ajouter_utilisateur(nom, prenom, age, image_data)

# Fonction appelée lorsque le bouton "Parcourir" est cliqué
def parcourir_clic():
    filename = filedialog.askopenfilename()
    image_entree.delete(0, tk.END)
    image_entree.insert(0, filename)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Ajouter un utilisateur")

# Ajouter des étiquettes et des zones de texte pour saisir les informations de l'utilisateur
nom_label = tk.Label(fenetre, text="Nom :")
nom_label.grid(row=0, column=0)
nom_entree = tk.Entry(fenetre)
nom_entree.grid(row=0, column=1)

prenom_label = tk.Label(fenetre, text="Prénom :")
prenom_label.grid(row=1, column=0)
prenom_entree = tk.Entry(fenetre)
prenom_entree.grid(row=1, column=1)

age_label = tk.Label(fenetre, text="Âge :")
age_label.grid(row=2, column=0)
age_entree = tk.Entry(fenetre)
age_entree.grid(row=2, column=1)

image_label = tk.Label(fenetre, text="Image :")
image_label.grid(row=3, column=0)
image_entree = tk.Entry(fenetre)
image_entree.grid(row=3, column=1)

# Ajouter un bouton pour parcourir les fichiers de l'utilisateur
parcourir_bouton = tk.Button(fenetre, text="Parcourir", command=parcourir_clic)
parcourir_bouton.grid(row=3, column=2)

# Ajouter un bouton pour ajouter l'utilisateur à la base de données
ajouter_bouton = tk.Button(fenetre, text="Ajouter", command=ajouter_clic)
ajouter_bouton.grid(row=4, column=1)

# Lancer la boucle principale de l'interface graphique
fenetre.mainloop()
