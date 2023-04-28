from insert_data import insert_data,hash_password,connectDB
import mysql.connector
import numpy as np


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
    cnx,cursor = connectDB('student_managment')

    img = l[1][0].resize((60,60))
    print(img)
    img_np = np.array(img)
    img_bytes = img_np.tobytes()

    month=l[0][6][1]
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

    std_data=[(f'{l[0][0]}',f'{l[0][1]}',f'{l[0][2]}',f'{l[0][3]}',f'{l[0][4]}',f'{l[0][5]}',f'{l[0][6][2]}-{num}-{l[0][6][0]}',f'{img_bytes}'),]
    columns_std=['id_class','firstname','lastname','CIN','CNE','gender','birthday','image']
    insert_data("student",columns_std,std_data)


    print("done student")

    cin = l[0][3]
    cursor = cnx.cursor()
    query = ("SELECT id_student FROM student WHERE cin = %s")
    try:
        cursor.execute(query, (cin,))
    except mysql.connector.Error as e :
        return
    id_student = cursor.fetchone()[0]
    print(id_student)

    update_image(img,id_student)




    columns_bac=['id_student','bac_filier','bac_language','grid','bac_city','school_city','school_type']
    bac_data=[(f'{id_student}',f'{l[2][1]}',f'{l[2][2]}',f'{l[2][3]}',f'{l[2][0]}',f'{l[2][4]}',f'{l[2][5]}'),]
    insert_data("bac_student",columns_bac,bac_data)
    print("done bac")

    columns_login=['id_filier','email_acadymic','password']
    login_data=[(-1,f'{l[4][0]}',f'{hash_password(l[4][1])}'),]
    insert_data("login",columns_login,login_data)
    print("done login")


    columns_ct = ['id_student','adresse1','adresse2','country','city','postal_code','phone_number','email_acadymic']
    con_data=[(f'{id_student}',f'{l[3][0]}',f'{l[3][1]}',f'{l[3][5]}',f'{l[3][4]}',f'{l[3][2]}',f'{l[3][3]}',f'{l[4][0]}'),]
    insert_data("contact",columns_ct,con_data)
    print("done contact")


    columns_fs=['id_filier','id_student']
    fs_data=[(-1,f'{id_student}'),]
    insert_data("filier_student",columns_fs,fs_data)
    print("done fs")



    print("fin")





