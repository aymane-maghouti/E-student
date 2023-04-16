

import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
import io

# Créer une connexion à la base de données MySQL
mydb = mysql.connector.connect(
    user='root', password='MG1234',
    host='localhost', database='gestion_etudiant'
)

# Créer une instance de la fenêtre Tkinter
root = Tk()


# Ajouter des widgets à la fenêtre
id_label = Label(root, text="ID:")
id_entry = Entry(root)
id_label.pack()
id_entry.pack()

def show_data():
    # Récupérer l'ID entré par l'utilisateur
    id = id_entry.get()

    # Créer un curseur pour exécuter des requêtes SQL
    mycursor = mydb.cursor()

    # Exécuter une requête SQL pour récupérer les données de l'enregistrement
    mycursor.execute("SELECT * FROM students WHERE id = %s", (id,))

    # Récupérer les données de l'enregistrement
    record = mycursor.fetchone()

    # Créer une fenêtre pour afficher les données
    record_window = Toplevel()
    full_name_label = Label(record_window, text="Full Name: " + record[1])
    age_label = Label(record_window, text="Age: " + str(record[2]))
    filier_label = Label(record_window, text="Filier: " + record[3])
    full_name_label.pack()
    age_label.pack()
    filier_label.pack()

    # Afficher l'image
    image = Image.open(io.BytesIO(record[4]))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(record_window, image=photo)
    image_label.image = photo
    image_label.pack()

# Ajouter un bouton pour afficher les données
show_button = Button(root, text="Show Data", command=show_data)
show_button.pack()

# Afficher la fenêtre Tkinter
root.mainloop()



