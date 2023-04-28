from CanvasToWidget import *
import tkinter as tk

class StudentStaff:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]


    def remove(self):
        self.base.studentStaffGroup.removeGroup()

    def createStudentStaff(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        # base.Staff=StudentStaff()
        base.studentStaffTitle = base.Background.create_text(156, 130, text="Staff",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.studentStaffImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentStaffPage/staffBackground.png")))

        base.studentStaffFrame=MyScrollableFrame(base.Background,base.studentStaffImg,"green",685,297,117,174,20,20)

        # base.studentHomeGraphImg =ImageTk.PhotoImage(Image.open(
        #    base.resourcePath("assest/studentHomePage/graphBackground.png")))
        #
        # base.studentStaffGraphFrame=MyFrame(base.Background,base.studentHomeGraphImg,"blue",100,200,117,244,10,10)

        base.studentStaffGroup=MyWidgetsGroup(base.Background,base.studentStaffTitle,base.studentStaffFrame)
        self.hideWidgets=[self.base.studentStaffFrame]
