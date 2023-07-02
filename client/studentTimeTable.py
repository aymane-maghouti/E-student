import os
import tkinter as tk
from tkinter import filedialog

from CanvasToWidget import *
from backEndUtilities import connectDB


def get_pdf_from_database(index):
    conn, cursor = connectDB("student_managment")
    query = "SELECT timetable FROM emploi_temps order by date_pub desc"
    cursor.execute(query)
    rows = cursor.fetchall()

    if index >= len(rows):
        return None

    pdf_content = rows[index][0]
    return pdf_content


def download_pdf(pdf_content):
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


def download_button_click(index):
    pdf_content = get_pdf_from_database(index)
    if pdf_content is not None:
        download_pdf(pdf_content)


class StudentTimeTable:
    def __init__(self):
        self.taskSelected = False
        self.hiddenWidgetsPlaces = []

    def remove(self):
        self.base.studentTimeTableGroup.removeGroup()

    def createStudentTimeTable(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        mydb, mycursor = connectDB("student_managment")
        mycursor.execute("SELECT class,timetable,date_pub FROM emploi_temps order by date_pub desc ")
        result = mycursor.fetchall()

        base.currentFrame = self
        self.base = base
        # base.TimeTable=StudentTimeTable()
        base.studentTimeTableTitle = base.Background.create_text(156, 130, text="TimeTable",
                                                                 font=("Montserrat", 20, "bold"), fill="white",
                                                                 anchor=tk.NW)

        base.studentTimeTableImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/studentTimeTablePage/timeTableBackground.png")))

        base.studentTimeTableFrame = MyScrollableFrame(base.Background, base.studentTimeTableImg, "#1f1a24", 685, 297,
                                                       117, 174, 20, 20)

        # Créer un cadre pour le tableau
        table = Frame(base.studentTimeTableFrame.scrollable_frame, width=600, height=500, background="#1f1a24")
        table.pack(side=LEFT, fill=BOTH, expand=1)

        # Afficher les données dans un tableau tkinter
        Label(table, text="Class", width=5, height=2, font=("Montserrat", 12, "bold"), foreground="#bb86fc",
              background="#1f1a24").grid(row=0, column=0)
        Label(table, text="Download", width=15, height=2, font=("Montserrat", 12, "bold"), foreground="#bb86fc",
              background="#1f1a24").grid(row=0, column=1)
        Label(table, text="Published at", width=20, height=2, font=("Montserrat", 12, "bold"), foreground="#bb86fc",
              background="#1f1a24").grid(row=0, column=2)

        self.downloadStandardIcon = ImageTk.PhotoImage(Image.open(
            self.base.resourcePath("assets/general/downloadStandardIcon.png")))

        i = 0
        for row in result:
            Label(table, text=row[0], width=10, height=2, font=("Montserrat", 10), foreground="white",
                  background="#1f1a24").grid(row=i + 1, column=0)
            downloadButton = tk.Button(table, relief="sunken", borderwidth=0, cursor="hand2",
                                       activebackground="#1f1a24", background="#1f1a24",
                                       image=self.downloadStandardIcon,
                                       command=lambda index=i: download_button_click(index))
            downloadButton.grid(row=i + 1, column=1)
            Label(table, text=row[2], width=20, height=2, font=("Montserrat", 10), foreground="white",
                  background="#1f1a24").grid(row=i + 1, column=2)
            i += 1

        base.studentTimeTableGroup = MyWidgetsGroup(base.Background, base.studentTimeTableTitle,
                                                    base.studentTimeTableFrame)
        self.hideWidgets = [self.base.studentTimeTableFrame]
