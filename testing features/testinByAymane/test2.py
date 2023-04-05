import mysql.connector
from PIL import Image
from io import BytesIO
import mysql.connector
from jinja2 import Template

# Se connecter à la base de données
cnx = mysql.connector.connect(user='root', password='MG1234',
                              host='localhost', database='gestion_etudiant')
cursor = cnx.cursor()

# Exécuter une requête SQL pour récupérer toutes les données d'une table
query = "SELECT * FROM exemple where id = 2"
cursor.execute(query)

# Récupérer toutes les données
data = cursor.fetchall()
# print(data)

# Récupérer les données de l'image
image_data = data[0][-1]

# Ouvrir les données de l'image comme un flux d'octets
img_stream = BytesIO(image_data)

# Ouvrir l'image avec Pillow
image = Image.open(img_stream)

# Enregistrer l'image dans un fichier
image.save("C:/Users/pc/PycharmProjects/pythonProject/projet_web/mon_image.jpg")



path = "C:/Users/pc/PycharmProjects/pythonProject/projet_web/mon_image.jpg"

print(path)
cursor.close()
cnx.close()



donnees = {"nom" : data[0][2], "prenom" : data[0][1]  ,"age" :data[0][3], "path" : path}

template_html = Template(open("index.html").read())
html_final = template_html.render(donnees)

with open('donnees.html', 'w') as f:
    f.write(html_final)


import webbrowser

webbrowser.open('donnees.html')









