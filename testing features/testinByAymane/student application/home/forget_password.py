import hashlib
import random
import string

from conneToDB import connectDB

conn, mycursor = connectDB('student_managment')


def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()


def sendpasswod(email, password):
    return 'the password is sended'


def generate_password():
    min_length = 8
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    num_lower = 0
    num_upper = 0
    num_digit = 0
    password = ""
    while len(password) < min_length or num_lower == 0 or num_upper == 0 or num_digit == 0:
        char_type = random.randint(1, 3)
        if char_type == 1:
            password += random.choice(lowercase_letters)
            num_lower += 1
        elif char_type == 2:
            password += random.choice(uppercase_letters)
            num_upper += 1
        else:
            password += random.choice(digits)
            num_digit += 1
    return password


def forget(email):
    mycursor.execute("SELECT email_acadymic FROM login")
    results = mycursor.fetchall()
    emails = [result[0] for result in results]
    if email in emails:
        new_password = generate_password()
        print('the new password is ', new_password)
        new_password_hashed = hash_password(new_password)
        print(new_password_hashed)
        sql = "UPDATE login SET password = %s WHERE email_acadymic =  %s"
        values = (new_password_hashed, email)
        mycursor.execute(sql, values)
        conn.commit()
        print(sendpasswod(email, new_password))
        return 'password changed'

    else:
        return 'Email Error'


print(forget('o.o@etu.uae.ac.ma'))
