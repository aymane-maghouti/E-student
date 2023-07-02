import tkinter as tk
from io import BytesIO
from tkinter import filedialog

import mysql.connector
from PIL import Image, ImageTk

# Connecter à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MG1234",
    database="gestion_etudiant"
)
cursor = conn.cursor()

# Créer la table "personnes" si elle n'existe pas
cursor.execute("CREATE TABLE IF NOT EXISTS personnes (nom VARCHAR(255), prenom VARCHAR(255), age INT, image LONGBLOB)")


def ajouter_personne():
    nom = nom_entree.get()
    prenom = prenom_entree.get()
    age = age_entree.get()

    # Ouvrir une boîte de dialogue pour permettre à l'utilisateur de sélectionner une image
    image_path = filedialog.askopenfilename()

    # Lire les données de l'image et les stocker sous forme de bytes
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    # Insérer les données dans la base de données
    cursor.execute("INSERT INTO personnes (nom, prenom, age, image) VALUES (%s, %s, %s, %s)",
                   (nom, prenom, age, image_bytes))
    conn.commit()


def afficher_personnes():
    # Récupérer les données de la base de données

    query = "SELECT * FROM personnes where nom = 'tati'"
    cursor.execute(query)

    # Récupérer toutes les données
    personnes = cursor.fetchall()
    # print(data)
    # print(personnes)
    # Récupérer les données de l'image
    image_data = personnes[0][3]

    # Ouvrir les données de l'image comme un flux d'octets
    img_stream = BytesIO(image_data)

    # Ouvrir l'image avec Pillow
    image = Image.open(img_stream)

    # Enregistrer l'image dans un fichier
    image.save("C:/Users/pc/PycharmProjects/pythonProject/projet_web/mon_image.png")

    frame2.tkraise()
    for personne in personnes:
        nom_label = tk.Label(frame2, text="Nom : " + personne[0])
        nom_label.pack()

        prenom_label = tk.Label(frame2, text="Prénom : " + personne[1])
        prenom_label.pack()

        age_label = tk.Label(frame2, text="Âge : " + str(personne[2]))
        age_label.pack()

        # resized_image = photo2.resize((300, 150), Image.ANTIALIAS)
        converted_image = ImageTk.PhotoImage(Image.open("logo-ensah.png"))

        label = tk.Label(frame2, image=converted_image, width=300, height=150)
        label.pack()


def show_frame1():
    frame1.tkraise()


def show_frame2():
    frame2.tkraise()


fenetre = tk.Tk()

frame1 = tk.Frame(fenetre, bg='red', width=600, height=400)
frame2 = tk.Frame(fenetre, bg='green', width=600, height=400)
frame3 = tk.Frame(fenetre, bg='blue', width=600, height=400)
# frame = Frame(win, width=600, height=400)
# frame.pack()
frame3.pack()
frame3.place(anchor='center', relx=0.5, rely=0.5)
frame1.place(x=0, y=0, relwidth=1, relheight=1)
frame2.place(x=0, y=0, relwidth=1, relheight=1)
# frame3.place(x=0, y=0, relwidth=1, relheight=1)


afficher_pag1 = tk.Button(fenetre, text="-->page1", command=show_frame1)
afficher_pag1.pack()

afficher_pag2 = tk.Button(frame1, text="-->page2", command=show_frame2)
afficher_pag2.pack()

afficher_pag2 = tk.Button(frame2, text="afficher data", command=afficher_personnes)
afficher_pag2.pack()

nom_label = tk.Label(frame1, text="Nom : ")
nom_label.pack()
nom_entree = tk.Entry(frame1)
nom_entree.pack()

prenom_label = tk.Label(frame1, text="Prénom : ")
prenom_label.pack()
prenom_entree = tk.Entry(frame1)
prenom_entree.pack()

age_label = tk.Label(frame1, text="Âge : ")
age_label.pack()
age_entree = tk.Entry(frame1)
age_entree.pack()

# Ajouter un bouton pour permettre à l'utilisateur de sélectionner une image
image_label = tk.Label(frame1, text="Image : ")
image_label.pack()
image_bouton = tk.Button(frame1, text="Sélectionner une image", command=ajouter_personne)
image_bouton.pack()

# Ajouter un bouton pour afficher les données de la base de données
# afficher_bouton = tk.Button(frame2, text="Afficher personnes", command=afficher_personnes)
# afficher_bouton.pack()

afficher_pag3 = tk.Button(frame2, text="-->page3", command=show_frame1)
afficher_pag3.pack()

# retour_button = tk.Button(frame2,text="retour",command=show_frame2)
# retour_button.pack()
fenetre.geometry("500x500")
# L
fenetre.mainloop()

conn.close()
