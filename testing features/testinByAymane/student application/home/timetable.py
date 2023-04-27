from tkinter import *
from tkinter import filedialog
import os
from conneToDB import connectDB

# Se connecter à la base de données MySQL
mydb  ,mycursor = connectDB("student_managment")
mycursor.execute("SELECT class,timetable,date_pub FROM emploi_temps order by date_pub desc ")
result = mycursor.fetchall()



def get_pdf_from_database(index):

    conn , cursor = connectDB("student_managment")
    query = "SELECT timetable FROM emploi_temps order by date_pub desc"
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



# Créer une fenêtre et un canvas avec une barre de défilement verticale
root = Tk()
root.geometry('400x100')
root.title("Emploi du temps")

canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Créer un cadre pour le tableau
table = Frame(canvas)
canvas.create_window((0,0), window=table, anchor="nw")

# Afficher les données dans un tableau tkinter
Label(table,text="Class" , width=10,height=2).grid(row=0,column=0)
Label(table,text="emploi du temps" , width=15,height=2).grid(row=0,column=1)
Label(table,text="date de publication" , width=15,height=2).grid(row=0,column=2)
for i, row in enumerate(result):
    Label(table, text=row[0],width=10,height=2).grid(row=i+1, column=0)
    Button(table, text="telecharger", command=lambda index=i: download_button_click(index), width=15, height=2).grid(row=i+1, column=1)
    Label(table, text=row[2],width=15,height=2).grid(row=i+1, column=2)

root.mainloop()
