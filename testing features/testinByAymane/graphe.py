#
# import matplotlib
#
# matplotlib.use('TkAgg')
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import tkinter as tk
#
# # Données de test
#
# dates = ['2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05']
# y = [10, 20, 15, 25, 18]
# labels = ['2023-03-01 \n nbr.Connexions 10', '2023-03-02 \n nbr.Connexions 20', '2023-03-03 \n nbr.Connexions 15', '2023-03-04 \n nbr.Connexions 25', '2023-03-04 \n nbr.Connexions 18']
#
# # Convertir les dates en format matplotlib
# dates = [mdates.datestr2num(d) for d in dates]
#
# # Créer le graphe
# fig, ax = plt.subplots()
# scatter = ax.scatter(dates, y)
#
#
# # Fonction pour afficher le texte au survol
# def hover(event):
#     vis = scatter.contains(event)[0]
#     if vis:
#         ind = scatter.contains(event)[1]["ind"][0]
#         text.set_text(labels[ind])
#         text.set_position((dates[ind], y[ind]))
#         text.set_visible(True)
#     else:
#         text.set_visible(False)
#     fig.canvas.draw_idle()
#
# # Ajouter le texte
# text = ax.text(0, 0, "", ha="center", va="center", backgroundcolor=(1, 1, 1, 0.7))
#
# # Ajouter la fonction de survol
# fig.canvas.mpl_connect("motion_notify_event", hover)
#
# # Formater les dates sur l'axe des x
# date_format = mdates.DateFormatter('%Y-%m-%d')
# ax.xaxis.set_major_formatter(date_format)
#
# # Afficher les abscisses verticalement
# ax.xaxis.set_tick_params(rotation=45)
#
# # Créer une fenêtre Tkinter
# root = tk.Tk()
# root.title("Statistiques d'accès à E-Students")
#
# # Créer un widget pour afficher le graphe
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.draw()
# canvas.get_tk_widget().pack()
#
# # Ajouter un bouton pour fermer la fenêtre
# button = tk.Button(master=root, text="Fermer", command=root.destroy)
# button.pack()
# root.geometry("800x800")
#
#
# tk.mainloop()
#

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Création de la fenêtre
root = tk.Tk()

# Création du widget Treeview
tree = ttk.Treeview(root)

# Ajout des colonnes
tree["columns"] = ("id", "nom", "prenom", "age", "image")

# Définition des en-têtes de colonnes
tree.heading("id", text="ID")
tree.heading("nom", text="Nom")
tree.heading("prenom", text="Prenom")
tree.heading("age", text="Age")
tree.heading("image", text="Image")

# Création de la propriété image_references pour stocker les références aux objets PhotoImage
tree.image_references = []

# Insertion des données dans le widget Treeview
# Exemple de données
data = [
    {"id": 1, "nom": "aymane", "prenom": "maghouti", "age": 20, "image": "C:/Users/pc/PycharmProjects/pythonProject/projet_web/mon_image.png"},
    {"id": 2, "nom": "oussam", "prenom": "outmani", "age": 20, "image": "C:/Users/pc/PycharmProjects/pythonProject/projet_web/mon_image.png"},
    {"id": 3, "nom": "tata", "prenom": "oussama", "age": 21, "image": "C:/Users/pc/PycharmProjects/pythonProject/projet_web/mon_image.png"}
]

for row in data:
    with Image.open(row["image"]) as logo_image :
        logo_image_regular = ImageTk.PhotoImage(logo_image)

    tree.insert(parent="", index=tk.END, values=(row["id"],row["nom"], row["prenom"], row["age"]), image=logo_image_regular)


# Affichage du widget Treeview
tree.pack()

# Démarrage de la boucle principale de la fenêtre
root.mainloop()
