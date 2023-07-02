from io import BytesIO

import mysql.connector
from PIL import Image

# Open the image file with Pillow
image = Image.open('image.jpg')

# Convert the image to bytes using BytesIO
buffer = BytesIO()
image.save(buffer, format='JPEG')
image_bytes = buffer.getvalue()

# Store the image in MySQL
cnx = mysql.connector.connect(user='your_username', password='your_password',
                              host='your_host', database='your_database')
cursor = cnx.cursor()
add_image = ("INSERT INTO images "
             "(id, image_data) "
             "VALUES (%s, %s)")
data_image = (1, image_bytes)
cursor.execute(add_image, data_image)
cnx.commit()
cursor.close()
cnx.close()
