from datetime import datetime

import numpy as np

from conneToDB import connectDB


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
