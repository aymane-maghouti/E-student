from backEndUtilities import createDb, connectMySQL, connectDB, insert_data, hash_password


def checkIfAlreadyInstalled(database_name):
    conn, cursor = connectMySQL()
    query = "SHOW DATABASES LIKE %s"
    cursor.execute(query, (database_name,))
    database_exists = cursor.fetchone() is not None
    cursor.close()
    conn.close()

    return database_exists


def run():
    _, mycur = connectMySQL()
    createDb("student_managment")
    sql = "use student_managment"
    mycur.execute(sql)

    cnx, mycursor = connectDB("student_managment")
    # TABLE : departement
    mycursor.execute(
        "create table if not exists departement(id_departement int primary key auto_increment,name varchar(45))")
    # TABLE : filier
    mycursor.execute(
        "create table if not exists filier(id_filier int primary key auto_increment,name varchar(45),description varchar(200),id_departement int not null,foreign key (id_departement) references departement(id_departement))")
    # TABLE : class
    mycursor.execute(
        "create table if not exists class(id_class int primary key auto_increment,name_class varchar(45),id_filier int not null,foreign key (id_filier) references filier(id_filier))")
    # TABLE : student
    mycursor.execute(
        "create table if not exists student (id_student int primary key auto_increment,id_class int not null,firstname varchar(45),lastname varchar(45),CIN varchar(45),CNE varchar(45),gender varchar(45),birthday date,image longBlob,foreign key (id_class) references class(id_class))")
    # TABLE : bac_student
    mycursor.execute(
        "create table if not exists bac_student (id_bac_student int primary key auto_increment,id_student int not null,bac_filier varchar(45),bac_language varchar(45),grid numeric(4,2),bac_city varchar(45),school_city varchar(45),school_type varchar(45),foreign key (id_student) references student(id_student))")
    # TABLE : contact
    mycursor.execute(
        "create table if not exists contact (id_contact int primary key auto_increment,id_student int not null,adresse1 varchar(150),adresse2 varchar(150),country varchar(45),city varchar(45),postal_code varchar(45),phone_number varchar(45),email_personel varchar(45),email_acadymic varchar(45),foreign key (id_student) references student(id_student))")

    # TABLE : login
    mycursor.execute(
        "create table if not exists login (id_login int primary key auto_increment,id_filier int not null,email_acadymic varchar(45) ,password varchar(200),foreign key (id_filier) references filier(id_filier))")
    # TABLE : notification
    mycursor.execute(
        "create table if not exists Notification (id_notification int primary key auto_increment,id_filier int not null,title varchar(200),detail varchar(9999),date_not datetime,foreign key (id_filier) references filier(id_filier))")
    # TABLE : admin
    mycursor.execute(
        "create table if not exists Admin(id_admin int primary key auto_increment,firstname varchar(45),lastname varchar(45),CIN varchar(45),birthday date,image longBlob,email_admin varchar(200))")
    # TABLE : prof
    mycursor.execute(
        "create table  if not exists prof(id_prof int primary key auto_increment,firstname varchar(45),lastname varchar(45),CIN varchar(45),email_prof varchar(200),id_departement int not null,foreign key (id_departement) references departement(id_departement))")
    # TABLE : filier_student
    mycursor.execute(
        "CREATE table if not exists filier_student (id_filier_student int primary key auto_increment,id_filier int not null,id_student int not null,foreign key (id_filier) references filier(id_filier),foreign key (id_student) references student(id_student))")
    # TABLE : Affichage
    mycursor.execute(
        "CREATE table if not exists affichage(id_affichage int primary key auto_increment,class varchar(45),module  varchar(45),notetable longblob,date_pub datetime)")
    # TABLE : emploi_temps
    mycursor.execute(
        "CREATE table if not exists emploi_temps(id_emploi int primary key auto_increment,class varchar(45),timetable longblob,date_pub datetime)")
    # TABLE : documents
    mycursor.execute(
        "CREATE table if not exists documents(id_cours int primary key auto_increment,type varchar(45),titre varchar(45),class varchar(45),file longblob,date_doc datetime)")
    # Table : graphe
    mycursor.execute(
        "CREATE table if not exists graph_table(id int primary key auto_increment,nb_visiteur int ,date date)")
    # TABLR : admin_login
    mycursor.execute(
        "create table if not exists admin_login (id int primary key  auto_increment,id_admin int not null,email varchar(100),password varchar(999),foreign key (id_admin) references admin(id_admin))")

    print("all tables are created ")
    cnx.commit()
    mycursor.close()
    cnx.close()
    # inserting starter infos

    mydb, mycursor = connectDB('student_managment')

    # default empty class,filiere,departement
    mycursor.execute("insert into departement(id_departement,name) values (-1,'-')")
    mycursor.execute("insert into filier(id_filier,name,description,id_departement) values (-1,'-','-',-1)")
    mycursor.execute("insert into class(id_class,name_class,id_filier) values (-1,'-',-1)")

    mydb.commit()

    mycursor.close()
    mydb.close()

    columns_admin = ['firstname', 'lastname', 'CIN', 'birthday', 'image', 'email_admin']
    data_admin = [('cherradi', 'Mohamed', 'Z12345', '1989-01-12', '', 'medcherradi00@gmail.com')]

    # admin_login
    columns_admin_login = ['id_admin', 'email', 'password']
    data_admin_login = [(1, 'medcherradi00@gmail.com', hash_password('Admin1234'))]
    insert_data("admin_login", columns_admin_login, data_admin_login)

    # AFFICHAGE DATA
    with open('les notes/BDD.pdf', 'rb') as f1, \
            open('les notes/Theorie des langages et Compilation.pdf', 'rb') as f2, \
            open('les notes/Big data 1.pdf', 'rb') as f3, \
            open('les notes/AI 1- ML- .pdf', 'rb') as f4, \
            open('les notes/RO.pdf', 'rb') as f5, \
            open('les notes/langage C.pdf', 'rb') as f6, \
            open('les notes/Java.pdf', 'rb') as f7, \
            open('les notes/python.pdf', 'rb') as f8, \
            open('les notes/dessin.pdf', 'rb') as f9, \
            open('les notes/Topographie.pdf', 'rb') as f10, \
            open('les notes/RDM 3.pdf', 'rb') as f11:
        BDD = f1.read()
        TLC = f2.read()
        BIGDATA = f3.read()
        ML = f4.read()
        RO = f5.read()
        Lc = f6.read()
        java = f7.read()
        python = f8.read()
        dessin = f9.read()
        topo = f10.read()
        RDM = f11.read()
    columns_affichage = ['class', 'module', 'notetable', 'date_pub']
    data_affichage = [('ID1', 'BDD', BDD, '2023-01-12 00:46:50'),
                      ('ID1', 'Theorie des langages et de compilation', TLC, '2023-01-07 15:46:50'),
                      ('ID2', 'AI 1 - Machine Learning', ML, '2023-01-12 09:23:50'),
                      ('ID2', 'Big Data 1', BIGDATA, '2023-01-17 10:22:23'),
                      ('GI1', 'RO', RO, '2023-01-08 17:46:50'), ('GI1', 'Langage C avancee', Lc, '2023-01-13 01:09:50'),
                      ('GI2', 'Java avancee', java, '2023-01-16 19:46:50'),
                      ('GI2', 'Python for data science', python, '2023-01-21 15:32:50'),
                      ('GC1', 'Dessin', dessin, '2023-01-19 13:55:17'),
                      ('GC1', 'Topographie', topo, '2023-01-17 20:12:37'),
                      ('GC2', 'RDM 3', RDM, '2023-01-15 19:23:31')]

    # departemenet Data
    columns_departement = ['name']
    data_depertement = [('Département Mathématiques et Informatique',),
                        ('Département Génie Civil Energétique et Environnement',)]
    insert_data("departement", columns_departement, data_depertement)

    # filier data
    columns_filier = ['name', 'description', 'id_departement']
    data_filier = [('ID', 'Ingénierie des données', 1), ('GI', 'Génie Informatique', 1),
                   ('GEER', 'Génie énergétique et énergies renouvelables', 2), ('GC', 'Génie Civil', 2)]
    insert_data("filier", columns_filier, data_filier)

    # emploi_temps data
    columns_time = ['class', 'timetable', 'date_pub']

    with open('timetable/ID1.pdf', 'rb') as f12, \
            open('timetable/ID2.pdf', 'rb') as f13, \
            open('timetable/GI1.pdf', 'rb') as f14, \
            open('timetable/GI2.pdf', 'rb') as f15, \
            open('timetable/GC1.pdf', 'rb') as f16, \
            open('timetable/GC2.pdf', 'rb') as f17, \
            open('timetable/GEER1.pdf', 'rb') as f18, \
            open('timetable/GEER2.pdf', 'rb') as f19:
        ID1 = f12.read()
        ID2 = f13.read()
        GI1 = f14.read()
        GI2 = f15.read()
        GC1 = f16.read()
        GC2 = f17.read()
        GEER1 = f18.read()
        GEER2 = f19.read()
    data_time = [('ID1', ID1, '2023-02-27 08:47:31'),
                 ('ID2', ID2, '2023-02-07 12:25:50'),
                 ('GI1', GI1, '2023-03-09 11:20:17'),
                 ('GI2', GI2, '2023-03-09 11:24:42'),
                 ('GC1', GC1, '2023-03-22 09:48:11'),
                 ('GC2', GC2, '2023-03-22 09:53:24'),
                 ('GEER1', GEER1, '2023-03-27 09:23:47'),
                 ('GEER2', GEER2, '2023-02-13 08:53:09')]

    # class data
    columns_class = ['name_class', 'id_filier']
    data_class = [('ID1', 1),
                  ('ID2', 1),
                  ('GI1', 2),
                  ('GI2', 2),
                  ('GC2', 3),
                  ('GC2', 3),
                  ('GEER1', 4),
                  ('GEER2', 4)]

    # documents data
    with open('documents/ID1/9. PL-SQL.pdf', 'rb') as f20, \
            open('documents/ID1/CoursAnalyseDonne (2).pdf', 'rb') as f21, \
            open('documents/ID1/Formation Data Mining.pdf', 'rb') as f22, \
            open('documents/ID1/La gestion des exceptions.pdf', 'rb') as f23, \
            open('documents/ID1/TP1-ID.pdf', 'rb') as f24, \
            open('documents/ID1/TD TP N° 2.pdf', 'rb') as f25, \
            open('documents/ID1/TD TP N° 3.pdf', 'rb') as f26:
        pl_sql = f20.read()
        sgd = f21.read()
        dm = f22.read()
        ge = f23.read()
        tp1 = f24.read()
        tp2 = f25.read()
        tp3 = f26.read()

    with open('documents/ID2/Java-jee.pdf', 'rb') as f27, \
            open('documents/ID2/ProgrammationWEB avec servlet.pdf', 'rb') as f28, \
            open('documents/ID2/TPJEE.pdf', 'rb') as f29, \
            open('documents/ID2/TPJEEE.pdf', 'rb') as f30:
        java_jee = f27.read()
        servelet = f28.read()
        tp1_jee = f29.read()
        tp2_jee = f30.read()

    with open('documents/GI1/Chapitre 0-Introduction GENERALE.pdf', 'rb') as f31, \
            open('documents/GI1/Chapitre 1-Fonctionnement du Web .pdf', 'rb') as f32, \
            open('documents/GI1/Chapitre 2- HTML5.pdf', 'rb') as f33, \
            open('documents/GI1/TP1.pdf', 'rb') as f34, \
            open('documents/GI1/TP2 (1).pdf', 'rb') as f35:
        WEB_CHP0 = f31.read()
        web_chp1 = f32.read()
        html = f33.read()
        tp1_web = f34.read()
        tp2_web = f35.read()

    with open('documents/GI2/Ccharp.pdf', 'rb') as f36, \
            open('documents/GI2/Introduction sécurité.pdf', 'rb') as f38, \
            open('documents/GI2/TD1 crypto.pdf', 'rb') as f39, \
            open('documents/GI2/TP Ccharp.pdf', 'rb') as f40:
        csharp = f36.read()
        si_chp0 = f38.read()
        td_crypto = f39.read()
        tpcsharp = f40.read()

    columns_doc = ['type', 'titre', 'class', 'file', 'date_doc']
    data_doc1 = [('Cours', 'PL/SQL', 'ID1', pl_sql, '2023-03-28 19:53:09'),
                 ('Cours', 'Data Mining', 'ID1', dm, '2023-03-15 14:19:43'),
                 ('Cours', 'Gestion des Exception', 'ID1', ge, '2023-04-05 20:17:28'),
                 ('TP', 'Le langage SQL', 'ID1', tp2, '2023-03-29 13:28:28')]
    data_doc2 = [('TP', 'Analyse de donnnees avec R', 'ID1', tp1, '2023-04-15 19:28:50'),
                 ('Cours', 'Analyse de donnees', 'ID1', sgd, '2023-03-17 11:28:54'),
                 ('TP', 'PL/SQL instruction de Base', 'ID1', tp3, '2023-04-26 13:34:48'),
                 ('Cours', 'Java/JEE', 'ID2', java_jee, '2023-03-17 12:53:09')]
    data_doc3 = [('Cours', 'Programmation web (SERVLET)', 'ID2', servelet, '2023-03-24 13:12:34'),
                 ('TP', 'TP1 - JEE', 'ID2', tp1_jee, '2023-03-25 14:34:28'),
                 ('TP', 'TP2 - JEE', 'ID2', tp2_jee, '2023-04-01 14:40:11'),
                 ('Cours', 'Ch.0 : Introduction Au WEB', 'GI1', WEB_CHP0, '2023-03-17 12:34:48')]
    data_doc4 = [('Cours', 'Ch.1 : Fonctionnement du WEB ', 'GI1', web_chp1, '2023-03-17 11:53:09'),
                 ('Cours', 'Ch.2 : HTML', 'GI1', html, '2023-03-24 14:12:34'),
                 ('TP', 'TP1 - Notion Du base', 'GI1', tp1_web, '2023-03-25 14:38:28'),
                 ('TP', 'TP2 - HTML', 'GI1', tp2_web, '2023-04-01 15:40:11')]
    data_doc5 = [('Cours', 'Introduction A la securite Informatique', 'GI2', si_chp0, '2023-03-17 19:34:48'),
                 ('TD', 'TD1 : Crypto', 'GI2', td_crypto, '2023-03-18 10:12:34'),
                 ('TP', 'TP1 - C#', 'GI2', tpcsharp, '2023-03-21 00:55:28'),
                 ('Cours', 'Support du Cours : C#', 'GI2', csharp, '2023-03-21 00:50:11')]

    # prof data
    import random
    import string

    # fonction qui generer Un CIN aleatoire
    def generate_code():
        code = random.choice(string.ascii_uppercase)  # Choisissez un caractère aléatoire en majuscule
        code += ''.join(random.choices(string.digits, k=5))  # Ajoutez 5 chiffres aléatoires
        return code

    columns_prof = ['firstname', 'lastname', 'CIN', 'email_prof', 'id_departement']
    data_prof = [('Mohamed', 'ADDAM', generate_code(), 'm.addam@uae.ac.ma', 1),
                 ('younes', 'ABOU EL HANOUNE', generate_code(), 'yabouelhanoune@uae.ac.ma', 1),
                 ('Nabil', 'KANNOUF', generate_code(), 'n.kannouf@uae.ac.ma', 1),
                 ('Tarik', 'BOUDAA', generate_code(), 't.boudaa@uae.ac.ma	', 1),
                 ('Anass', 'ELHADDADI', generate_code(), 'a.elhaddadi@uae.ac.ma', 1),
                 ('Abderrahim', 'BOULANOUAR', generate_code(), 'aboulanouar@uae.ac.ma', 2),
                 ('Ismael', 'Driouch', generate_code(), 'i.driouch@uae.ac.ma', 2),
                 ('Mohamed', 'EL HAIM', generate_code(), 'melhaim@uae.ac.ma', 2),
                 ('Hossain', 'EL OUARGHI', generate_code(), 'helouarghi@uae.ac.ma', 2),
                 ('Abdellatif', 'LAMHAMDI', generate_code(), 'a.lamhamdi@uae.ac.ma', 2)]

    # Student data

    def generate_CNE():
        code = random.choice(string.ascii_uppercase)  # Choisissez un caractère aléatoire en majuscule
        code += ''.join(random.choices(string.digits, k=9))  # Ajoutez 9 chiffres aléatoires
        return code

    columns_std = ['id_Class', 'firstname', 'lastname', 'CIN', 'CNE', 'gender', 'birthday', 'image']
    data_std = [(1, 'ossama', 'outmani', generate_code(), generate_CNE(), 'Male', '2002-12-17', ''),
                (1, 'aymane', 'maghouti', generate_code(), generate_CNE(), 'Male', '2002-07-05', ''),
                (2, 'mahamed', 'tati', generate_code(), generate_CNE(), 'Male', '2000-12-17', ''),
                (2, 'badr', 'jalili', generate_code(), generate_CNE(), 'Male', '2001-01-12', ''),
                (3, 'mohamed', 'najib', generate_code(), generate_CNE(), 'Male', '2001-10-07', ''),
                (3, 'tarik', 'hadaddi', generate_code(), generate_CNE(), 'Male', '2001-05-22', ''),
                (5, 'ossama', 'zitouni', generate_code(), generate_CNE(), 'Male', '2001-11-29', ''),
                (5, 'mohamed', 'boroumi', generate_code(), generate_CNE(), 'Male', '2002-01-19', ''),
                (7, 'yassin', 'azizi', generate_code(), generate_CNE(), 'Male', '2001-09-09', ''),
                (4, 'mohamed', 'elhadadi', generate_code(), generate_CNE(), 'Male', '2000-07-20', ''),
                (6, 'yassin', 'farissi', generate_code(), generate_CNE(), 'M', '2000-06-15', '')]

    # Contact data
    columns_ct = ['id_student', 'adresse1', 'adresse2', 'country', 'city', 'postal_code', 'phone_number',
                  'email_acadymic']

    def phone_number():
        number = "06"
        for i in range(9):
            number += str(random.randint(0, 9))
        return number

    data_ct = [
        (1, 'imzourn,Maroc', 'hayAMN,N_9', 'MAROC', 'Tetouan', '32250', phone_number(), 'ossama.outmani@etu.uae.ac.ma'),
        (2, 'aknoul,taza,Maroc', 'haychouhada,N_67', 'MAROC', 'Aknoul', '53050', phone_number(),
         'aymane.maghouti@etu.uae.ac.ma'),
        (3, 'agadir,Maroc', 'hassan2,N_13', 'MAROC', 'Agadir', '80800', phone_number(), 'mohamed.tati@etu.uae.ac.ma'),
        (4, 'casablanca,Maroc', 'sidiMoumn,N_83', 'MAROC', 'casablanca', '20020', phone_number(),
         'badr.jalilli@etu.uae.ac.ma'),
        (5, 'taroudant,Maroc', 'lmdina,N_17', 'MAROC', 'Taroudant', '83000', phone_number(),
         'mohamed.najib@etu.uae.ac.ma'),
        (6, 'rabat,Maroc', 'centre,N_19', 'MAROC', 'Rabat', '10000', phone_number(), 'hadaddi.tarik@etu.uae.ac.ma'),
        (7, 'errachidia,Maroc', 'lkhawarzmi,N_99', 'MAROC', 'Errachidia', '52000', phone_number(),
         'ossama.zitouni@etu.uae.ac.ma'),
        (8, 'nador,Maroc', 'srwan,N_101', 'MAROC', 'Nador', '62000', phone_number(), 'mahamed.boroumi@etu.uae.ac.ma'),
        (9, 'Rabat,Maroc', 'agdal,N_03', 'MAROC', 'Rabat', '10170', phone_number(), 'yassin.azizi@etu.uae.ac.ma'),
        (10, 'oujda,Maroc', 'Hay El-Andalouss,N_9', 'MAROC', 'Oujda', '60000', phone_number(),
         'mohamed.elhadadi@etu.uae.ac.ma'),
        (11, 'casablanca,Maroc', 'lmaarif,N_9', 'MAROC', 'Casablanca', '20090', phone_number(),
         'yassin.farissi@etu.uae.ac.ma')]

    # bac_student
    columns_bac = ['id_student', 'bac_filier', 'bac_language', 'grid', 'bac_city', 'school_city', 'school_type']
    data_bac = [(1, 'SC Mathematique A', 'French', '17.39', 'Tetouan', 'Tetouan', 'State'),
                (2, 'SC Physique chmie', 'Arabic', '15.27', 'Aknoul', 'Aknoul', 'State'),
                (3, 'SC Physique chmie', 'French', '16.89', 'Agadir', 'Agadir', 'State'),
                (4, 'SC Physique chmie', 'Arabic', '17.43', 'Casablanca', 'Caasblanca', 'State'),
                (5, 'SC Physique chmie', 'Arabic', '17.89', 'Taroudant', 'Taroudant', 'Private'),
                (6, 'SC Mathematique B', 'French', '15.15', 'Rabat', 'Rabat', 'Private'),
                (7, 'SC Physique chmie', 'French', '16.99', 'Errachidia', 'Errachidia', 'State'),
                (8, 'SC Physique chmie', 'Arabic', '17.07', 'Nador', 'Nador', 'State'),
                (9, 'SC Mathematique B', 'French', '14.43', 'Rabat', 'Rabat', 'State'),
                (10, 'SC Physique chmie', 'Arabic', '16.56', 'Oujda', 'Oujda', 'State'),
                (11, 'SC Mathematique A', 'French', '15.97', 'Casablanca', 'Casablanca', 'Private')]

    # filier_student data
    columns_fs = ['id_filier', 'id_student']
    data_fs = [(1, 1),
               (1, 2),
               (1, 3),
               (1, 4),
               (2, 5),
               (2, 6),
               (3, 7),
               (3, 8),
               (4, 9),
               (2, 10),
               (3, 11)]

    # Notification Data
    columns_noti = ['id_filier', 'title', 'detail', 'date_not']
    data_noti = [(1, 'Avis aux élèves ingénieurs ID1',
                  'Il est porté à la connaissance des élèves ingénieurs \nde la première année Ingénieurie des données (ID1) que leDS du module Data Mining aura lieu \nle Jeudi 12/04/2023 à 09h00 à l’amphi A.',
                  '2023-04-02 13:12:34')]

    # Login data

    columns_login = ['id_filier', 'email_acadymic', 'password']
    data_login = [
        ('1', 'ossama.outmani@etu.uae.ac.ma', '69432d34708334dc6088b7b7c76c7304d246575c406cf663a4c5735cceb65d37'),
        ('1', 'aymane.maghouti@etu.uae.ac.ma', '05ca08bbc9acc7aa5080a386226d7b218d806aaab2a7ab8b0e7baf5e531d64ef'),
        ('1', 'mohamed.tati@etu.uae.ac.ma', '17dd58aa247486788375d0b07f2b0369815bf84f67cd3b504183e773e67b9d19'),
        ('1', 'badr.jalilli@etu.uae.ac.ma', '0380948ef6033b0cc26b14288477292429fae6a55dd7f3d676b5124f60828976'),
        ('2', 'mohamed.najib@etu.uae.ac.ma', '17dd58aa247486788375d0b07f2b0369815bf84f67cd3b504183e773e67b9d19'),
        ('2', 'hadaddi.tarik@etu.uae.ac.ma', '5e756bc80813b3dbcf824feb45ad96d6515f854139980ffbb92c2ff5886cea4a'),
        ('3', 'ossama.zitouni@etu.uae.ac.ma', '69432d34708334dc6088b7b7c76c7304d246575c406cf663a4c5735cceb65d37'),
        ('3', 'mahamed.boroumi@etu.uae.ac.ma', '17dd58aa247486788375d0b07f2b0369815bf84f67cd3b504183e773e67b9d19'),
        ('4', 'yassin.azizi@etu.uae.ac.ma', 'e9c45bc9793628c8810a117b4a281886ead1d60a513d988671d532c0e33e8e7c'),
        ('2', 'mohamed.elhadadi@etu.uae.ac.ma', '17dd58aa247486788375d0b07f2b0369815bf84f67cd3b504183e773e67b9d19'),
        ('3', 'yassin.farissi@etu.uae.ac.ma', 'e9c45bc9793628c8810a117b4a281886ead1d60a513d988671d532c0e33e8e7c')]

    insert_data("admin", columns_admin, data_admin)
    insert_data("admin_login", columns_admin_login, data_admin_login)
    insert_data("affichage", columns_affichage, data_affichage)
    insert_data("departement", columns_departement, data_depertement)
    insert_data("filier", columns_filier, data_filier)
    insert_data("emploi_temps", columns_time, data_time)
    insert_data("documents", columns_doc, data_doc1)
    insert_data("documents", columns_doc, data_doc2)
    insert_data("documents", columns_doc, data_doc3)
    insert_data("documents", columns_doc, data_doc4)
    insert_data("documents", columns_doc, data_doc5)
    insert_data("class", columns_class, data_class)
    insert_data("prof", columns_prof, data_prof)
    insert_data("notification", columns_noti, data_noti)

    # insert_data("student", columns_std, data_std)
    # insert_data("contact", columns_ct, data_ct)
    # insert_data("bac_student", columns_bac, data_bac)
    # insert_data("filier_student", columns_fs, data_fs)
    # insert_data("login", columns_login, data_login)
