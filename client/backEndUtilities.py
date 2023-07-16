import configparser
import hashlib
import os
import random as rd
import tempfile
import tkinter.filedialog as filedialog
from datetime import datetime
from tkinter import messagebox

import numpy as np
from PIL import Image
from mysql import connector


def get_database_credentials():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the config file
    config.read('config.ini')

    # Retrieve the database credentials
    username = config.get('database', 'username')
    password = config.get('database', 'password')
    host = config.get('database', 'host')
    port = config.get('database', 'port')
    return {"username": username, "password": password, "host": host, "port": port}


def connectMySQL():
    credentials = get_database_credentials()
    try:
        conn = connector.Connect(host=credentials["host"],
                                 user=credentials["username"],
                                 port=credentials["port"],
                                 password=credentials["password"]
                                 )
        # Creating the cursor
        cur = conn.cursor()
        #print("Connected to MySQL")
        return conn, cur

    except connector.Error as e:
        print(e)
        return e


def createDb(nameDB):
    conn, cur = connectMySQL()
    try:
        cur.execute(f"Create database {nameDB}")
        cur.execute("commit")
        # Closing the connection to the default database
        conn.close()

    except connector.Error as e:
        print(e)


def connectDB(nameDB):
    credentials = get_database_credentials()
    try:
        conn = connector.Connect(host=credentials["host"],
                                 user=credentials["username"],
                                 password=credentials["password"],
                                 port=int(credentials["port"]),
                                 db=nameDB

                                 )
        # Creating the cursor
        cur = conn.cursor()
        #print(f"Connected to {nameDB}")
        return conn, cur

    except connector.Error as e:
        print(e)
        return e


def insert_data(table_name, columns, data):
    cnx, cursor = connectDB('student_managment')
    cursor = cnx.cursor()
    columns_str = ", ".join(columns)
    values_str = ", ".join(["%s"] * len(columns))
    insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
    try:
        cursor.executemany(insert_query, data)
    except connector.Error as e:
        print(e)
        raise e
    cnx.commit()


def update_image(img, id_student):
    conn, cursor = connectDB("student_managment")
    resized_photo = img.resize((60, 60))
    img_np = np.array(resized_photo)
    sql_update = "UPDATE student SET image = %s WHERE id_student = %s"
    val = (img_np.tobytes(), id_student)
    cursor.execute(sql_update, val)
    conn.commit()
    cursor.close()
    conn.close()


def student_inscription(l):
    l[0] = [-1] + l[0]
    cnx, cursor = connectDB('student_managment')
    img = l[1][0].resize((60, 60))
    img_np = np.array(img)
    img_bytes = img_np.tobytes()

    month = l[0][6][1]
    if month.lower() == "january":
        num = 1
    elif month.lower() == "february":
        num = 2
    elif month.lower() == "march":
        num = 3
    elif month.lower() == "april":
        num = 4
    elif month.lower() == "may":
        num = 5
    elif month.lower() == "june":
        num = 6
    elif month.lower() == "july":
        num = 7
    elif month.lower() == "august":
        num = 8
    elif month.lower() == "september":
        num = 9
    elif month.lower() == "october":
        num = 10
    elif month.lower() == "november":
        num = 11
    elif month.lower() == "december":
        num = 12
    else:
        num = None

    std_data = [(f'{l[0][0]}', f'{l[0][1]}', f'{l[0][2]}', f'{l[0][3]}', f'{l[0][4]}', f'{l[0][5]}',
                 f'{l[0][6][2]}-{num}-{l[0][6][0]}', f'{img_bytes}'), ]
    columns_std = ['id_class', 'firstname', 'lastname', 'CIN', 'CNE', 'gender', 'birthday', 'image']
    insert_data("student", columns_std, std_data)


    cin = l[0][3]
    cursor = cnx.cursor()
    query = ("SELECT id_student FROM student WHERE cin = %s")
    try:
        cursor.execute(query, (cin,))
    except connector.Error as e:
        return
    id_student = cursor.fetchone()[0]

    update_image(img, id_student)

    columns_bac = ['id_student', 'bac_filier', 'bac_language', 'grid', 'bac_city', 'school_city', 'school_type']
    bac_data = [(f'{id_student}', f'{l[2][1]}', f'{l[2][2]}', f'{l[2][3]}', f'{l[2][0]}', f'{l[2][4]}', f'{l[2][5]}'), ]
    insert_data("bac_student", columns_bac, bac_data)
    print("done bac")

    columns_login = ['id_filier', 'email_acadymic', 'password']
    login_data = [(-1, f'{l[4][0]}', f'{hash_password(l[4][1])}'), ]
    insert_data("login", columns_login, login_data)
    print("done login")

    columns_ct = ['id_student', 'adresse1', 'adresse2', 'country', 'city', 'postal_code', 'phone_number',
                  'email_acadymic']
    con_data = [(f'{id_student}', f'{l[3][0]}', f'{l[3][1]}', f'{l[3][5]}', f'{l[3][4]}', f'{l[3][2]}', f'{l[3][3]}',
                 f'{l[4][0]}'), ]
    insert_data("contact", columns_ct, con_data)
    print("done contact")

    columns_fs = ['id_filier', 'id_student']
    fs_data = [(-1, f'{id_student}'), ]
    insert_data("filier_student", columns_fs, fs_data)
    print("done fs")

    print("fin")


def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()


def sign(email, password):
    cnx, mycursor = connectDB('student_managment')
    # Check if the user is an admin
    mycursor.execute("SELECT email_admin FROM admin")
    email_admin = mycursor.fetchall()[0][0]
    if email == email_admin:
        mycursor.execute("SELECT password FROM admin_login WHERE email = %s", (email,))
        result = mycursor.fetchone()
        code = result[0]
        if hash_password(password) == code:
            mycursor.execute("SELECT firstname, lastname, email_admin FROM admin WHERE id_admin=1")
            result = mycursor.fetchone()
            admin_info = list(result)
            dict_admin = {'firstname': admin_info[0], 'lastname': admin_info[1], 'email_admin': admin_info[2]}
            tuple_admin = ('admin', dict_admin)
            update_data_base() #to remove

            return tuple_admin
        else:
            return 'Password Error'
    else:
        # Check if the user is a student
        mycursor.execute("SELECT email_acadymic FROM login")
        results = mycursor.fetchall()
        emails = [result[0] for result in results]
        if email in emails:
            password_hash = hash_password(password)
            mycursor.execute("SELECT password FROM login WHERE email_acadymic = %s", (email,))
            result = mycursor.fetchone()
            code = result[0]
            if code == password_hash:
                mycursor.execute("SELECT id_student FROM contact WHERE email_acadymic = %s", (email,))
                result = mycursor.fetchone()
                id_student = result[0]
                mycursor.execute("SELECT firstname FROM student WHERE id_student = %s", (id_student,))
                result = mycursor.fetchone()
                firstname = result[0]
                mycursor.execute("SELECT lastname FROM student WHERE id_student = %s", (id_student,))
                result = mycursor.fetchone()
                lastname = result[0]
                mycursor.execute(
                    "SELECT name_class FROM class c, student s WHERE s.id_class = c.id_class AND id_student = %s",
                    (id_student,))
                result = mycursor.fetchone()
                class_name = result[0]
                mycursor.execute(
                    "SELECT f.name FROM filier f, filier_student fs WHERE f.id_filier = fs.id_filier AND fs.id_student = %s",
                    (id_student,))
                result = mycursor.fetchone()
                filiere = result[0]
                dict_std = {'firstname': firstname, 'lastname': lastname, 'id': id_student, 'class': class_name,
                            'filiere': filiere}
                tuple_std = ('student', dict_std)
                update_data_base()
                return tuple_std
            else:
                return 'Password Error'
        else:
            return 'Email Error'


def Convert_IMG(binary_data):
    array = np.frombuffer(binary_data, dtype=np.uint8).reshape((60, 60, 3))
    return Image.fromarray(array)


def return_data_by_id(id_student):
    def convert_number_to_month(number):
        months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        return months.get(number)

    db, cursor = connectDB('student_managment')

    cursor.execute(
        "SELECT firstname, lastname, cin, cne, gender, DAY(birthday), MONTH(birthday), YEAR(birthday) FROM student WHERE id_student = %s",
        (id_student,))
    liste1 = list(cursor.fetchone())
    liste1[5] = [liste1[5], convert_number_to_month(liste1[6]), liste1[7]]
    liste1 = liste1[:5] + [liste1[5]]

    cursor.execute("SELECT image FROM student WHERE id_student = %s", (id_student,))
    binary_data = cursor.fetchone()[0]
    liste2 = [Convert_IMG(binary_data)]

    cursor.execute(
        "SELECT bac_City, bac_filier, bac_language, grid, school_city, school_type FROM bac_student WHERE id_student = %s",
        (id_student,))
    liste3 = list(cursor.fetchone())

    cursor.execute(
        "SELECT adresse1, adresse2, postal_code, phone_number, city, country FROM contact WHERE id_student = %s",
        (id_student,))
    liste4 = list(cursor.fetchone())
    cursor.execute("SELECT email_acadymic FROM contact WHERE id_student = %s", (id_student,))
    liste5 = list(cursor.fetchone())

    cursor.execute("SELECT name_class FROM class c, student s WHERE c.id_class = s.id_class AND id_student = %s",
                   (id_student,))
    liste6 = [result[0] for result in cursor.fetchall()]
    cursor.execute(
        "select name from filier f , filier_student fs where f.id_filier = fs.id_filier  and id_student = %s",
        (id_student,))
    liste6.append(cursor.fetchone()[0])

    list_final = [liste1, liste2, liste3, liste4, liste5, liste6]

    cursor.close()
    db.close()
    return list_final


def id_class(class_name):
    class_id = -1
    if class_name == 'ID1':
        class_id = 1
    elif class_name == 'ID2':
        class_id = 2
    elif class_name == 'GI1':
        class_id = 3
    elif class_name == 'GI2':
        class_id = 4
    elif class_name == 'GC1':
        class_id = 5
    elif class_name == 'GC2':
        class_id = 6
    elif class_name == 'GEER1':
        class_id = 7
    elif class_name == 'GEER2':
        class_id = 8
    return class_id


def delete_student(student_id):
    try :
        mydb, mycursor = connectDB('student_managment')

        # Récupérer l'e-mail académique de l'étudiant depuis la base de données
        select_req = 'SELECT c.email_acadymic FROM student s, contact c WHERE s.id_student = c.id_student AND s.id_student = %s'
        mycursor.execute(select_req, (student_id,))
        email_academic = mycursor.fetchone()[0]

        # Suppression de l'étudiant
        del_from_contact = "DELETE FROM contact WHERE id_student = %s"
        del_from_login = "DELETE FROM login WHERE email_acadymic = %s"
        del_from_bac_student = "DELETE FROM bac_student WHERE id_student = %s"
        del_from_filiere_student = "DELETE FROM filier_student WHERE id_student = %s"
        del_from_student = "DELETE FROM student WHERE id_student = %s"
        val = (student_id,)
        mycursor.execute(del_from_bac_student, val)
        mycursor.execute(del_from_contact, val)
        mycursor.execute(del_from_login, (email_academic,))
        mycursor.execute(del_from_filiere_student, val)
        mycursor.execute(del_from_student, val)

        mydb.commit()
        return True
    except:
        mydb.commit()
        return False


def insert_into_document(file_type, file_class, file_titre, file_path):
    execution_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        cnx, cursor = connectDB('student_managment')

        insert_query = ("INSERT INTO documents(type, titre,class, file, date_doc) VALUES (%s,%s, %s, %s, %s)")
        with open(file_path, 'rb') as f:
            pdf_file = f.read()
        insert_values = (file_type, file_titre, file_class, pdf_file, execution_date)
        cursor.execute(insert_query, insert_values)
        cnx.commit()

        cursor.close()
        cnx.close()
        print("done")
        messagebox.showinfo("Insertion", "Document successfully inserted")
        return True


    except connector.Error as err:
        print(err)
        return False


def save_into_emploi_temps(file_class, file_path):
    execution_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        # Connexion à la base de données MySQL
        cnx, cursor = connectDB('student_managment')

        # Insertion des données dans la table "files"
        insert_query = ("INSERT INTO emploi_temps(class, timetable, date_pub) VALUES (%s,%s, %s)")
        with open(file_path, 'rb') as f:
            pdf_file = f.read()
        insert_values = (file_class, pdf_file, execution_date)
        cursor.execute(insert_query, insert_values)
        cnx.commit()

        cursor.close()
        cnx.close()
        messagebox.showinfo("Insertion", "Document inserted succesfully")



    except connector.Error as err:
        print(err)
        messagebox.showerror("Insertion", "Document inserted failed")
        return


def save_into_affichage(file_class, file_module, file_path):
    execution_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        # Connexion à la base de données MySQL
        cnx, cursor = connectDB('student_managment')

        # Insertion des données dans la table "files"
        insert_query = ("INSERT INTO affichage(class,module,notetable, date_pub) VALUES (%s,%s, %s, %s)")
        with open(file_path, 'rb') as f:
            pdf_file = f.read()
        insert_values = (file_class, file_module, pdf_file, execution_date)
        cursor.execute(insert_query, insert_values)
        cnx.commit()

        cursor.close()
        cnx.close()
        messagebox.showinfo("Insertion", "Document inserted succesfully")

    except connector.Error as err:
        print(err)
        messagebox.showerror("Insertion", "Document inserted failed")
        return


def insert_into_notification(title, detail, filiere):
    mydb, mycursor = connectDB('student_managment')
    date_pub = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    select_req = 'SELECT id_filier FROM filier WHERE name = %s'
    mycursor.execute(select_req, (filiere,))
    id_filier = mycursor.fetchone()[0]
    sql = "INSERT INTO notification (id_filier, title, detail, date_not) VALUES (%s, %s, %s, %s)"
    val = (id_filier, title, detail, date_pub)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Insertion", "News added succesfully")


def get_data():
    conn, cursor = connectDB('student_managment')

    nb_visiteur = "select nb_visiteur from graph_table order by  date desc limit 5 OFFSET 1"
    cursor.execute(nb_visiteur)
    nb_visiteurs = np.array(cursor.fetchall())

    date = "select date from graph_table order by  date desc limit 5 OFFSET 1"
    cursor.execute(date)
    dates_list = cursor.fetchall()

    dates_str_list = [datetime.strftime(date[0], '%Y-%m-%d') for date in dates_list]
    dates = np.array(dates_str_list)

    cursor.close()
    conn.close()
    return nb_visiteurs, dates


def update_data_base():
    import datetime
    date_systeme = datetime.date.today()
    date_systeme = date_systeme.strftime('%Y-%m-%d')
    conn, cursor = connectDB('student_managment')
    req = "select count(*) from graph_table where date = %s"
    cursor.execute(req, (date_systeme,))
    res = cursor.fetchall()[0][0]

    if res == 0:
        insert_req = 'insert into graph_table(nb_visiteur,date) values (%s,%s)'
        val = (1, date_systeme)
        cursor.execute(insert_req, val)
        conn.commit()
        print("add date")
    else:
        select_req = "select nb_visiteur from graph_table where date = %s"
        cursor.execute(select_req, (date_systeme,))
        res = cursor.fetchall()[0][0]
        update_req = "UPDATE graph_table SET nb_visiteur = %s WHERE date = %s"
        nb = res + 1
        val = (nb, date_systeme)
        cursor.execute(update_req, val)
        conn.commit()
        print("update date")


def get_pdf_affichage_from_database(index):
    conn, cursor = connectDB('student_managment')

    query = "SELECT notetable FROM affichage order by date_pub desc "
    cursor.execute(query)
    rows = cursor.fetchall()
    if index >= len(rows):
        return None

    pdf_content = rows[index][0]
    return pdf_content


def download_pdf(pdf_content):
    # Demander à l'utilisateur de choisir le dossier où il souhaite stocker le fichier PDF
    folder_path = filedialog.askdirectory()

    if folder_path:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(pdf_content)
        temp_file.close()

        # Obtenez le nom de fichier aléatoire
        n = rd.randrange(1000000000000000000, 999999999999999999999)
        name_file = f"{n}.pdf"

        # Créez le fichier de destination dans le dossier choisi par l'utilisateur
        destination_file = os.path.join(folder_path, name_file)

        # Copiez le contenu du fichier temporaire vers le fichier de destination
        with open(destination_file, "wb") as f:
            f.write(pdf_content)

        # Ouvrez le dossier dans l'explorateur de fichiers
        os.startfile(folder_path)


def download_button_click(index):
    pdf_content = get_pdf_affichage_from_database(index)
    if pdf_content is not None:
        download_pdf(pdf_content)


def update_student(field_name, new_value, id_student):
    if field_name == 'class':
        if new_value == 'ID1':
            update_table('student', 'id_class', 1, id_student)
        elif new_value == 'ID2':
            update_table('student', 'id_class', 2, id_student)
        elif new_value == 'GI1':
            update_table('student', 'id_class', 3, id_student)
        elif new_value == 'GI2':
            update_table('student', 'id_class', 4, id_student)
        elif new_value == 'GC1':
            update_table('student', 'id_class', 5, id_student)
        elif new_value == 'GC2':
            update_table('student', 'id_class', 6, id_student)
        elif new_value == 'GEER1':
            update_table('student', 'id_class', 7, id_student)
        elif new_value == 'GEER2':
            update_table('student', 'id_class', 8, id_student)
    if field_name == 'filiere':
        cnx, cursor = connectDB('student_managment')
        cursor.execute("Select email_acadymic from contact where id_student = %s ", (id_student,))
        email = cursor.fetchall()[0][0]
        if new_value == 'ID':
            update_table('filier_student', 'id_filier', 1, id_student)
            update_login('login', 'id_filier', 1, email)
        elif new_value == 'GI':
            update_table('filier_student', 'id_filier', 2, id_student)
            update_login('login', 'id_filier', 2, email)
        elif new_value == 'GC':
            update_table('filier_student', 'id_filier', 3, id_student)
            update_login('login', 'id_filier', 3, email)

        elif new_value == 'GEER':
            update_table('filier_student', 'id_filier', 4, id_student)
            update_login('login', 'id_filier', 4, email)


def update_table(table_name, field_name, new_value, id_student):
    db, cursor = connectDB('student_managment')
    sql_query = f"UPDATE {table_name} SET {field_name} = %s WHERE id_student = %s"
    cursor.execute(sql_query, (new_value, id_student))
    db.commit()
    print(f"Nombre de lignes mises à jour : {cursor.rowcount}")
    cursor.close()
    db.close()


def update_login(table_name, field_name, new_value, email):
    db, cursor = connectDB('student_managment')
    sql_query = f"UPDATE {table_name} SET {field_name} = %s WHERE email_acadymic = %s"
    cursor.execute(sql_query, (new_value, email))
    db.commit()
    print(f"Nombre de lignes mises à jour : {cursor.rowcount}")
    cursor.close()
    db.close()
