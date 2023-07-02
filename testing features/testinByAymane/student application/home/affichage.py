import os
import random as rd
import tempfile
import tkinter.filedialog as filedialog
from tkinter import *

from conneToDB import connectDB

# Se connecter à la base de données MySQL

mydb, mycursor = connectDB("student_managment")
mycursor.execute("SELECT class,module,notetable,date_pub FROM affichage order by date_pub desc ")
result = mycursor.fetchall()


def get_pdf_from_database(index):
    conn, cursor = connectDB('student_managment')

    query = "SELECT notetable FROM affichage order by date_pub desc "
    cursor.execute(query)
    rows = cursor.fetchall()

    if index >= len(rows):
        return None

    pdf_content = rows[index][0]
    return pdf_content


def download_pdf(pdf_content):
    # Demander à l'utilisateur de choisir le dossier où il souhaite stocker le fichier PDF
    folder_path = filedialog.askdirectory()

    if folder_path:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(pdf_content)
        temp_file.close()

        # Obtenez le nom de fichier aléatoire
        n = rd.randrange(1000000000000000000, 999999999999999999999)
        name_file = f"{n}.pdf"

        # Créez le fichier de destination dans le dossier choisi par l'utilisateur
        destination_file = os.path.join(folder_path, name_file)

        # Copiez le contenu du fichier temporaire vers le fichier de destination
        with open(destination_file, "wb") as f:
            f.write(pdf_content)

        # Ouvrez le dossier dans l'explorateur de fichiers
        os.startfile(folder_path)


def download_button_click(index):
    pdf_content = get_pdf_from_database(index)
    if pdf_content is not None:
        download_pdf(pdf_content)


# Afficher les données dans un tableau tkinter
root = Tk()
root.geometry('800x200')
root.title("Affichage")

# Create a canvas and add it to the root window
canvas = Canvas(root, width=600, height=500)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Create a frame to hold the table
table_frame = Frame(canvas)
table_frame.pack(fill=BOTH, expand=1)

# Add the table frame to the canvas
canvas.create_window(0, 0, anchor=NW, window=table_frame)

# Add a scrollbar to the canvas
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Bind the canvas to the scrollbar
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all"), yscrollincrement=5))

# Add the table headers
Label(table_frame, text="Class", width=10, height=2).grid(row=0, column=0)
Label(table_frame, text="Module", width=25, height=2).grid(row=0, column=1)
Label(table_frame, text="Les notes", width=15, height=2).grid(row=0, column=2)
Label(table_frame, text="Date de publication", width=15, height=2).grid(row=0, column=3)

# Add the data to the table
for i, row in enumerate(result):
    Label(table_frame, text=row[0], width=10, height=2).grid(row=i + 1, column=0)
    Label(table_frame, text=row[1], width=25, height=2).grid(row=i + 1, column=1)
    Button(table_frame, text="Télécharger", command=lambda index=i: download_button_click(index), width=15,
           height=2).grid(row=i + 1, column=2)
    Label(table_frame, text=row[3], width=15, height=2).grid(row=i + 1, column=3)

root.mainloop()
