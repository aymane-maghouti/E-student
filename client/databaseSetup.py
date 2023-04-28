from backEndUtilities import createDb,connectMySQL, connectDB,insert_data

import mysql.connector



_,mycur = connectMySQL()
createDb("student_managment")
cnx,mycursor=connectDB("student_managment")
# TABLE : departement
mycursor.execute("create table if not exists departement(id_departement int primary key auto_increment,name varchar(45))")
# TABLE : filier
mycursor.execute("create table if not exists filier(id_filier int primary key auto_increment,name varchar(45),description varchar(200),id_departement int not null,foreign key (id_departement) references departement(id_departement))")

#TABLE : class
mycursor.execute("create table if not exists class(id_class int primary key auto_increment,name_class varchar(45),id_filier int not null,foreign key (id_filier) references filier(id_filier))")

# TABLE : student
mycursor.execute("create table if not exists student (id_student int primary key auto_increment,id_class int not null,firstname varchar(45),lastname varchar(45),CIN varchar(45),CNE varchar(45),gender varchar(45),birthday date,image longBlob,foreign key (id_class) references class(id_class))")
# TABLE : bac_student
mycursor.execute("create table if not exists bac_student (id_bac_student int primary key auto_increment,id_student int not null,bac_filier varchar(45),bac_language varchar(45),grid numeric(4,2),bac_city varchar(45),school_city varchar(45),school_type varchar(45),foreign key (id_student) references student(id_student))")
# TABLE : contact
mycursor.execute("create table if not exists contact (id_contact int primary key auto_increment,id_student int not null,adresse1 varchar(150),adresse2 varchar(150),country varchar(45),city varchar(45),postal_code varchar(45),phone_number varchar(45),email_personel varchar(45),email_acadymic varchar(45),foreign key (id_student) references student(id_student))")

# TABLE : login
mycursor.execute("create table if not exists login (id_login int primary key auto_increment,id_filier int not null,email_acadymic varchar(45) ,password varchar(200),foreign key (id_filier) references filier(id_filier))")
# TABLE : notification
mycursor.execute("create table if not exists Notification (id_notification int primary key auto_increment,id_filier int not null,title varchar(200),detail varchar(9999),date_not datetime,foreign key (id_filier) references filier(id_filier))")
# TABLE : admin
mycursor.execute("create table if not exists Admin(id_admin int primary key auto_increment,firstname varchar(45),lastname varchar(45),CIN varchar(45),birthday date,image longBlob,email_admin varchar(200))")
# TABLE : prof
mycursor.execute("create table  if not exists prof(id_prof int primary key auto_increment,firstname varchar(45),lastname varchar(45),CIN varchar(45),email_prof varchar(200),id_departement int not null,foreign key (id_departement) references departement(id_departement))")
# TABLE : filier_student
mycursor.execute("CREATE table if not exists filier_student (id_filier_student int primary key auto_increment,id_filier int not null,id_student int not null,foreign key (id_filier) references filier(id_filier),foreign key (id_student) references student(id_student))")
# TABLE : Affichage
mycursor.execute("CREATE table if not exists affichage(id_affichage int primary key auto_increment,class varchar(45),module  varchar(45),notetable longblob,date_pub datetime)")
# TABLE : emploi_temps
mycursor.execute("CREATE table if not exists emploi_temps(id_emploi int primary key auto_increment,class varchar(45),timetable longblob,date_pub datetime)")
# TABLE : documents
mycursor.execute("CREATE table if not exists documents(id_cours int primary key auto_increment,type varchar(45),titre varchar(45),class varchar(45),file longblob,date_doc datetime)")
#Table : graphe
mycursor.execute("CREATE table if not exists graph_table(id int primary key auto_increment,nb_visiteur int ,date date)")
#TABLR : admin_login
mycursor.execute("create table if not exists admin_login (id int primary key  auto_increment,id_admin int not null,email varchar(100),password varchar(999),foreign key (id_admin) references admin(id_admin))")



print("all tables are created ")
cnx.commit()
mycursor.close()
cnx.close()
#inserting starter infos

mydb,mycursor =connectDB('student_managment')

#default empty class,filiere,departement
mycursor.execute("insert into departement(id_departement,name) values (-1,'------------')")
mycursor.execute("insert into filier(id_filier,name,description,id_departement) values (-1,'---','----------------',-1)")
mycursor.execute("insert into class(id_class,name_class,id_filier) values (-1,'------------',-1)")

mydb.commit()

mycursor.close()
mydb.close()

#departemenet Data
columns_departement=['name']
data_depertement=[('Département Mathématiques et Informatique',),('Département Génie Civil Energétique et Environnement',)]
insert_data("departement", columns_departement, data_depertement)

#filier data
columns_filier=['name','description','id_departement']
data_filier=[('ID','Ingénierie des données',1),('GI','Génie Informatique',1),
             ('GEER','Génie énergétique et énergies renouvelables',2),('GC','Génie Civil',2)]
insert_data("filier", columns_filier, data_filier)

#class data
columns_class=['name_class','id_filier']
data_class=[('ID1',1),
            ('ID2',1),
            ('GI1',2),
            ('GI2',2),
            ('GC2',3),
            ('GC2',3),
            ('GEER1',4),
            ('GEER2',4)]
insert_data("class", columns_class, data_class)





