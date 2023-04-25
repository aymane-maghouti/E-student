import mysql.connector

def insert_data(table_name, columns, data):
    cnx = mysql.connector.connect(user='root',
                                   host='localhost',
                                   database='student_managment')
    cursor = cnx.cursor()
    columns_str = ", ".join(columns)
    values_str = ", ".join(["%s"] * len(columns))
    insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
    cursor.executemany(insert_query, data)
    cnx.commit()
    print(f"{cursor.rowcount} rows added")



# ADMIN DATA
with open('admin_image.jpeg', 'rb') as f:
    image_admin = f.read()
columns_admin = ['firstname', 'lastname', 'CIN','birthday','image','email_admin']
data_admin = [('cherradi', 'Mohamed', 'Z12345','1989-01-12',image_admin,'medcherradi00@gmail.com')]



# AFFICHAGE DATA
with open('les notes/BDD.pdf', 'rb') as f1,\
     open('les notes/Theorie des langages et Compilation.pdf', 'rb') as f2,\
     open('les notes/Big data 1.pdf', 'rb') as f3,\
     open('les notes/AI 1- ML- .pdf', 'rb') as f4,\
     open('les notes/RO.pdf', 'rb') as f5,\
     open('les notes/langage C.pdf', 'rb') as f6,\
     open('les notes/Java.pdf', 'rb') as f7,\
     open('les notes/python.pdf', 'rb') as f8,\
     open('les notes/dessin.pdf', 'rb') as f9,\
     open('les notes/Topographie.pdf', 'rb') as f10,\
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
columns_affichage=['class','module','notetable','date_pub']
data_affichage = [('ID1','BDD',BDD,'2023-01-12 00:46:50'),('ID1','Theorie des langages et de compilation',TLC,'2023-01-07 15:46:50'),
    ('ID2','AI 1 - Machine Learning',ML,'2023-01-12 09:23:50'),('ID2','Big Data 1',BIGDATA,'2023-01-17 10:22:23'),
    ('GI1','RO',RO,'2023-01-08 17:46:50'),('GI1','Langage C avancee',Lc,'2023-01-13 01:09:50'),
    ('GI2','Java avancee',java,'2023-01-16 19:46:50'),('GI2','Python for data science',python,'2023-01-21 15:32:50'),
    ('GC1','Dessin',dessin,'2023-01-19 13:55:17'),('GC1','Topographie',topo,'2023-01-17 20:12:37'),
    ('GC2','RDM 3',RDM,'2023-01-15 19:23:31')]


#departemenet Data
columns_departement=['name']
data_depertement=[('Département Mathématiques et Informatique',),('Département Génie Civil Energétique et Environnement',)]

#filier data
columns_filier=['name','description','id_departement']
data_filier=[('ID','Ingénierie des données',1),('GI','Génie Informatique',1),
             ('GEER','Génie énergétique et énergies renouvelables',2),('GC','Génie Civil',2)]


#emploi_temps data
columns_time=['class','timetable','date_pub']

with open('timetable/ID1.pdf', 'rb') as f12,\
     open('timetable/ID2.pdf', 'rb') as f13,\
     open('timetable/GI1.pdf', 'rb') as f14,\
     open('timetable/GI2.pdf', 'rb') as f15,\
     open('timetable/GC1.pdf', 'rb') as f16,\
     open('timetable/GC2.pdf', 'rb') as f17,\
     open('timetable/GEER1.pdf', 'rb') as f18,\
     open('timetable/GEER2.pdf', 'rb') as f19:
    ID1 = f12.read()
    ID2 = f13.read()
    GI1 = f14.read()
    GI2 = f15.read()
    GC1 = f16.read()
    GC2 = f17.read()
    GEER1 = f18.read()
    GEER2 = f19.read()
data_time=[('ID1',ID1,'2023-02-27 08:47:31'),
           ('ID2',ID2,'2023-02-07 12:25:50'),
           ('GI1',GI1,'2023-03-09 11:20:17'),
           ('GI2',GI2,'2023-03-09 11:24:42'),
           ('GC1',GC1,'2023-03-22 09:48:11'),
           ('GC2',GC2,'2023-03-22 09:53:24'),
           ('GEER1',GEER1,'2023-03-27 09:23:47'),
           ('GEER2',GEER2,'2023-02-13 08:53:09')]




#documents data
with open('doc/ID1/9. PL-SQL.pdf', 'rb') as f20,\
     open('doc/ID1/CoursAnalyseDonne (2).pdf', 'rb') as f21,\
     open('doc/ID1/Formation Data Mining.pdf', 'rb') as f22,\
     open('doc/ID1/La gestion des exceptions.pdf', 'rb') as f23,\
     open('doc/ID1/TP1-ID.pdf', 'rb') as f24,\
     open('doc/ID1/TD TP N° 2.pdf', 'rb') as f25,\
     open('doc/ID1/TD TP N° 3.pdf', 'rb') as f26 :
    pl_sql = f20.read()
    sgd = f21.read()
    dm = f22.read()
    ge = f23.read()
    tp1 = f24.read()
    tp2 = f25.read()
    tp3 = f26.read()

with open('doc/ID2/Java-jee.pdf', 'rb') as f27,\
     open('doc/ID2/ProgrammationWEB avec servlet.pdf', 'rb') as f28,\
     open('doc/ID2/TPJEE.pdf', 'rb') as f29,\
     open('doc/ID2/TPJEEE.pdf', 'rb') as f30 :
    java_jee=f27.read()
    servelet = f28.read()
    tp1_jee = f29.read()
    tp2_jee =  f30.read()

with open('doc/GI1/Chapitre 0-Introduction GENERALE.pdf', 'rb') as f31,\
     open('doc/GI1/Chapitre 1-Fonctionnement du Web .pdf', 'rb') as f32,\
     open('doc/GI1/Chapitre 2- HTML5.pdf', 'rb') as f33,\
     open('doc/GI1/TP1.pdf', 'rb') as f34,\
     open('doc/GI1/TP2 (1).pdf', 'rb') as f35 :
    WEB_CHP0 = f31.read()
    web_chp1 = f32.read()
    html = f33.read()
    tp1_web = f34.read()
    tp2_web = f35.read()

with open('doc/GI2/Ccharp.pdf', 'rb') as f36, \
        open('doc/GI2/Cours TypeScript-1.pdf', 'rb') as f37, \
        open('doc/GI2/Introduction sécurité.pdf', 'rb') as f38, \
        open('doc/GI2/TD1 crypto.pdf', 'rb') as f39, \
        open('doc/GI2/TP Ccharp.pdf', 'rb') as f40:
    csharp = f36.read()
    ts_chp0 = f37.read()
    si_chp0 = f38.read()
    td_crypto = f39.read()
    tpcsharp = f40.read()



columns_doc = ['type','titre','class','file','date_doc']
data_doc = [('Cours','PL/SQL','ID1',pl_sql,'2023-03-28 19:53:09'),
            ('Cours','Data Mining','ID1',dm,'2023-03-15 14:19:43'),
            ('Cours','Gestion des Exception','ID1',ge,'2023-04-05 20:17:28'),
            ('TP','Le langage SQL','ID1',tp2,'2023-03-29 13:28:28'),
            ('TP','Analyse de donnnees avec R','ID1',tp1,'2023-04-15 19:28:50'),
            ('Cours','Analyse de donnees','ID1',sgd,'2023-03-17 11:28:54'),
            ('TP','PL/SQL instruction de Base','ID1',tp3,'2023-04-26 13:34:48'),
            ('Cours', 'Java/JEE', 'ID2', java_jee, '2023-03-17 12:53:09'),
            ('Cours', 'Programmation web (SERVLET)', 'ID2', servelet, '2023-03-24 13:12:34'),
            ('TP', 'TP1 - JEE', 'ID2', tp1_jee, '2023-03-25 14:34:28'),
            ('TP', 'TP2 - JEE', 'ID2', tp2_jee, '2023-04-01 14:40:11'),
            ('Cours','Ch.0 : Introduction Au WEB','GI1',WEB_CHP0,'2023-03-17 12:34:48'),
            ('Cours', 'Ch.1 : Fonctionnement du WEB ', 'GI1', web_chp1, '2023-03-17 11:53:09'),
            ('Cours', 'Ch.2 : HTML', 'GI1', html, '2023-03-24 14:12:34'),
            ('TP', 'TP1 - Notion Du base', 'GI1', tp1_web, '2023-03-25 14:38:28'),
            ('TP', 'TP2 - HTML', 'GI1', tp2_web, '2023-04-01 15:40:11'),
            ('Cours','Introduction A la securite Informatique','GI2',si_chp0,'2023-03-17 19:34:48'),
            ('TD', 'TD1 : Crypto', 'GI2', td_crypto, '2023-03-18 10:12:34'),
            ('TP', 'TP1 - C#', 'GI2', tpcsharp, '2023-03-21 00:55:28'),
            ('Cours', 'Support du Cours : C#', 'GI2', csharp, '2023-03-21 00:50:11')]



#prof data
import random
import string

#fonction qui generer Un CIN aleatoire
def generate_code():
    code = random.choice(string.ascii_uppercase) # Choisissez un caractère aléatoire en majuscule
    code += ''.join(random.choices(string.digits, k=5)) # Ajoutez 5 chiffres aléatoires
    return code
columns_prof =['firstname','lastname','CIN','email_prof','id_departement']
data_prof=[('Mohamed','ADDAM',generate_code(),'m.addam@uae.ac.ma',1),
           ('younes','ABOU EL HANOUNE',generate_code(),'yabouelhanoune@uae.ac.ma',1),
           ('Nabil','KANNOUF',generate_code(),'n.kannouf@uae.ac.ma',1),
           ('Tarik','BOUDAA',generate_code(),'t.boudaa@uae.ac.ma	',1),
           ('Anass','ELHADDADI',generate_code(),'a.elhaddadi@uae.ac.ma',1),
           ('Abderrahim','BOULANOUAR',generate_code(),'aboulanouar@uae.ac.ma',2),
           ('Ismael','Driouch',generate_code(),'i.driouch@uae.ac.ma',2),
           ('Mohamed','EL HAIM',generate_code(),'melhaim@uae.ac.ma',2),
           ('Hossain','EL OUARGHI',generate_code(),'helouarghi@uae.ac.ma',2),
           ('Abdellatif','LAMHAMDI',generate_code(),'a.lamhamdi@uae.ac.ma',2)]


#Student data

def generate_CNE():
    code = random.choice(string.ascii_uppercase) # Choisissez un caractère aléatoire en majuscule
    code += ''.join(random.choices(string.digits, k=9)) # Ajoutez 9 chiffres aléatoires
    return code
with open('image_student/ID1_S1 .jpg', 'rb') as i1,\
     open('image_student/ID1_S2.jpg', 'rb') as i2,\
     open('image_student/ID2_S1.jpg', 'rb') as i3, \
     open('image_student/ID2_S2.jpg', 'rb') as i4, \
     open('image_student/GI1_S1.jpg', 'rb') as i5, \
     open('image_student/GI1_S2.jpg', 'rb') as i6, \
     open('image_student/GC1_S1.jpg', 'rb') as i7, \
     open('image_student/GC1_S2.jpg', 'rb') as i8, \
     open('image_student/GEER1.jpg', 'rb') as i9, \
     open('image_student/GI2.jpg', 'rb') as i10, \
     open('image_student/GC2.jpg', 'rb') as i11:
    id1s1 = i1.read()
    id1s2 = i2.read()
    id2s1 = i3.read()
    id2s2 = i4.read()
    gi1s1 = i5.read()
    gi1s2 = i6.read()
    gc1s1 = i7.read()
    gc1s2 = i8.read()
    geer1 = i9.read()
    gi2 = i10.read()
    gc2 = i11.read()
columns_std=['firstname','lastname','CIN','CNE','gender','birthday','image']
data_std=[('ossama','outmani',generate_code(),generate_CNE(),'M','2002-12-17',id1s1),
          ('aymane','maghouti',generate_code(),generate_CNE(),'M','2002-07-05',id1s2),
          ('mahamed','tati',generate_code(),generate_CNE(),'M','2000-12-17',id2s1),
          ('badr','jalili',generate_code(),generate_CNE(),'M','2001-01-12',id2s2),
          ('mohamed','najib',generate_code(),generate_CNE(),'M','2001-10-07',gi1s1),
          ('tarik','hadaddi',generate_code(),generate_CNE(),'M','2001-05-22',gi1s2),
          ('ossama','zitouni',generate_code(),generate_CNE(),'M','2001-11-29',gc1s1),
          ('mohamed','boroumi',generate_code(),generate_CNE(),'M','2002-01-19',gc1s2),
          ('yassin','azizi',generate_code(),generate_CNE(),'M','2001-09-09',geer1),
          ('mohamed','elhadadi',generate_code(),generate_CNE(),'M','2000-07-20',gi2),
          ('yassin','farissi',generate_code(),generate_CNE(),'M','2000-06-15',gc2)]







#Contact data
columns_ct = ['id_student','adresse1','adresse2','country','city','postal_code','phone_number','email_personel','email_acadymic']
def phone_number():
    number = "06"
    for i in range(9):
        number += str(random.randint(0, 9))
    return number

data_ct=[(1,'imzourn,Maroc','hayAMN,N_9','MAROC','Tetouan','32250',phone_number(),'ossamaoutmani@gmail.com','ossama.outmani@etu.uae.ac.ma'),
         (2,'aknoul,taza,Maroc','haychouhada,N_67','MAROC','Aknoul','53050',phone_number(),'aymanemaghouti@gmail.com','aymane.maghouti@etu.uae.ac.ma'),
         (3,'agadir,Maroc','hassan2,N_13','MAROC','Agadir','80800',phone_number(),'medtati@gmail.com','mohamed.tati@etu.uae.ac.ma'),
         (4,'casablanca,Maroc','sidiMoumn,N_83','MAROC','casablanca','20020',phone_number(),'badrjalilli@gmail.com','badr.jalilli@etu.uae.ac.ma'),
         (5,'taroudant,Maroc','lmdina,N_17','MAROC','Taroudant','83000',phone_number(),'najibMed@gmail.com','mohamed.najib@etu.uae.ac.ma'),
         (6,'rabat,Maroc','centre,N_19','MAROC','Rabat','10000',phone_number(),'tarikhadaddi@gmail.com','hadaddi.tarik@etu.uae.ac.ma'),
         (7, 'errachidia,Maroc', 'lkhawarzmi,N_99', 'MAROC', 'Errachidia', '52000', phone_number(), 'ossamazitouni@gmail.com','ossama.zitouni@etu.uae.ac.ma'),
         (8, 'nador,Maroc', 'srwan,N_101', 'MAROC', 'Nador', '62000', phone_number(), 'medboroumi@gmail.com','mahamed.boroumi@etu.uae.ac.ma'),
         (9, 'Rabat,Maroc', 'agdal,N_03', 'MAROC', 'Rabat', '10170', phone_number(), 'yassinazizi@gmail.com','yassin.azizi@etu.uae.ac.ma'),
         (10, 'oujda,Maroc', 'Hay El-Andalouss,N_9', 'MAROC', 'Oujda', '60000', phone_number(), 'medelhadadi@gmail.com','mohamed.elhadadi@etu.uae.ac.ma'),
         (11, 'casablanca,Maroc', 'lmaarif,N_9', 'MAROC', 'Casablanca', '20090', phone_number(), 'yassinfarissi@gmail.com','yassin.farissi@etu.uae.ac.ma')]



#bac_student
columns_bac=['id_student','bac_filier','bac_language','grid','bac_city','school_city','school_type']
data_bac=[(1,'SC Mathematique A','French','17.39','Tetouan','Tetouan','State'),
          (2,'SC Physique chmie','Arabic','15.27','Aknoul','Aknoul','State'),
          (3,'SC Physique chmie','French','16.89','Agadir','Agadir','State'),
          (4,'SC Physique chmie','Arabic','17.43','Casablanca','Caasblanca','State'),
          (5,'SC Physique chmie','Arabic','17.89','Taroudant','Taroudant','Private'),
          (6,'SC Mathematique B','French','15.15','Rabat','Rabat','Private'),
          (7,'SC Physique chmie','French','16.99','Errachidia','Errachidia','State'),
          (8,'SC Physique chmie','Arabic','17.07','Nador','Nador','State'),
          (9,'SC Mathematique B','French','14.43','Rabat','Rabat','State'),
          (10,'SC Physique chmie','Arabic','16.56','Oujda','Oujda','State'),
          (11,'SC Mathematique A','French','15.97','Casablanca','Casablanca','Private')]



#filier_student data
columns_fs=['id_filier','id_student']
data_fs=[(1,1),
         (1,2),
         (1,3),
         (1,4),
         (2,5),
         (2,6),
         (3,7),
         (3,8),
         (4,9),
         (2,10),
         (3,11)]


#Notification Data
columns_noti = ['id_filier','title','detail','date_not']
data_noti=[(1,'Avis aux élèves ingénieurs ID1','Il est porté à la connaissance des élèves ingénieurs \nde la première année Ingénieurie des données (ID1) que leDS du module Data Mining aura lieu \nle Jeudi 12/04/2023 à 09h00 à l’amphi A.','2023-04-02 13:12:34')]


#Login data

columns_login=['id_filier','email_acadymic','password']
data_login=[('1','ossama.outmani@etu.uae.ac.ma','69432d34708334dc6088b7b7c76c7304d246575c406cf663a4c5735cceb65d37'),
            ('1','aymane.maghouti@etu.uae.ac.ma','05ca08bbc9acc7aa5080a386226d7b218d806aaab2a7ab8b0e7baf5e531d64ef'),
            ('1','mohamed.tati@etu.uae.ac.ma','17dd58aa247486788375d0b07f2b0369815bf84f67cd3b504183e773e67b9d19'),
            ('1','badr.jalilli@etu.uae.ac.ma','0380948ef6033b0cc26b14288477292429fae6a55dd7f3d676b5124f60828976'),
            ('2','mohamed.najib@etu.uae.ac.ma','17dd58aa247486788375d0b07f2b0369815bf84f67cd3b504183e773e67b9d19'),
            ('2','hadaddi.tarik@etu.uae.ac.ma','5e756bc80813b3dbcf824feb45ad96d6515f854139980ffbb92c2ff5886cea4a'),
            ('3','ossama.zitouni@etu.uae.ac.ma','69432d34708334dc6088b7b7c76c7304d246575c406cf663a4c5735cceb65d37'),
            ('3','mahamed.boroumi@etu.uae.ac.ma','17dd58aa247486788375d0b07f2b0369815bf84f67cd3b504183e773e67b9d19'),
            ('4','yassin.azizi@etu.uae.ac.ma','e9c45bc9793628c8810a117b4a281886ead1d60a513d988671d532c0e33e8e7c'),
            ('2','mohamed.elhadadi@etu.uae.ac.ma','17dd58aa247486788375d0b07f2b0369815bf84f67cd3b504183e773e67b9d19'),
            ('3','yassin.farissi@etu.uae.ac.ma','e9c45bc9793628c8810a117b4a281886ead1d60a513d988671d532c0e33e8e7c')]


#call function
insert_data("admin", columns_admin, data_admin)


