from CanvasToWidget import *
import tkinter as tk

class StudentAbout:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]


    def remove(self):
        self.base.studentAboutGroup.removeGroup()

    def createStudentAbout(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        # base.About=StudentAbout()
        base.studentAboutTitle = base.Background.create_text(156, 130, text="About",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.studentAboutImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentAboutPage/aboutBackground.png")))

        base.studentAboutFrame=MyFrame(base.Background,base.studentAboutImg,"orange",685,297,117,174,20,20)

        # base.studentHomeGraphImg =ImageTk.PhotoImage(Image.open(
        #    base.resourcePath("assest/studentHomePage/graphBackground.png")))
        #
        # base.studentAboutGraphFrame=MyFrame(base.Background,base.studentHomeGraphImg,"blue",100,200,117,244,10,10)

        base.studentAboutGroup=MyWidgetsGroup(base.Background,base.studentAboutTitle,base.studentAboutFrame)
        self.hideWidgets=[self.base.studentAboutFrame]
