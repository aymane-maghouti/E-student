from CanvasToWidget import *
import tkinter as tk

class StudentTimeTable:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]


    def remove(self):
        self.base.studentTimeTableGroup.removeGroup()

    def createStudentTimeTable(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        # base.TimeTable=StudentTimeTable()
        base.studentTimeTableTitle = base.Background.create_text(156, 130, text="TimeTable",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.studentTimeTableImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentTimeTablePage/timeTableBackground.png")))

        base.studentTimeTableFrame=MyScrollableFrame(base.Background,base.studentTimeTableImg,"yellow",685,297,117,174,20,20)


        base.studentTimeTableGroup=MyWidgetsGroup(base.Background,base.studentTimeTableTitle,base.studentTimeTableFrame)
        self.hideWidgets=[self.base.studentTimeTableFrame]
