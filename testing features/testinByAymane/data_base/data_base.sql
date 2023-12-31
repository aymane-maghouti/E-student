create database student_managment;


create table student (
id_student int primary key auto_increment,
firstname varchar(45),
lastname varchar(45),
CIN varchar(45),
CNE varchar(45),
gender varchar(45),
birthday date,
image longBlob
); 


create table bac_student (
id_bac_student int primary key auto_increment,
id_student int not null,
bac_filier varchar(45),
bac_language varchar(45),
grid varchar(45),
bac_city varchar(45),
school_city varchar(45),
school_type varchar(45),
foreign key (id_student) references student(id_student)
);


create table contact (
id_contact int primary key auto_increment,
id_student int not null,
adresse1 varchar(150),
adresse2 varchar(150),
country varchar(45),
city varchar(45),
postal_code varchar(45),
phone_number varchar(45),
email_personel varchar(45),
email_acadymic varchar(45),
foreign key (id_student) references student(id_student)
);

create table departement(
id_departement int primary key auto_increment,
name varchar(45)
);



create table filier(
id_filier int primary key auto_increment,
name varchar(45),
description varchar(200),
id_departement int not null,
foreign key (id_departement) references departement(id_departement)
);


create table login (
id_login int primary key auto_increment,
id_filier int not null,
email_acadymic varchar(45) ,
password varchar(200),
foreign key (id_filier) references filier(id_filier)
);


create table Notification (
id_notification int primary key auto_increment,
id_filier int not null,
title varchar(200),
detail varchar(9999),
date_not datetime,
foreign key (id_filier) references filier(id_filier)
);


create table Admin(
id_admin int primary key auto_increment,
firstname varchar(45),
lastname varchar(45),
CIN varchar(45),
birthday date,
image longBlob,
email_admin varchar(200)
);

create table affichage(
id_affichage int primary key auto_increment,
class varchar(45),
module  varchar(45),
notetable longblob,
date_pub datetime
);
create table emploi_temps(
id_emploi int primary key auto_increment,
class varchar(45),
timetable longblob,
date_pub datetime
);
create table documents(
id_cours int primary key auto_increment,
type varchar(45),
titre varchar(45),
class varchar(45),
file longblob,
date_doc datetime
);

create table prof(
id_prof int primary key auto_increment,
firstname varchar(45),
lastname varchar(45),
CIN varchar(45),
email_prof varchar(200),
id_departement int not null,
foreign key (id_departement) references departement(id_departement)
);


CREATE table filier_student(
id_filier_student int primary key auto_increment,
id_filier int not null,
id_student int not null,
foreign key (id_filier) references filier(id_filier),
foreign key (id_student) references student(id_student)
);

