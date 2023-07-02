from tkinter import *

from conneToDB import connectDB


def show_prof(filier_name):
    mydb, mycursor = connectDB("student_managment")
    mycursor.execute(
        "select firstname , lastname , email_prof from prof p , filier f , departement d where f.id_departement = d.id_departement  and p.id_departement = d.id_departement and f.name = %s ",
        (filier_name,))
    result = mycursor.fetchall()
    # Créer une fenêtre et un canvas avec une barre de défilement verticale
    root = Tk()
    root.geometry('600x100')
    root.title("Emploi du temps")

    canvas = Canvas(root)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Créer un cadre pour le tableau
    table = Frame(canvas)
    canvas.create_window((0, 0), window=table, anchor="nw")

    # Afficher les données dans un tableau tkinter
    Label(table, text="first name", width=10, height=2).grid(row=0, column=0)
    Label(table, text="last name", width=25, height=2).grid(row=0, column=1)
    Label(table, text="email ", width=30, height=2).grid(row=0, column=2)
    for i, row in enumerate(result):
        Label(table, text=row[0], width=10, height=2).grid(row=i + 1, column=0)
        Label(table, text=row[1], width=25, height=2).grid(row=i + 1, column=1)
        Label(table, text=row[2], width=30, height=2).grid(row=i + 1, column=2)

    root.mainloop()


show_prof('ID')
