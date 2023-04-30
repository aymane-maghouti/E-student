import hashlib
from conneToDB import connectDB

conn,mycursor  = connectDB('student_managment')
def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

def sign(email, password):
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
                mycursor.execute("SELECT name_class FROM class c, student s WHERE s.id_class = c.id_class AND id_student = %s", (id_student,))
                result = mycursor.fetchone()
                class_name = result[0]
                mycursor.execute("SELECT f.name FROM filier f, filier_student fs WHERE f.id_filier = fs.id_filier AND fs.id_student = %s", (id_student,))
                result = mycursor.fetchone()
                filiere = result[0]
                dict_std = {'firstname': firstname, 'lastname': lastname, 'id': id_student, 'class': class_name, 'filiere': filiere}
                tuple_std = ('student', dict_std)
                return tuple_std
            else:
                return 'Password Error'
        else:
            return 'Email Error'







