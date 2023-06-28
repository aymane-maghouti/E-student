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

        base.adminAboutFrame=MyScrollableFrame(base.Background,base.adminAboutImg,"#1f1a24",685,297,117,174,20,20)

        #Technical
        base.adminAboutTechnicalText=Label(base.adminAboutFrame.scrollable_frame,text="Technical Informations :", font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.adminAboutTechnicalText.grid(row=1,column=0,sticky=W)
        base.adminAboutTechnical="The core of the application is developed from scratch with the Python language (100%)\nNo framework is used, it is pure Python code\nThe application interface is inspired from ENSAH's E-services application"


        Technical_length = len(base.adminAboutTechnical)
        Technical_width = 70
        num_lines = int(Technical_length / Technical_width) + (1 if Technical_length % Technical_width else 0)

        base.Technical = Text(base.adminAboutFrame.scrollable_frame, width=Technical_width, height=num_lines, takefocus=False, font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="white", background="#1f1a24")
        base.Technical.insert(tk.END,f"{base.adminAboutTechnical}")
        base.Technical.grid(row=2,column=0,sticky=W)

        #materials
        base.adminMaterialsText=Label(base.adminAboutFrame.scrollable_frame,text="About Materials :", font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.adminMaterialsText.grid(row=3,column=0,sticky=W)
        base.adminAboutMaterials="Designed with Photopea ,icon by Flaticon "
        Materials_length = len(base.adminAboutMaterials)
        Materials_width = 70
        num_lines = int(Materials_length / Materials_width) + (1 if Materials_length % Materials_width else 0)

        base.Materials = Text(base.adminAboutFrame.scrollable_frame, width=Materials_width, height=num_lines, takefocus=False, font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="white", background="#1f1a24")
        base.Materials.insert(tk.END,f"{base.adminAboutMaterials}")
        base.Materials.grid(row=4,column=0,sticky=W)

        #developers
        base.admindevelopersText=Label(base.adminAboutFrame.scrollable_frame,text="About Developers :", font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.admindevelopersText.grid(row=5,column=0,sticky=W)
        base.adminAboutDevelopers="Ossama Outmani, data engineering student (first year)\nAymane Maghouti, data engineering student (first year)\nNational School of Applied Sciences - Al HOCEIMA\nEmail: ossama.outmani@etu.uae.ac.ma / aymane.maghouti@etu.uae.ac.ma "

        developers_length = len(base.adminAboutDevelopers)
        developers_width = 70
        num_lines = int(developers_length / developers_width) + (1 if developers_length % developers_width else 0)

        base.developers = Text(base.adminAboutFrame.scrollable_frame, width=developers_width, height=num_lines, takefocus=False, font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="white", background="#1f1a24")
        base.developers.insert(tk.END,f"{base.adminAboutDevelopers}")
        base.developers.grid(row=6,column=0,sticky=W)

        #App
        base.adminAppText=Label(base.adminAboutFrame.scrollable_frame,text="App :", font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.adminAppText.grid(row=7,column=0,sticky=W)
        base.adminAboutApp="E-student is an open source desktop app ,you can find the source code via the link:\nhttps://github.com/nexossama/E-student"
        App_length = len(base.adminAboutApp)
        App_width = 70
        num_lines = int(App_length / App_width) + (1 if App_length % App_width else 0)

        base.App = Text(base.adminAboutFrame.scrollable_frame, width=App_width, height=num_lines, takefocus=False, font=("Montserrat", 10, "bold"),
                    relief="flat", foreground="white", background="#1f1a24")
        base.App.insert(tk.END,f"{base.adminAboutApp}")
        base.App.grid(row=8,column=0,sticky=W)






        base.adminAboutGroup=MyWidgetsGroup(base.Background,base.adminAboutTitle,base.adminAboutFrame)
        self.hideWidgets=[self.base.adminAboutFrame]
