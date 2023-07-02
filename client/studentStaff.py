import tkinter as tk

from CanvasToWidget import *
from backEndUtilities import connectDB


class StudentStaff:
    def __init__(self):
        self.taskSelected = False
        self.hiddenWidgetsPlaces = []

    def remove(self):
        self.base.studentStaffGroup.removeGroup()

    def createStudentStaff(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame = self
        self.base = base
        # base.Staff=StudentStaff()
        base.studentStaffTitle = base.Background.create_text(156, 130, text="Staff",
                                                             font=("Montserrat", 20, "bold"), fill="white",
                                                             anchor=tk.NW)

        base.studentStaffImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/studentStaffPage/staffBackground.png")))

        base.studentStaffFrame = MyScrollableFrame(base.Background, base.studentStaffImg, "#1f1a24", 685, 297, 117, 174,
                                                   20, 20)
        # Create a canvas and add it to the root window
        canvas = Canvas(self.base.studentStaffFrame.scrollable_frame, width=685, height=500)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create a frame to hold the self.table
        self.table = Frame(canvas, background="#1f1a24", width=10)
        self.table.pack(fill=BOTH, expand=1)

        self.show_prof()

        base.studentStaffGroup = MyWidgetsGroup(base.Background, base.studentStaffTitle, base.studentStaffFrame)
        self.hideWidgets = [self.base.studentStaffFrame]

    def show_prof(self):
        mydb, mycursor = connectDB("student_managment")
        mycursor.execute(
            "select firstname , lastname , email_prof from prof p , filier f , departement d where f.id_departement = d.id_departement  and p.id_departement = d.id_departement and f.name = %s ",
            (self.base.connectedUser['filiere'],))
        result = mycursor.fetchall()

        # Afficher les données dans un self.tableau tkinter
        Label(self.table, text="First name", font=("Montserrat", 15, "bold"), foreground="#bb86fc",
              background="#1f1a24", width=10, height=2).grid(row=0, column=0)
        Label(self.table, text="Last name", font=("Montserrat", 15, "bold"), foreground="#bb86fc", background="#1f1a24",
              width=15, height=2).grid(row=0, column=1)
        Label(self.table, text="Email ", font=("Montserrat", 15, "bold"), foreground="#bb86fc", background="#1f1a24",
              width=20, height=2).grid(row=0, column=2)
        i = 0
        for row in result:
            Label(self.table, text=row[0], font=("Montserrat", 10), foreground="white", background="#1f1a24", width=20,
                  height=2).grid(row=i + 1, column=0)
            Label(self.table, text=row[1], font=("Montserrat", 10), foreground="white", background="#1f1a24", width=25,
                  height=2).grid(row=i + 1, column=1)
            Label(self.table, text=row[2], font=("Montserrat", 10), foreground="white", background="#1f1a24", width=36,
                  height=2).grid(row=i + 1, column=2)
            i += 1
