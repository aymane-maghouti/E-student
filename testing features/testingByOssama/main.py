from tkinter import *
from PIL import Image,ImageTk
from CanvasToWidget import MyButton,MyEntry,MyMenu,MyOption,MyOptionList

def printing():
    print("hello")
class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("850x500+250+100")
        self.overrideredirect(True)
        self.resizable(False,False)
        self.title("test modern app")

        self.wm_attributes('-transparentcolor', '#ab23ff')

        self.config(background="black")
        self.toplevel=Toplevel()
        self.toplevel.geometry("400x200+650+150")
        self.toplevel.wm_attributes('-transparentcolor', '#ab23ff')
        self.toplevel.overrideredirect(True)

        #icon
        appIcon=PhotoImage(file="iris-recognition.png")
        self.iconphoto(False,appIcon)

        # #-------------------------
        # self.Body=Frame(self,width=900,height=600,bg="#d6d6d6")
        # self.Body.pack(padx=20,pady=20)

        #-------------------------background----
        self.backImage=PhotoImage(file="loginscene.png")
        self.Body=Canvas(self,width=850,height=500,highlightthickness=0,background="#ab23ff")
        self.Body.create_image(0,0,image=self.backImage,anchor=NW)
        self.backImage2 = PhotoImage(file="loginscene2.png")
        self.Body2=Canvas(self.toplevel,width=850,height=500,highlightthickness=0,background="#ab23ff")
        self.Body2.create_image(0,0,image=self.backImage2,anchor=NW)
        self.Body2.place(x=0,y=0)

        def mini():
            self.iconify()
        exitButton=MyButton(self.Body,800,10,text="x",standardImg="quitStandard.png",clickImg="quitClicked.png",hoverImg="quitHovered.png",behavior=self.destroy)
        minimizeButton=MyButton(self.Body,780,10,text="x",standardImg="quitStandard.png",clickImg="quitClicked.png",hoverImg="quitHovered.png",behavior=self.iconify)


        # -------------------------email zone---
        # self.loginLabelimage=ImageTk.PhotoImage(Image.open("login zone.png"))
        # self.loginLabel=self.Body.create_image(57, 201, image=self.loginLabelimage, anchor=NW)
        # self.Body.tag_bind(self.loginLabel,"<Enter>",self.emailEnter)
        # self.Body.tag_bind(self.loginLabel, "<Leave>", self.emailLeave)

        #-------------------------email login---
        self.emailLogin=Entry(self.Body,border=0,bg="#1f1a24",fg="white",font=("Montserrat",12,"bold"),width=25,disabledbackground="#1f1a24")
        # self.emailLogin.place(x=75,y=205)
        # self.emailLogin.bind("<Enter>", self.emailEnter)
        # self.emailLogin.bind("<Leave>", self.emailLeave)

        loginLabel=MyEntry(self.Body,self.emailLogin,57,201,"login zone.png","clickedLogin.png",behavior=printing,marginX=15,marginY=5,placeholder="example@etu.uae.ac.ma")

        # -------------------------password zone---
        # self.passwordLabelimage = ImageTk.PhotoImage(Image.open("password zone.png"))
        # self.passwordLabel=self.Body.create_image(57, 280,image=self.passwordLabelimage, anchor=NW)
        # self.Body.tag_bind(self.passwordLabel, "<Enter>", self.passwordEnter)
        # self.Body.tag_bind(self.passwordLabel, "<Leave>", self.passwordLeave)

        # self.passwordLabel=MyButton(self.Body,57,280,"password zone.png","clickedPassword.png",behavior=printing)

        # ------------------------password------
        self.emailPassword = Entry(self.Body, border=0, bg="#1f1a24", fg="white", font=("Montserrat", 12, "bold"),width=25,show="*",disabledbackground="#1f1a24")

        PasswordLabel=MyEntry(self.Body,self.emailPassword,57,280,"login zone.png","clickedLogin.png",behavior=printing,marginX=15,marginY=5,placeholder="exampleexemple")


        # ------------------------signup------
        self.signuptext=Button(self.Body,text="signup",cursor="hand2",relief=SUNKEN,font=("Montserrat",9,"underline"),fg="#bb86fc",bg="#121212",border=0,activebackground="#121212",activeforeground="#dabcff")
        self.signuptext.place(x=166, y=144)

        # ------------------------Forgot Password------
        self.forgotPassText = Button(self.Body ,text="Forgot password ?",cursor="hand2",relief=SUNKEN, font=("Montserrat", 9, "underline"), fg="#bb86fc",bg="#121212", border=0, activebackground="#121212",activeforeground="#dabcff")
        self.forgotPassText.place(x=167, y=325)

        # ------------------------submit2------
        submit2=MyButton(self.Body,166,367,"submitBtn.png","submitLoginHover.png","submitLiginClicked.png",behavior=printing)


        menuEntry=Label(self.Body,text="select",background="#1f1a24",anchor="w",width=7,foreground="white")
        self.dropDown=MyMenu(self.Body,280,140,menuEntry,[self.emailLogin],"DropDback.png","DdownHover.png","menuClicked.png","menuDownClicked.png",width=14,height=4,highlightthickness=0,bd=0,selectbackground="#bb86fc",activestyle="none",options=["ossama","33","44","55","66"])
        self.Body.pack()

        option1=MyOption(self.Body,55,450,"Male",standardImg="optionStandard.png",clickImg="optionClicked.png",entry=True,pady=17,padx=50,text="Male",font=("Montserrat",9,"bold"),fgNotSelected="white",fgSelected="#1f1a24")
        option2=MyOption(self.Body,55,400,"Female",standardImg="optionStandard.png",clickImg="optionClicked.png",entry=True,pady=17,padx=57,text="Female",font=("Montserrat",9,"bold"),fgNotSelected="white",fgSelected="#1f1a24")
        optionsList=MyOptionList([option1,option2])
        option1.setOptionlist(optionsList)
        option2.setOptionlist(optionsList)

        # create a frame to use as the title bar
        self.title_bar = Frame(self.Body, bg="blue",width=200,height=40)
        self.title_bar.place(x=0,y=0)

        # add a label to the title bar
        # self.title_label = Label(self.title_bar, text="Drag Me", bg="gray", fg="white")
        # self.title_label.pack(side=LEFT, padx=5)

        # bind mouse events to the title bar
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_move)
        self.title_bar.bind("<B1-Motion>", self.on_move)

    def start_move(self, event):
        self._dragging = True
        self._x = event.x
        self._y = event.y

    def stop_move(self, event):
        self._dragging = False

    def on_move(self, event):
        if self._dragging:
            x = self.winfo_x() + event.x - self._x
            y = self.winfo_y() + event.y - self._y
            self.geometry(f"+{x}+{y}")


    def clickSubmitLogin(self,event):
        self.submitLoginImage = ImageTk.PhotoImage(Image.open("submitLiginClicked.png"))
        self.submitLoginBtn.config(image=self.submitLoginImage)


    def leaveSubmitLogin(self,event):
        self.submitLoginImage = ImageTk.PhotoImage(Image.open("submitBtn.png"))
        self.submitLoginBtn["image"]=self.submitLoginImage

    def hoverSubmitLogin(self,event):
        self.submitLoginImage = ImageTk.PhotoImage(Image.open("submitLoginHover.png"))
        self.submitLoginBtn["image"]=self.submitLoginImage

    def releaseSubmitLogin(self,event):
        self.submitLoginImage = ImageTk.PhotoImage(Image.open("submitBtn.png"))
        self.submitLoginBtn["image"] = self.submitLoginImage

    def emailEnter(self,event):
        self.loginLabelImage = ImageTk.PhotoImage(Image.open("clickedLogin.png"))
        self.Body.itemconfig(self.loginLabel,image=self.loginLabelImage)

    def emailLeave(self, event):
        self.loginLabelImage = ImageTk.PhotoImage(Image.open("login zone.png"))
        self.Body.itemconfig(self.loginLabel, image=self.loginLabelImage)

    def passwordEnter(self,event):
        self.passwordLabelImage = ImageTk.PhotoImage(Image.open("clickedPassword.png"))
        self.Body.itemconfig(self.passwordLabel,image=self.passwordLabelImage)

    def passwordLeave(self, event):
        self.passwordLabelImage = ImageTk.PhotoImage(Image.open("password zone.png"))
        self.Body.itemconfig(self.passwordLabel, image=self.passwordLabelImage)


win=App()
win.mainloop()