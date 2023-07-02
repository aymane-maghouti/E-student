# import mysql.connector
import io
import tkinter as tk
from tkinter import *

from PIL import Image, ImageTk

# Créer une connexion à la base de données MySQL
# mydb = mysql.connector.connect(
# user='root', password='MG1234',
# host='localhost', database='gestion_etudiant'
# )

# Créer une instance de la fenêtre Tkinter
root = Tk()
root.geometry("300x300")

record_window = Toplevel(root)
record_window.geometry("400x300")

right_frame = Frame(record_window, width=200, height=20)
right_frame.pack(side=LEFT)

canvas = tk.Canvas(right_frame, borderwidth=0, highlightthickness=0, width=200, height=20)
scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="right", fill="both", expand=False)
scrollbar.pack(side="right", fill="y")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")


def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


scrollable_frame.bind("<Configure>", update_scrollregion)

# Ajouter des widgets à la frame gauche
# id_label = Label(root, text="ID:")
# id_label.grid(row=0, column=0, padx=5, pady=5)
# id_entry = Entry(root)
# id_entry.grid(row=1, column=1, padx=5, pady=5)
#
full_name_label = Label(scrollable_frame, text="Full Name :", width=1000)
full_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
full_name_display = Label(scrollable_frame, text="")
full_name_display.grid(row=1, column=1, padx=5, pady=5, sticky=W)

age_label = Label(scrollable_frame, text="Age :")
age_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
age_display = Label(scrollable_frame, text="")
age_display.grid(row=2, column=1, padx=5, pady=5, sticky=W)

filier_label = Label(scrollable_frame, text="Filière :")
filier_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
filier_display = Label(scrollable_frame, text="")
filier_display.grid(row=3, column=1, padx=5, pady=5, sticky=W)

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
    width, height = photo.width(), photo.height()
    width, height = 200, (height * 200) // width  # Set the desired width and height
    image = image.resize((width, height))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

    # Afficher la fenêtre contenant les données
    record_window.deiconify()


# Ajouter des widgets à la frame gauche
show_button = Button(root, text="Show Data", command=show_data)
show_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Masquer la fenêtre record_window au lancement du programme
record_window.withdraw()

# Afficher la fen
root.mainloop()
