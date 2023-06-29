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

        base.studentAboutFrame=MyScrollableFrame(base.Background,base.studentAboutImg,"#1f1a24",685,297,117,174,20,20)

        #Technical
        base.studentAboutTechnicalText=Label(base.studentAboutFrame.scrollable_frame,text="Technical Informations :", font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.studentAboutTechnicalText.grid(row=1,column=0,sticky=W)
        base.studentAboutTechnical="The core of the application is developed from scratch with the Python language (100%)\nNo framework is used, it is pure Python code\nThe application interface is inspired from ENSAH's E-services application"


        Technical_length = len(base.studentAboutTechnical)
        Technical_width = 70
        num_lines = int(Technical_length / Technical_width) + (1 if Technical_length % Technical_width else 0)

        base.Technical = Text(base.studentAboutFrame.scrollable_frame, width=Technical_width, height=num_lines, takefocus=False, font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="white", background="#1f1a24")
        base.Technical.insert(tk.END,f"{base.studentAboutTechnical}")
        base.Technical.grid(row=2,column=0,sticky=W)

        #materials
        base.studentMaterialsText=Label(base.studentAboutFrame.scrollable_frame,text="About Materials :", font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.studentMaterialsText.grid(row=3,column=0,sticky=W)
        base.studentAboutMaterials="Designed with Photopea ,icon by Flaticon "
        Materials_length = len(base.studentAboutMaterials)
        Materials_width = 70
        num_lines = int(Materials_length / Materials_width) + (1 if Materials_length % Materials_width else 0)

        base.Materials = Text(base.studentAboutFrame.scrollable_frame, width=Materials_width, height=num_lines, takefocus=False, font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="white", background="#1f1a24")
        base.Materials.insert(tk.END,f"{base.studentAboutMaterials}")
        base.Materials.grid(row=4,column=0,sticky=W)

        #developers
        base.studentdevelopersText=Label(base.studentAboutFrame.scrollable_frame,text="About Developers :", font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.studentdevelopersText.grid(row=5,column=0,sticky=W)
        base.studentAboutDevelopers="Ossama Outmani, data engineering student (first year)\nAymane Maghouti, data engineering student (first year)\nNational School of Applied Sciences - Al HOCEIMA\nEmail: ossama.outmani@etu.uae.ac.ma / aymane.maghouti@etu.uae.ac.ma "

        developers_length = len(base.studentAboutDevelopers)
        developers_width = 70
        num_lines = int(developers_length / developers_width) + (1 if developers_length % developers_width else 0)

        base.developers = Text(base.studentAboutFrame.scrollable_frame, width=developers_width, height=num_lines, takefocus=False, font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="white", background="#1f1a24")
        base.developers.insert(tk.END,f"{base.studentAboutDevelopers}")
        base.developers.grid(row=6,column=0,sticky=W)

        #App
        base.studentAppText=Label(base.studentAboutFrame.scrollable_frame,text="App :", font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.studentAppText.grid(row=7,column=0,sticky=W)
        base.studentAboutApp="E-student is an open source desktop app ,you can find the source code via the link:\nhttps://github.com/nexossama/E-student"
        App_length = len(base.studentAboutApp)
        App_width = 70
        num_lines = int(App_length / App_width) + (1 if App_length % App_width else 0)

        base.App = Text(base.studentAboutFrame.scrollable_frame, width=App_width, height=num_lines, takefocus=False, font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="white", background="#1f1a24")
        base.App.insert(tk.END,f"{base.studentAboutApp}")
        base.App.grid(row=8,column=0,sticky=W)

        base.studentAboutGroup=MyWidgetsGroup(base.Background,base.studentAboutTitle,base.studentAboutFrame)
        self.hideWidgets=[self.base.studentAboutFrame]
