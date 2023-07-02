import tkinter as tk

import mysql.connector


# Fonction appelée lorsque l'utilisateur clique sur le bouton "Supprimer"
def delete_student():
    # Récupération de l'identifiant de l'étudiant à supprimer
    student_id = id_entry.get()

    # Connexion à la base de données
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MG1234",
        database="gestion_etudiant"
    )

    # Création d'un objet "cursor" pour exécuter des commandes SQL
    mycursor = mydb.cursor()

    # Suppression de l'étudiant
    sql = "DELETE FROM students WHERE nom = %s"
    val = (student_id,)
    mycursor.execute(sql, val)

    # Validation de la transaction
    mydb.commit()

    # Affichage du nombre d'enregistrements supprimés
    result_label.configure(text=mycursor.rowcount + " enregistrement(s) supprimé(s)")


# Création de la fenêtre principale
window = tk.Tk()
window.title("Supprimer un étudiant")

# Création du champ de saisie pour l'identifiant de l'étudiant
id_label = tk.Label(window, text=" full name  : ")
id_label.grid(column=0, row=0)
id_entry = tk.Entry(window)
id_entry.grid(column=1, row=0)

# Création du bouton "Supprimer"
delete_button = tk.Button(window, text="Supprimer", command=delete_student)
delete_button.grid(column=0, row=1)

# Création du champ de texte pour afficher le résultat
result_label = tk.Label(window, text="")
result_label.grid(column=0, row=2)

# Lancement de la boucle principale de l'interface graphique
window.mainloop()
