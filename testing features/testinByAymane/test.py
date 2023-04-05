import csv
from tkinter import  *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MG1234",
  database="gestion_etudiant"
)

cursor = mydb.cursor()


class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("")
        self.file_path = None

        # Création des 4 pages
        self.page1 = tk.Frame(self, bg="blue")
        self.page2 = tk.Frame(self, bg="red")
        self.page3 = tk.Frame(self, bg="green")
        self.page4 = tk.Frame(self, bg="purple")

        # Création des boutons "Next" et "Back"
        self.button_back = tk.Button(self,text='Back',font=('Bold',12),bg='#1877f2', fg='white',width=8, command=self.show_previous_page)
        self.button_next = tk.Button(self, text='Next',font=('Bold',12),bg='#1877f2', fg='white',width=8, command=self.show_next_page)




        # Ajout des widgets à la fenêtre
        self.page1.pack(fill="both", expand=True)
        self.page2.pack(fill="both", expand=True)
        self.page3.pack(fill="both", expand=True)
        self.page4.pack(fill="both", expand=True)
        self.button_back.pack(side="left", padx=5, pady=5)
        self.button_next.pack(side="right", padx=5, pady=5)



        # Initialisation de l'index de la page affichée
        self.current_page = 0
        self.show_current_page()


        #@page 1
        self.label_nom = tk.Label(self.page1, text="Nom:")
        self.label_prenom = tk.Label(self.page1, text="Prenom:")
        self.label_Pays = tk.Label(self.page1, text="Pays :")
        # Création des zones de texte pour les informations
        self.entry_nom = tk.Entry(self.page1)
        self.entry_prenom = tk.Entry(self.page1)

        self.entry_Pays = tk.Entry(self.page1)
        # Placement des labels et des zones de texte
        self.label_nom.grid(row=1, column=0, padx=5, pady=5)
        self.label_prenom.grid(row=2, column=0, padx=5, pady=5)
        self.entry_nom.grid(row=1, column=1, padx=5, pady=5)
        self.entry_prenom.grid(row=2, column=1, padx=5, pady=5)
        self.label_Pays.grid(row=6, column=0, padx=5, pady=5)
        self.image_label = tk.Label(self.page1, text="Image :")
        self.image_label.grid(row=7, column=1)
        self.image_entree = tk.Entry(self.page1)
        self.image_entree.grid(row=7, column=2)


        # lire le fichier CSV et stocker les villes dans une liste
        with open('countries.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            countries = [row[0] for row in reader]
        # créer une variable pour stocker la ville sélectionnée
        self.var = tk.StringVar()
        # par défaut, la ville sélectionnée est la première ville de la liste
        self.var.set(countries[0])
        # créer un menu déroulant avec les villes
        menu = tk.OptionMenu(self.page1, self.var, *countries)
        menu.grid(row=6, column=1, padx=5, pady=5)



        self.label_title1 = tk.Label(self.page1, text="IDENTIFICATION DE L'ETUDIANT", font=("Arial", 16))
        self.label_title2 = tk.Label(self.page2, text="NAISSANCE DE L'ETUDIANT", font=("Arial", 16))
        self.label_title3 = tk.Label(self.page3, text="COORDONNEES DE L'ETUDIANT", font=("Arial", 16))
        self.label_title4 = tk.Label(self.page4, text="BAC DE L'ETUDIANT", font=("Arial", 16))
        self.label_title1.grid(row=0, column=0, padx=5, pady=5)
        self.label_title2.grid(row=0, column=0, padx=5, pady=5)
        self.label_title3.grid(row=0, column=0, padx=5, pady=5)
        self.label_title4.grid(row=0, column=0, padx=5, pady=5)
        self.button_select_image = tk.Button(self.page1, text="Select Image", command=self.select_image)
        self.button_select_image.grid(row=7, column=0, padx=5, pady=5)


        #@page 2
        self.label_DN = tk.Label(self.page2, text="Date de Naissance :")

        # Création des zones de texte pour les informations
        self.entry_DN = tk.Entry(self.page2)

        # Placement des labels et des zones de texte
        self.label_DN.grid(row=1, column=0, padx=5, pady=5)

        self.entry_DN.grid(row=1, column=1, padx=5, pady=5)

        #@PAGE3
        self.label_TELE = tk.Label(self.page3, text="Tele :")
        # Création des zones de texte pour les informations
        self.entry_TELE = tk.Entry(self.page3)

        # Placement des labels et des zones de texte
        self.label_TELE.grid(row=1, column=0, padx=5, pady=5)
        self.entry_TELE.grid(row=1, column=1, padx=5, pady=5)



        # @page4
        self.label_AB = tk.Label(self.page4, text="Année d'obtention BAC  :")
        # Création des zones de texte pour les informations
        self.entry_AB = tk.Entry(self.page4)
        # Placement des labels et des zones de texte
        self.label_AB.grid(row=1, column=0, padx=5, pady=5)
        self.entry_AB.grid(row=1, column=1, padx=5, pady=5)


        self.button_submit = tk.Button(self.page4, text='submit',font=('Bold',12),bg='#1877f2', fg='white',width=8,command=self.save_data).grid(row=2, column=1, padx=5, pady=5)

    def save_data(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        pays= self.var.get()
        date_naissance = self.entry_DN.get()
        tele = self.entry_TELE.get()
        annee_bac=self.entry_AB.get()
        image = self.image_entree.get()

        with open(image, 'rb') as f:
            image_data = f.read()

        self.add_user(nom,prenom,pays,date_naissance,tele,annee_bac,image_data)
        # print("done")
    def add_user(self,nom, prenom, pays,date_naissance,tele,annee_bac,image):
        mycursor = mydb.cursor()
        sql = "INSERT INTO data (nom, prenom,pays, date_naissance,tele,annee_bac,image) VALUES (%s,%s, %s, %s, %s,%s,%s)"
        val = (nom, prenom, pays,date_naissance,tele,annee_bac,image)
        mycursor.execute(sql, val)
        mydb.commit()
        # print(mycursor.rowcount, "utilisateur inséré.")
    def select_image(self):
        self.file_path = filedialog.askopenfilename()
        image = Image.open(self.file_path)
        image = image.resize((100, 100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.image_entree.delete(0, tk.END)
        self.image_entree.insert(0, self.file_path)
        self.label_image = tk.Label(self.page1, image=photo)
        self.label_image.image = photo
        self.label_image.grid(row=8, column=0, padx=5, pady=5)




    def show_current_page(self):
        # Masquer toutes les pages
        self.page1.pack_forget()
        self.page2.pack_forget()
        self.page3.pack_forget()
        self.page4.pack_forget()

        # Afficher la page correspondant à l'index actuel
        if self.current_page == 0:
            self.page1.pack(fill="both", expand=True)
            self.button_back.pack_forget()
            self.button_next.pack(side="right", padx=5, pady=5)
        elif self.current_page == 1:
            self.page2.pack(fill="both", expand=True)
            self.button_back.pack(side="left", padx=5, pady=5)
            self.button_next.pack(side="right", padx=5, pady=5)
        elif self.current_page == 2:
            self.page3.pack(fill="both", expand=True)
            self.button_back.pack(side="left", padx=5, pady=5)
            self.button_next.pack(side="right", padx=5, pady=5)
        elif self.current_page == 3:
            self.page4.pack(fill="both", expand=True)
            self.button_back.pack(side="left", padx=5, pady=5)
            self.button_next.pack_forget()

    def show_next_page(self):
        # Passer à la page suivante
        self.current_page = (self.current_page + 1) % 4
        self.show_current_page()

    def show_previous_page(self):
        # Revenir à la page précédente
        self.current_page = (self.current_page - 1) % 4
        self.show_current_page()


# Création de l'application
app = ExampleApp()
app.geometry("700x500")
# Lancer la boucle principale
app.mainloop()



