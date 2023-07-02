import tkinter as tk
from datetime import datetime
from tkinter import filedialog

import mysql.connector
from mysql.connector import errorcode


# Fonction appelée lorsque l'utilisateur clique sur le bouton "Sélectionner un fichier"
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)


# Fonction appelée lorsque l'utilisateur clique sur le bouton "Enregistrer"
def save_file():
    file_class = file_class_entry.get()
    file_path = file_path_entry.get()

    execution_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        # Connexion à la base de données MySQL
        cnx = mysql.connector.connect(user='root', password='MG1234',
                                      host='localhost', database='gestion_etudiant')
        cursor = cnx.cursor()

        # Insertion des données dans la table "files"
        insert_query = ("INSERT INTO emploi_temps(class, timetable, date_pub) VALUES (%s,%s, %s)")
        with open(file_path, 'rb') as f:
            pdf_file = f.read()
        insert_values = (file_class, pdf_file, execution_date)
        cursor.execute(insert_query, insert_values)
        cnx.commit()

        cursor.close()
        cnx.close()

        # Message de confirmation
        tk.messagebox.showinfo("Enregistrement", "Le fichier a été enregistré avec succès !")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            tk.messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            tk.messagebox.showerror("Erreur", "Nom de base de données incorrect.")
        else:
            tk.messagebox.showerror("Erreur", "Erreur lors de la connexion à la base de données.")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Emploi du temps")

file_class_label = tk.Label(root, text="Class : ")
file_class_label.grid(row=0, column=0, padx=10, pady=10)
file_class_entry = tk.Entry(root)
file_class_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

file_path_label = tk.Label(root, text="Emploi du temps :")
file_path_label.grid(row=2, column=0, padx=10, pady=10)
file_path_entry = tk.Entry(root)
file_path_button = tk.Button(root, text="Sélectionner un fichier", command=select_file)
file_path_button.grid(row=2, column=2, padx=10, pady=10)

save_button = tk.Button(root, text="Enregistrer", command=save_file)
save_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

root.mainloop()
