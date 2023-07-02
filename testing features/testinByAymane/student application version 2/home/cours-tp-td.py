import os
from tkinter import *
from tkinter import filedialog

from conneToDB import connectDB

# Se connecter à la base de données MySQL
mydb, mycursor = connectDB("student_managment")


def documents(class_name):
    mycursor.execute("SELECT type,titre,file,date_doc FROM documents where class = %s order by date_doc desc ",
                     (class_name,))
    result = mycursor.fetchall()

    def get_pdf_from_database(index):
        conn, cursor = connectDB("student_managment")
        query = "SELECT file FROM documents WHERE class = 'id1' order by date_doc desc"
        cursor.execute(query)
        rows = cursor.fetchall()

        if index >= len(rows):
            return None

        pdf_content = rows[index][0]
        return pdf_content

    def download_pdf(pdf_content):
        # Demander à l'utilisateur de choisir le dossier de destination
        destination_folder = filedialog.askdirectory()

        # Si aucun dossier n'est sélectionné, ne rien faire
        if not destination_folder:
            return

        # Créer un nom de fichier aléatoire avec l'extension .pdf
        import random as rd
        n = rd.randrange(1000000000000000000, 999999999999999999999)
        filename = f"{n}.pdf"

        # Construire le chemin complet du fichier de destination
        destination_file = os.path.join(destination_folder, filename)

        # Écrire le contenu du fichier PDF dans le fichier de destination
        with open(destination_file, "wb") as f:
            f.write(pdf_content)

        # Ouvrir le dossier de destination
        os.startfile(destination_folder)

    def download_button_click(index):
        pdf_content = get_pdf_from_database(index)
        if pdf_content is not None:
            download_pdf(pdf_content)

    # Créer une fenêtre
    root = Tk()
    root.geometry('600x100')
    root.title("COURS/TD/TP")

    # Créer un canevas pour contenir le tableau
    canvas = Canvas(root)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Créer une barre de défilement pour le canevas
    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Connecter la barre de défilement au canevas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Ajouter un cadre pour contenir les étiquettes
    table = Frame(canvas)
    canvas.create_window((0, 0), window=table, anchor=NW)

    # Ajouter les étiquettes au cadre
    Label(table, text="Type", width=10, height=2).grid(row=0, column=0)
    Label(table, text="Titre", width=25, height=2).grid(row=0, column=1)
    Label(table, text="file", width=10, height=2).grid(row=0, column=2)
    Label(table, text="date de publication", width=15, height=2).grid(row=0, column=3)

    for i, row in enumerate(result):
        Label(table, text=row[0], width=10, height=2).grid(row=i + 1, column=0)
        Label(table, text=row[1], width=25, height=2).grid(row=i + 1, column=1)
        Button(table, text="telecharger", command=lambda index=i: download_button_click(index), width=15,
               height=2).grid(row=i + 1, column=2)
        Label(table, text=row[3], width=15, height=2).grid(row=i + 1, column=3)

    # Redimensionner le canevas en fonction de son contenu
    table.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Afficher la fenêtre
    root.mainloop()


documents('gi1')
