from CanvasToWidget import *
import tkinter as tk
import os
from tkinter import filedialog
from backEndUtilities import connectDB






class StudentCourses:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]


    def remove(self):
        self.base.studentCoursesGroup.removeGroup()

    def createStudentCourses(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        # base.courses=StudentCourses()
        base.studentCoursesTitle = base.Background.create_text(156, 130, text="Courses",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.studentCoursesImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assets/studentCoursesPage/coursesBackground.png")))

        base.studentCoursesFrame=MyScrollableFrame(base.Background,base.studentCoursesImg,"#1f1a24",685,297,117,174,20,20)
        self.table = Frame(base.studentCoursesFrame.scrollable_frame, width=600, height=500,background="#1f1a24")
        self.table.pack(side=LEFT, fill=BOTH, expand=1)
        self.documents()


        base.studentCoursesGroup=MyWidgetsGroup(base.Background,base.studentCoursesTitle,base.studentCoursesFrame)
        self.hideWidgets=[self.base.studentCoursesFrame]

    def documents(self):
        mydb, mycursor = connectDB("student_managment")
        mycursor.execute("SELECT type,titre,file,date_doc FROM documents where class = %s order by date_doc desc ",
                         (self.base.connectedUser['class'],))
        result = mycursor.fetchall()

        # Créer un canevas pour contenir le self.tableau

        # Ajouter les étiquettes au cadre
        Label(self.table, text="Type", width=5, height=2,font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24").grid(row=0, column=0)
        Label(self.table, text="Title", width=30, height=2,font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24").grid(row=0, column=1)
        Label(self.table, text="Download", width=10, height=2,font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24").grid(row=0, column=2)
        Label(self.table, text="Published at", width=15, height=2,font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24").grid(row=0, column=3)

        self.downloadStandardIcon = ImageTk.PhotoImage(Image.open(
            self.base.resourcePath("assets/general/downloadStandardIcon.png")))

        i=0
        for row in result:
            Label(self.table, text=row[0], width=5, height=2,font=("Montserrat", 10),foreground="white",background="#1f1a24",).grid(row=i + 1, column=0)
            Label(self.table, text=row[1], width=40, height=2,font=("Montserrat", 10),foreground="white",background="#1f1a24",).grid(row=i + 1, column=1)
            downloadButton=tk.Button(self.table,relief="sunken",borderwidth=0,cursor="hand2",activebackground="#1f1a24",background="#1f1a24",image=self.downloadStandardIcon,command=lambda index=i:self.download_button_click(index))
            downloadButton.grid(row=i+1, column=2)
            Label(self.table, text=row[3], width=17, height=2,font=("Montserrat", 10),foreground="white",background="#1f1a24",).grid(row=i + 1, column=3)
            i+=1

    def download_button_click(self,index):
        pdf_content = self.get_pdf_from_database(index)
        if pdf_content is not None:
            self.download_pdf(pdf_content)

    def download_pdf(self,pdf_content):
        # Demander à l'utilisateur de choisir le dossier de destination
        destination_folder = filedialog.askdirectory()

        # Si aucun dossier n'est sélectionné, ne rien faire
        if not destination_folder:
            return

        # Créer un nom de fichier aléatoire avec l'extension .pdf
        import random as rd
        n = rd.randrange(1000000000000000000, 999999999999999999999)
        filename = f"{n}.pdf"

        # Construire le chemin complet du fichier de destination
        destination_file = os.path.join(destination_folder, filename)

        # Écrire le contenu du fichier PDF dans le fichier de destination
        with open(destination_file, "wb") as f:
            f.write(pdf_content)

        # Ouvrir le dossier de destination
        os.startfile(destination_folder)

    def get_pdf_from_database(self,index):
        conn, cursor = connectDB("student_managment")
        query = "SELECT file FROM documents WHERE class = 'id1' order by date_doc desc"
        cursor.execute(query)
        rows = cursor.fetchall()

        if index >= len(rows):
            return None

        pdf_content = rows[index][0]
        return pdf_content

