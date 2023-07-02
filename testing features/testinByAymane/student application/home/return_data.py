import numpy as np
from PIL import Image

from conneToDB import connectDB


def Convert_IMG(binary_data):
    array = np.frombuffer(binary_data, dtype=np.uint8)
    array = array.reshape((60, 60, 3))
    image = Image.fromarray(array)
    return image


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


print(return_data_by_id(10))
