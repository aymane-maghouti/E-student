from CanvasToWidget import *
import tkinter as tk

class StudentGrades:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]


    def remove(self):
        self.base.studentGradesGroup.removeGroup()

    def createStudentGrades(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        # base.Grades=StudentGrades()
        base.studentGradesTitle = base.Background.create_text(156, 130, text="Grades",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.studentGradesImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentGradesPage/gradesBackground.png")))

        base.studentGradesFrame=MyScrollableFrame(base.Background,base.studentGradesImg,"purple",685,297,117,174,20,20)

        # base.studentHomeGraphImg =ImageTk.PhotoImage(Image.open(
        #    base.resourcePath("assest/studentHomePage/graphBackground.png")))
        #
        # base.studentGradesGraphFrame=MyFrame(base.Background,base.studentHomeGraphImg,"blue",100,200,117,244,10,10)

        base.studentGradesGroup=MyWidgetsGroup(base.Background,base.studentGradesTitle,base.studentGradesFrame)
        self.hideWidgets=[self.base.studentGradesFrame]
