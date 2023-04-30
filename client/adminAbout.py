from CanvasToWidget import *
import tkinter as tk

class AdminAbout:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]


    def remove(self):
        self.base.adminAboutGroup.removeGroup()

    def createAdminAbout(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        base.adminAboutTitle = base.Background.create_text(156, 130, text="About",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.adminAboutImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/adminAboutPage/aboutBackground.png")))

        base.adminAboutFrame=MyFrame(base.Background,base.adminAboutImg,"orange",685,297,117,174,20,20)

        base.adminAboutGroup=MyWidgetsGroup(base.Background,base.adminAboutTitle,base.adminAboutFrame)
        self.hideWidgets=[self.base.adminAboutFrame]
