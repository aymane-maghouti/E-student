# import mysql.connector
#
# # Se connecter à la base de données
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="MG1234",
#   database="gestion_etudiant"
# )
#
# # Créer un curseur pour exécuter des requêtes SQL
# mycursor = mydb.cursor()
#
# # Définir les valeurs à insérer
# description = " notification 2 pour ID"
# detail = "Ceci est la notification  2 de test pour ID"
# filiere = "ID"
#
# # Créer la requête SQL
#
# sql = "INSERT INTO notification (description, detail, filier) VALUES (%s, %s, %s)"
# val = (description, detail, filiere)
#
# # Exécuter la requête SQL
# mycursor.execute(sql, val)
#
# # Valider les changements dans la base de données
# mydb.commit()
#
# print(mycursor.rowcount, "enregistrement inséré avec succès.")


# ################# inserer les donnees via l'interface tkinter ################################
# import mysql.connector
# from tkinter import *
#
# # Se connecter à la base de données
# mydb = mysql.connector.connect(
# host="localhost",
#   user="root",
#   password="MG1234",
#   database="gestion_etudiant"
# )
#
# # Créer une fonction pour insérer les données
# def inserer_donnees():
#     # Créer un curseur pour exécuter des requêtes SQL
#     mycursor = mydb.cursor()
#
#     # Récupérer les valeurs entrées par l'utilisateur
#     description = desc_entry.get()
#     detail = detail_entry.get()
#     filiere = filiere_entry.get()
#
#     # Créer la requête SQL
#     sql = "INSERT INTO notification (description, detail, filier) VALUES (%s, %s, %s)"
#     val = (description, detail, filiere)
#
#     # Exécuter la requête SQL
#     mycursor.execute(sql, val)
#
#     # Valider les changements dans la base de données
#     mydb.commit()
#
#     print(mycursor.rowcount, "enregistrement inséré avec succès.")
#
# # Créer une fenêtre
# root = Tk()
# root.title("Insertion de données")
#
# # Créer les champs de saisie
# desc_label = Label(root, text="Description")
# desc_label.grid(row=0, column=0)
# desc_entry = Entry(root)
# desc_entry.grid(row=0, column=1)
#
# detail_label = Label(root, text="Détail")
# detail_label.grid(row=1, column=0)
# detail_entry = Entry(root)
# detail_entry.grid(row=1, column=1)
#
# filiere_label = Label(root, text="Filière")
# filiere_label.grid(row=2, column=0)
# filiere_entry = Entry(root)
# filiere_entry.grid(row=2, column=1)
#
# # Créer un bouton pour insérer les données
# insert_button = Button(root, text="Insérer les données", command=inserer_donnees)
# insert_button.grid(row=3, column=0, columnspan=2)
#
# # Afficher la fenêtre
# root.mainloop()


from tkinter import *

import mysql.connector

# Se connecter à la base de données
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MG1234",
    database="gestion_etudiant"
)


# Créer une fonction pour insérer les données
def inserer_donnees():
    # Créer un curseur pour exécuter des requêtes SQL
    mycursor = mydb.cursor()

    # Récupérer les valeurs entrées par l'utilisateur
    description = desc_entry.get()
    detail = detail_entry.get("1.0", END)  # Récupérer tout le texte du champ de texte
    filiere = filiere_entry.get()

    # Créer la requête SQL
    sql = "INSERT INTO notification (description, detail, filier) VALUES (%s, %s, %s)"
    val = (description, detail, filiere)

    # Exécuter la requête SQL
    mycursor.execute(sql, val)

    # Valider les changements dans la base de données
    mydb.commit()

    print(mycursor.rowcount, "enregistrement inséré avec succès.")


# Créer une fenêtre
root = Tk()
root.title("Insertion de données")

# Créer les champs de saisie
desc_label = Label(root, text="Description")
desc_label.grid(row=0, column=0)
desc_entry = Entry(root)
desc_entry.grid(row=0, column=1)

detail_label = Label(root, text="Détail")
detail_label.grid(row=1, column=0)
detail_entry = Text(root, height=5)
detail_entry.grid(row=1, column=1)

filiere_label = Label(root, text="Filière")
filiere_label.grid(row=2, column=0)
filiere_entry = Entry(root)
filiere_entry.grid(row=2, column=1)

# Créer un bouton pour insérer les données
insert_button = Button(root, text="Insérer les données", command=inserer_donnees)
insert_button.grid(row=3, column=0, columnspan=2)

# Afficher la fenêtre
root.mainloop()
