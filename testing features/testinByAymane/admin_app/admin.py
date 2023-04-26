import mysql.connector
from datetime import datetime


def connectDB(nameDB):
    try:
        cnx = mysql.connector.connect(user='root', password='MG1234',
                                      host='localhost',
                                      database=nameDB)

        cursor = cnx.cursor()
        return cnx, cursor

    except mysql.connector.Error as e:
        return


def save_into_affichagee(file_class, file_module, file_path):
    execution_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        cnx, cursor = connectDB('student_managment')

        insert_query = ("INSERT INTO affichage(class,module,notetable, date_pub) VALUES (%s,%s, %s, %s)")
        with open(file_path, 'rb') as f:
            pdf_file = f.read()
        insert_values = (file_class, file_module, pdf_file, execution_date)
        cursor.execute(insert_query, insert_values)
        cnx.commit()

        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        return


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


    except mysql.connector.Error as err:
        return


def save_into_emploi_temps(file_class, file_path):
    execution_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        cnx, cursor = connectDB('student_managment')

        insert_query = ("INSERT INTO emploi_temps(class, timetable, date_pub) VALUES (%s,%s, %s)")
        with open(file_path, 'rb') as f:
            pdf_file = f.read()
        insert_values = (file_class, pdf_file, execution_date)
        cursor.execute(insert_query, insert_values)
        cnx.commit()

        cursor.close()
        cnx.close()


    except mysql.connector.Error as err:
        return


def delete_student(student_id):
    mydb, mycursor = connectDB('student_managment')

    select_req = 'SELECT c.email_acadymic FROM student s, contact c WHERE s.id_student = c.id_student AND s.id_student = %s'
    mycursor.execute(select_req, (student_id,))
    email_academic = mycursor.fetchone()[0]

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
    if field_name == 'filier':
        if new_value == 'ID':
            update_table('filier_student', 'id_filier', 1, id_student)
        elif new_value == 'GI':
            update_table('filier_student', 'id_filier', 2, id_student)
        elif new_value == 'GC':
            update_table('filier_student', 'id_filier', 3, id_student)
        elif new_value == 'GEER':
            update_table('filier_student', 'id_filier', 4, id_student)


def update_table(table_name, field_name, new_value, id_student):
    db, cursor = connectDB('student_managment')
    sql_query = f"UPDATE {table_name} SET {field_name} = %s WHERE id_student = %s"
    cursor.execute(sql_query, (new_value, id_student))
    db.commit()
    print(f"Nombre de lignes mises à jour : {cursor.rowcount}")
    cursor.close()
    db.close()


# Créer une fonction pour insérer les données
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
