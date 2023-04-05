import csv
from tkinter import  *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("")

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
        self.label_CIN = tk.Label(self.page1, text="CIN :")
        self.label_CNE = tk.Label(self.page1, text="CNE :")
        self.label_Sexe = tk.Label(self.page1, text="Sexe :")
        self.label_Pays = tk.Label(self.page1, text="Pays :")
        # Création des zones de texte pour les informations
        self.entry_nom = tk.Entry(self.page1)
        self.entry_prenom = tk.Entry(self.page1)
        self.entry_CIN = tk.Entry(self.page1)
        self.entry_CNE = tk.Entry(self.page1)
        sexe = StringVar()
        # Création des boutons radio
        bouton_masculin = Radiobutton(self.page1, text="Masculin", variable=sexe, value="Masculin")
        bouton_feminin = Radiobutton(self.page1, text="Féminin", variable=sexe, value="Féminin")
        self.entry_Pays = tk.Entry(self.page1)
        # Placement des labels et des zones de texte
        self.label_nom.grid(row=1, column=0, padx=5, pady=5)
        self.label_prenom.grid(row=2, column=0, padx=5, pady=5)
        self.label_CIN.grid(row=3, column=0, padx=5, pady=5)
        self.entry_nom.grid(row=1, column=1, padx=5, pady=5)
        self.entry_prenom.grid(row=2, column=1, padx=5, pady=5)
        self.entry_CIN.grid(row=3, column=1, padx=5, pady=5)
        self.label_CNE.grid(row=4, column=0, padx=5, pady=5)
        self.label_Sexe.grid(row=5, column=0, padx=5, pady=5)
        self.label_Pays.grid(row=6, column=0, padx=5, pady=5)
        self.entry_CNE.grid(row=4, column=1, padx=5, pady=5)
        # Positionnement des boutons radio
        bouton_masculin.grid(row=5, column=1, padx=5, pady=5)
        bouton_feminin.grid(row=5, column=2, padx=5, pady=5)
        # self.entry_Pays.grid(row=6, column=1, padx=5, pady=5)

        # lire le fichier CSV et stocker les villes dans une liste
        with open('countries.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            countries = [row[0] for row in reader]
        # créer une variable pour stocker la ville sélectionnée
        var = tk.StringVar()
        # par défaut, la ville sélectionnée est la première ville de la liste
        var.set(countries[0])
        # créer un menu déroulant avec les villes
        menu = tk.OptionMenu(self.page1, var, *countries)
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
        self.label_VN = tk.Label(self.page2, text="Ville de Naissance :")
        self.label_PN = tk.Label(self.page2, text="Province de Naissance :")
        self.label_LN = tk.Label(self.page2, text="Lieu de Naissance :")
        # Création des zones de texte pour les informations
        self.entry_DN = tk.Entry(self.page2)
        self.entry_VN = tk.Entry(self.page2)
        self.entry_PN = tk.Entry(self.page2)
        self.entry_LN = tk.Entry(self.page2)
        # Placement des labels et des zones de texte
        self.label_DN.grid(row=1, column=0, padx=5, pady=5)
        self.label_VN.grid(row=2, column=0, padx=5, pady=5)
        self.label_PN.grid(row=3, column=0, padx=5, pady=5)
        self.label_LN.grid(row=4, column=0, padx=5, pady=5)
        self.entry_DN.grid(row=1, column=1, padx=5, pady=5)
        self.entry_PN.grid(row=3, column=1, padx=5, pady=5)
        self.entry_LN.grid(row=4, column=1, padx=5, pady=5)

        # self.entry_VN.grid(row=2, column=1, padx=5, pady=5)

        # lire le fichier CSV et stocker les villes dans une liste
        with open('ma.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            villes = [row[0] for row in reader]
        # créer une variable pour stocker la ville sélectionnée
        var = tk.StringVar()
        # par défaut, la ville sélectionnée est la première ville de la liste
        var.set(villes[0])
        # créer un menu déroulant avec les villes
        menu = tk.OptionMenu(self.page2, var, *villes)
        menu.grid(row=2, column=1, padx=5, pady=5)



        #@PAGE3
        self.label_TELE = tk.Label(self.page3, text="Tele :")
        self.label_EP = tk.Label(self.page3, text="Email Personnel :")
        self.label_EI = tk.Label(self.page3, text="Email Institutionnel :")
        # Création des zones de texte pour les informations
        self.entry_TELE = tk.Entry(self.page3)
        self.entry_EP = tk.Entry(self.page3)
        self.entry_EI = tk.Entry(self.page3)
        # Placement des labels et des zones de texte
        self.label_TELE.grid(row=1, column=0, padx=5, pady=5)
        self.label_EP.grid(row=2, column=0, padx=5, pady=5)
        self.label_EI.grid(row=3, column=0, padx=5, pady=5)
        self.entry_TELE.grid(row=1, column=1, padx=5, pady=5)
        self.entry_EP.grid(row=2, column=1, padx=5, pady=5)
        self.entry_EI.grid(row=3, column=1, padx=5, pady=5)


        # @page4
        self.label_AB = tk.Label(self.page4, text="Année d'obtention BAC  :")
        self.label_TB = tk.Label(self.page4, text="Type BAC :")
        self.label_MB = tk.Label(self.page4, text="Mention BAC :")
        self.label_PB = tk.Label(self.page4, text="Prov. d'obtention du BAC :")
        self.label_AC = tk.Label(self.page4, text="Académie :")
        self.label_LY = tk.Label(self.page4, text="Lycée  :")
        self.label_TL = tk.Label(self.page4, text="Type Lycée :")
        # Création des zones de texte pour les informations
        self.entry_AB = tk.Entry(self.page4)
        self.entry_TB = tk.Entry(self.page4)
        self.entry_MB = tk.Entry(self.page4)
        self.entry_PB = tk.Entry(self.page4)
        self.entry_AC = tk.Entry(self.page4)
        self.entry_LY = tk.Entry(self.page4)
        self.entry_TL = tk.Entry(self.page4)
        # Placement des labels et des zones de texte
        self.label_AB.grid(row=1, column=0, padx=5, pady=5)
        self.label_TB.grid(row=2, column=0, padx=5, pady=5)
        self.label_MB.grid(row=3, column=0, padx=5, pady=5)
        self.label_PB.grid(row=4, column=0, padx=5, pady=5)
        self.label_AC.grid(row=5, column=0, padx=5, pady=5)
        self.label_LY.grid(row=6, column=0, padx=5, pady=5)
        self.label_TL.grid(row=7, column=0, padx=5, pady=5)
        self.entry_AB.grid(row=1, column=1, padx=5, pady=5)
        self.entry_TB.grid(row=2, column=1, padx=5, pady=5)
        self.entry_MB.grid(row=3, column=1, padx=5, pady=5)
        self.entry_PB.grid(row=4, column=1, padx=5, pady=5)
        self.entry_AC.grid(row=5, column=1, padx=5, pady=5)
        self.entry_LY.grid(row=6, column=1, padx=5, pady=5)
        self.entry_TL.grid(row=7, column=1, padx=5, pady=5)

    def select_image(self):
        file_path = filedialog.askopenfilename()
        # print("Image sélectionnée :", file_path)
        image = Image.open(file_path)
        image = image.resize((100, 100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
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
