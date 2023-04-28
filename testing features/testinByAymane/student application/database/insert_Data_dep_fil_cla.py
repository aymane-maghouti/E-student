from insert_data import connectDB
mydb,mycursor =connectDB('student_managment')


mycursor.execute("insert into departement(id_deprtement,name) values (-1,'------------')")
mycursor.execute("insert into filier(id_filier,name,description,id_departement) values (-1,'---','----------------',-1)")
mycursor.execute("insert into class(id_class,name_class,id_filier) values (-1,'------------',-1)")

mydb.commit()

mycursor.close()
mydb.close()