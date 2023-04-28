from mysql import connector
import hashlib
import numpy as np

def connectMySQL():
    try:
        conn = connector.Connect(host="localhost",  # your host, usually localhost
                                 user="root",  # your username
                                 port="3306"  # port (3306 default)
                                 )
        # Creating the cursor
        cur = conn.cursor()
        print("Connected to MySQL")
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

def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

def connectDB(nameDB):
    try:
        conn = connector.Connect(host="localhost",  # your host, usually localhost
                                 user="root",  # your username
                                 port="3306",  # port (3306 default)
                                 db=nameDB
                                 )
        # Creating the cursor
        cur = conn.cursor()
        print(f"Connected to {nameDB}")
        return conn, cur

    except connector.Error as e:
        print(e)
        return e

def insert_data(table_name, columns, data):
    cnx,cursor = connectDB('student_managment')
    cursor = cnx.cursor()
    columns_str = ", ".join(columns)
    values_str = ", ".join(["%s"] * len(columns))
    insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
    try:
        cursor.executemany(insert_query, data)
    except connector.Error as e :
        print(e)
        return
    cnx.commit()


def student_inscription(l):
    l[0] = [-1] + l[0]
    cnx, cursor = connectDB('student_managment')

    img = l[1][0]
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

    print("done student")

    cin = l[0][3]
    cursor = cnx.cursor()
    query = ("SELECT id_student FROM student WHERE cin = %s")
    try:
        cursor.execute(query, (cin,))
    except connector.Error as e:
        print(e)
        return
    id_student = cursor.fetchone()[0]
    print(id_student)
    cursor.close()
    cnx.close()

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


