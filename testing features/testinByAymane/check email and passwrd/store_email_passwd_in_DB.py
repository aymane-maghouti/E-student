import re
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import hashlib

# Connexion à la base de données MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MG1234",
    database="gestion_etudiant"
)

# Fonction de vérification de l'adresse e-mail
def check_email(email):
    pattern = r"^[a-zA-Z0-9]+\.([a-zA-Z0-9]+)+@+etu.uae.ac.ma$"
    return re.match(pattern, email)

# Fonction de vérification du mot de passe
def check_password(password, confirm_password):
    # Vérification de la longueur
    if len(password) < 8:
        return False
    # Vérification de la présence d'une lettre majuscule
    if not re.search("[A-Z]", password):
        return False
    # Vérification de la présence d'une lettre minuscule
    if not re.search("[a-z]", password):
        return False
    # Vérification de la présence d'un chiffre
    if not re.search("[0-9]", password):
        return False
    # Vérification de la correspondance des mots de passe
    if password != confirm_password:
        return False
    return True

# Fonction de hachage du mot de passe
def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

# Fonction de stockage des données dans la base de données
def store_data(email, password):
    hashed_password = hash_password(password)
    mycursor = mydb.cursor()
    sql = "INSERT INTO login (email, passwrd) VALUES (%s, %s)"
    val = (email, hashed_password)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Succès", "Les données ont été stockées avec succès dans la base de données.")
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

# Fonction de gestion du formulaire
def submit_form():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    if not check_email(email):
        messagebox.showerror("Erreur", "L'adresse e-mail saisie est invalide. Veuillez saisir une adresse e-mail valide.")
    elif not check_password(password, confirm_password):
        messagebox.showerror("Erreur", "Le mot de passe ne respecte pas les normes de sécurité. Veuillez entrer un mot de passe qui respecte les normes.")
    else:
        store_data(email, password)

# Interface graphique
root = tk.Tk()
root.title(" store the email adresse and the password")

email_label = tk.Label(root, text="Adresse e-mail :")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Mot de passe :")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

confirm_password_label = tk.Label(root, text="Confirmez le mot de passe :")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack()

submit_button = tk.Button(root, text="Valider", command=submit_form)
submit_button.pack()

root.geometry("400x500")

root.mainloop()
