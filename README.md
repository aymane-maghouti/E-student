# Student Management System
---

# Table of Contents
---

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Database Configuration](#database-configuration)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [About](#about)
- [Acknowledgments](#acknowledgments)


---

## Project Overview

This is a student management system project built using `Python` and the `Tkinter` library. The application allows students to register, access their personal profile, and download course materials. It also provides an admin space for administrators to manage files, view student information, and upload news. The system utilizes `MySQL` as the database management system and incorporates features such as image validation using `opencv` and visitor tracking. The application is build using  `PyCharm IDEA`.

---
![Texte alternatif de l'image](images/logo.png)
---

## Features

`Student Registration` :student registration after providing the necessary information such as full name, email, image, ...

`Admin Space`: for File Management and News Updates

`Student Space`: for Accessing Course Materials and Personal Profile

`Notification System`: to keep the student up to date for any new news

`Visitor Tracking Graph` : to view the number of visitors per day

---

## Architecture

The application is built using Python and utilizes the Tkinter library for the graphical user interface (GUI). The MySQL database is used as the backend database management system. The system follows a client-server architecture, where the client is the user interface and the server is responsible for interacting with the database (works locally).

We tried to design a detailed architecture of our database, and here is the result:

![Texte alternatif de l'image](images/E_R.png)

---


## Prerequisites

Before running the application, make sure you have the following prerequisites:

`Python` 3.9.x installed 

`MySQL` database installed

The libraries that should be installed are :

`matplotlib` and `scipy` : visualising platform daily access data\
`mysql-connector-python` : connect to MySQL via python\
`numpy`\
`opencv-python` : face detection and auto cropping faces in profile photos\
`Pillow` : for Image handling

Note that if you want to install all this libraries in one click, you just need to execute this command as it is shown [here](#running-the-application)

---

## Database Configuration

To configure the `MySQL database` connection, follow these steps:

Open the project in Pycharm (or just find the config.ini file).
Locate the configuration file named config.ini in the project's client folder.
Open the config.ini file and update the following properties with your MySQL database credentials:

`host` : Specify the host name (default: localhost).

`port` : Specify the port number (default: 3306).

`username` : Enter the MySQL username (default: root).

`password` : Enter the MySQL password (default:).

---

## Running the Application

Clone the repository:

`git clone https://github.com/nexossama/E-student.git`

Install the required dependencies after navigating to the project folder (E-student):

`pip install -r requirements.txt`

you can run the application with two methods: 

`First method` : navigate to the client folder after activating the virtual environment and run the **client.py** script using the terminal.

`Second method`: using Pycharm IDE run the **client.py** manually.

---

## Usage

Before running the E-student app, ensure that the DBMS(DataBase Management system) is turned On. The system itself handles the auto creation of the database if it does not exist ,named **student_managment**.

Upon launching the application, users will be prompted to either log in or register, depending on whether they are an admin or a student. During the registration process, students are required to provide their personal information, including an image of themselves for validation.

After logging in, users will be directed to their respective spaces, where they can perform various actions based on their roles and access levels.

Mainly there are four interface

#### Interface 1 : `Login`

![Texte alternatif de l'image](images/login.png)

#### Interface 2 : `Registration`

![Texte alternatif de l'image](images/registration.png)

#### Interface 3 : `Admin space`

It should be noted that to consult the admin space, you must provide the following email and password:

`Email`: admin2023@gmail.com

`Password`: Admin1234

![Texte alternatif de l'image](images/admin.png)

#### Inerface 4 : `Student space`

![Texte alternatif de l'image](images/student.png)


If you want to see how it's work, check the LinkedIn post where there is a video explaining how to use it, here it is the link of the post [https://www.linkedin.com/oussama]
or this one :
[https://www.linkedin.com/aymane]

---

## About : 
Here is other information on the application and the developers :

![Texte alternatif de l'image](images/about.png)

---

## Acknowledgments
We would like to express our gratitude to the following resources for their valuable contributions to this project:

The official documentation of `Python` language.

The documentation provided by `MySQL` for configuring and working with the database.

The `Tkinter` documentation, which aided in creating the graphical user interface.

`flaticon.com` for providing icons.

`Photopia`  for the application's design


Feel free to customize the content and functionality of this application according to your specific requirements.
