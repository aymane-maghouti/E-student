import mysql.connector


def connectDB(nameDB):
    try:
        cnx = mysql.connector.connect(user='root',
                                      host='localhost',
                                      database=nameDB)

        cursor = cnx.cursor()
        return cnx, cursor

    except mysql.connector.Error as e:
        return
