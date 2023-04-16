import mysql.connector
import tkinter as tk

# Connexion à la base de données MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MG1234",
    database="gestion_etudiant"
)

# Fonction appelée lorsque le bouton "Mettre à jour" est cliqué
def update_database():
    # Récupération des valeurs des champs de l'interface utilisateur
    champ = champ_var.get()
    valeur = valeur_entry.get()
    id_enregistrement = id_entry.get()

    # Exécution de la requête SQL pour mettre à jour la valeur du champ sélectionné
    mycursor = mydb.cursor()
    sql = "UPDATE etudiant SET {} = %s WHERE id = %s".format(champ)
    val = (valeur, id_enregistrement)
    mycursor.execute(sql, val)
    mydb.commit()

    # Affichage d'un message de confirmation
    message_label.config(text="Champ {} mis à jour avec la valeur {} pour l'enregistrement d'ID {}".format(champ, valeur, id_enregistrement))

# Création de l'interface utilisateur
root = tk.Tk()
root.title("Mise à jour de la base de données")

# Création du label "Champ" et de la barre d'options
champ_label = tk.Label(root, text="Champ :")
champ_label.grid(row=0, column=0)
champ_var = tk.StringVar()
champ_menu = tk.OptionMenu(root, champ_var, "Nom", "Prenom", "Filier")
champ_menu.grid(row=0, column=1)

# Champ pour entrer l'ID de l'enregistrement à mettre à jour
id_label = tk.Label(root, text="ID de l'enregistrement :")
id_label.grid(row=1, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1)

# Champ pour entrer la nouvelle valeur du champ
valeur_label = tk.Label(root, text="Nouvelle valeur :")
valeur_label.grid(row=2, column=0)
valeur_entry = tk.Entry(root)
valeur_entry.grid(row=2, column=1)

# Bouton pour mettre à jour la base de données
update_button = tk.Button(root, text="Mettre à jour", command=update_database)
update_button.grid(row=3, column=0, columnspan=2)

# Label pour afficher le message de confirmation
message_label = tk.Label(root, text="")
message_label.grid(row=4, column=0, columnspan=2)

# Lancement de l'interface utilisateur
root.mainloop()