
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

# Créer une nouvelle fenêtre pour afficher les données
record_window = Toplevel(root)

# Créer les frames gauche et droite pour l'affichage des données
left_frame = Frame(record_window)
left_frame.pack(side=LEFT, padx=10, pady=10)

right_frame = Frame(record_window)
right_frame.pack(side=RIGHT, padx=10, pady=10)

# Ajouter des widgets à la frame gauche
id_label = Label(root, text="ID:")
id_entry = Entry(root)
id_label.pack()
id_entry.pack()

full_name_label = Label(left_frame, text="Full Name:")
full_name_label.pack()
full_name_display = Label(left_frame)
full_name_display.pack()

age_label = Label(left_frame, text="Age:")
age_label.pack()
age_display = Label(left_frame)
age_display.pack()

filier_label = Label(left_frame, text="Filier:")
filier_label.pack()
filier_display = Label(left_frame)
filier_display.pack()

# Ajouter des widgets à la frame droite pour l'affichage de l'image
image_label = Label(right_frame)
image_label.pack()

def show_data():
    # Récupérer l'ID entré par l'utilisateur
    id = id_entry.get()

    # Créer un curseur pour exécuter des requêtes SQL
    mycursor = mydb.cursor()

    # Exécuter une requête SQL pour récupérer les données de l'enregistrement
    mycursor.execute("SELECT * FROM students WHERE id = %s", (id,))

    # Récupérer les données de l'enregistrement
    record = mycursor.fetchone()

    # Afficher les données autres que l'image
    full_name_display.config(text=record[1])
    age_display.config(text=str(record[2]))
    filier_display.config(text=record[3])

    # Afficher l'image
    image = Image.open(io.BytesIO(record[4]))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

    # Afficher la fenêtre contenant les données
    record_window.deiconify()

# Ajouter un bouton pour afficher les données
show_button = Button(root, text="Show Data", command=show_data)
show_button.pack()

# Masquer la fenêtre record_window au lancement du programme
record_window.withdraw()

# Afficher la fenêtre Tkinter
root.mainloop()
