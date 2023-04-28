from CanvasToWidget import *
import tkinter as tk

class StudentProfile:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]


    def remove(self):
        self.base.studentProfileGroup.removeGroup()

    def createStudentProfile(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        # base.Profile=StudentProfile()
        base.studentProfileTitle = base.Background.create_text(156, 130, text="Profile",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.studentProfileImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentProfilePage/profileBackground.png")))

        base.studentProfileFrame=MyScrollableFrame(base.Background,base.studentProfileImg,"black",685,297,117,174,20,20)

        # base.studentHomeGraphImg =ImageTk.PhotoImage(Image.open(
        #    base.resourcePath("assest/studentHomePage/graphBackground.png")))
        #
        # base.studentProfileGraphFrame=MyFrame(base.Background,base.studentHomeGraphImg,"blue",100,200,117,244,10,10)

        base.studentProfileGroup=MyWidgetsGroup(base.Background,base.studentProfileTitle,base.studentProfileFrame)
        self.hideWidgets=[self.base.studentProfileFrame]
