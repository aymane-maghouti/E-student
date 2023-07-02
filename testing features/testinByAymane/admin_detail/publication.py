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
    file_type = type_var.get()
    file_title = file_title_entry.get()
    file_path = file_path_entry.get()
    execution_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        # Connexion à la base de données MySQL
        cnx = mysql.connector.connect(user='root', password='MG1234',
                                      host='localhost', database='gestion_etudiant')
        cursor = cnx.cursor()

        # Insertion des données dans la table "files"
        insert_query = ("INSERT INTO publication(type, titre, file, date_pub) VALUES (%s, %s, %s, %s)")
        with open(file_path, 'rb') as f:
            pdf_file = f.read()
        insert_values = (file_type, file_title, pdf_file, execution_date)
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
root.title("Enregistrer un fichier")

# Création des widgets
file_type_label = tk.Label(root, text="Type de fichier :")
file_type_label.grid(row=0, column=0, padx=10, pady=10)
type_var = tk.StringVar()
type_var.set("TD")
file_type_td_button = tk.Radiobutton(root, text="TD", variable=type_var, value="TD")
file_type_td_button.grid(row=0, column=1)
file_type_cours_button = tk.Radiobutton(root, text="COURS", variable=type_var, value="COURS")
file_type_cours_button.grid(row=0, column=2)
file_type_exam_button = tk.Radiobutton(root, text="PLANNING EXAM", variable=type_var, value="PLANNING EXAM")
file_type_exam_button.grid(row=0, column=3)
file_type_tp_button = tk.Radiobutton(root, text="TP", variable=type_var, value="TP")
file_type_tp_button.grid(row=1, column=1)
file_type_avis_button = tk.Radiobutton(root, text="AVIS", variable=type_var, value="AVIS")
file_type_avis_button.grid(row=1, column=2)
file_title_label = tk.Label(root, text="Titre du fichier :")
file_title_label.grid(row=2, column=0, padx=10, pady=10)
file_title_entry = tk.Entry(root)
file_title_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

file_path_label = tk.Label(root, text="Chemin du fichier :")
file_path_label.grid(row=3, column=0, padx=10, pady=10)
file_path_entry = tk.Entry(root)
file_path_entry.grid(row=3, column=1, padx=10, pady=10)
file_path_button = tk.Button(root, text="Sélectionner un fichier", command=select_file)
file_path_button.grid(row=3, column=2, padx=10, pady=10)

save_button = tk.Button(root, text="Enregistrer", command=save_file)
save_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

root.mainloop()
