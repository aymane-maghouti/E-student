import tkinter as tk

from CanvasToWidget import *
from backEndUtilities import connectDB, download_button_click


class StudentGrades:
    def __init__(self):
        self.taskSelected = False
        self.hiddenWidgetsPlaces = []

    def remove(self):
        self.base.studentGradesGroup.removeGroup()

    def createStudentGrades(self, base):

        base.currentFrame = self
        self.base = base
        base.studentGradesTitle = base.Background.create_text(156, 130, text="Grades",
                                                              font=("Montserrat", 20, "bold"), fill="white",
                                                              anchor=tk.NW)

        base.studentGradesImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/studentGradesPage/gradesBackground.png")))

        base.studentGradesFrame = MyScrollableFrame(base.Background, base.studentGradesImg, "#1f1a24", 685, 297, 117,
                                                    174, 20, 20)
        self.show_grades()

        base.studentGradesGroup = MyWidgetsGroup(base.Background, base.studentGradesTitle, base.studentGradesFrame)
        self.hideWidgets = [self.base.studentGradesFrame]

    def show_grades(self):
        mydb, mycursor = connectDB("student_managment")
        mycursor.execute("SELECT class,module,notetable,date_pub FROM affichage order by date_pub desc ")
        result = mycursor.fetchall()

        # Create a canvas and add it to the root window
        canvas = Canvas(self.base.studentGradesFrame.scrollable_frame, width=600, height=500)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create a frame to hold the table
        table_frame = Frame(canvas, background="#1f1a24", width=10)
        table_frame.pack(fill=BOTH, expand=1)

        # Add the table headers
        Label(table_frame, text="Class", width=5, height=2, font=("Montserrat", 12, "bold"), foreground="#bb86fc",
              background="#1f1a24").grid(row=0, column=0)
        Label(table_frame, text="Module", width=30, height=2, font=("Montserrat", 12, "bold"), foreground="#bb86fc",
              background="#1f1a24").grid(row=0, column=1)
        Label(table_frame, text="Download", width=9, height=2, font=("Montserrat", 12, "bold"), foreground="#bb86fc",
              background="#1f1a24").grid(row=0, column=2)
        Label(table_frame, text="Published at", width=15, height=2, font=("Montserrat", 12, "bold"),
              foreground="#bb86fc", background="#1f1a24").grid(row=0, column=3)

        self.downloadStandardIcon = ImageTk.PhotoImage(Image.open(
            self.base.resourcePath("assets/general/downloadStandardIcon.png")))

        # Add the data to the table
        i = 0
        for row in result:
            Label(table_frame, text=row[0], width=5, height=2, font=("Montserrat", 10), foreground="white",
                  background="#1f1a24").grid(row=i + 1, column=0)
            Label(table_frame, text=row[1], width=30, height=2, font=("Montserrat", 10), foreground="white",
                  background="#1f1a24").grid(row=i + 1, column=1)
            downloadButton = tk.Button(table_frame, relief="sunken", borderwidth=0, cursor="hand2",
                                       activebackground="#1f1a24", background="#1f1a24",
                                       image=self.downloadStandardIcon,
                                       command=lambda index=i: download_button_click(index))
            downloadButton.grid(row=i + 1, column=2)
            Label(table_frame, text=row[3], width=15, height=2, font=("Montserrat", 10), foreground="white",
                  background="#1f1a24").grid(row=i + 1, column=3)
            i += 1

    def get_pdf_from_database(self, index):
        conn, cursor = connectDB('student_managment')

        query = "SELECT notetable FROM affichage order by date_pub desc "
        cursor.execute(query)
        rows = cursor.fetchall()
        if index >= len(rows):
            return None

        pdf_content = rows[index][0]
        return pdf_content
