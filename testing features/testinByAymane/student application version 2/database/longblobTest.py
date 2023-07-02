import mysql.connector

from insert_data import connectDB


def insert_data(table_name, columns, data):
    cnx, cursor = connectDB('student_managment')
    cursor = cnx.cursor()
    columns_str = ", ".join(columns)
    values_str = ", ".join(["%s"] * len(columns))
    insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
    try:
        cursor.executemany(insert_query, data)
    except mysql.connector.Error as e:
        print(e)
        return
    cnx.commit()


#######
with open('les notes/BDD.pdf', 'rb') as f1, \
        open('les notes/Theorie des langages et Compilation.pdf', 'rb') as f2, \
        open('les notes/Big data 1.pdf', 'rb') as f3:
    BDD = f1.read()
    TLC = f2.read()
    BIGDATA = f3.read()

column = ['file']
data = [(BDD,), (TLC,), (BIGDATA,)]

insert_data('longblobtable', column, data)
