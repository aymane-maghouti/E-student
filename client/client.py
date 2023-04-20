import threading
import tkinter
import tkinter as tk
import loginCanvas
from PIL import Image,ImageTk
from CanvasToWidget import MyButton
from loginCanvas import Login
from register1Canvas import Register1
from register2Canvas import Register2
from register3Canvas import Register3
from register4Canvas import Register4
import sys,os

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.geometry("915x540+250+100")
        self.overrideredirect(True)
        self.resizable(False, False)
        self.title("test modern app")

        self.wm_attributes('-transparentcolor', '#ab23ff')

        self.login=Login()
        self.r1=Register1()
        self.r2=Register2()
        self.r3=Register3()
        self.r4=Register4()

        #adding the background image to canvas
        self.backImage = tk.PhotoImage(file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\loginBackgroundImg.png")
        self.Background = tk.Canvas(self, width=915, height=540, highlightthickness=0, background="#ab23ff")
        self.Background.create_image(0, 0, image=self.backImage, anchor=tk.NW)
        self.Background.place(x=0,y=0)

        #adding the top header Bar
        self.headerBarImg = tk.PhotoImage(file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\headerBar.png")
        self.headerBarObject=self.Background.create_image(55, 42, image=self.headerBarImg, anchor=tk.NW)

        #adding the moving option to the header bar
        self.Background.tag_bind(self.headerBarObject,"<ButtonPress-1>", self.start_move)
        self.Background.tag_bind(self.headerBarObject,"<ButtonRelease-1>", self.stop_move)
        self.Background.tag_bind(self.headerBarObject,"<B1-Motion>", self.on_move)

        # adding the close button
        self.closeStandardImg = Image.open(r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\closeStandardImg.png").resize((46,46))
        self.closeHoverImg = Image.open(r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\closeHoverImg.png").resize((46,46))
        self.closeButton = MyButton(self.Background,standardImg=self.closeStandardImg,hoverImg=self.closeHoverImg,x=812,y=43,behavior=self.quit)

        self.logoImg = ImageTk.PhotoImage(Image.open(r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\EstudentLogo.png"))
        self.loginObject = self.Background.create_image(79, 51, image=self.logoImg, anchor=tk.NW)

        # create a Toplevel window
        self.loginWidgetsFrame1=self.login.createLogin(self)

        # loginWidgetsImg = tk.PhotoImage(
        #     file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\loginFrame.png")
        # loginWidgetsFrame = self.Background.create_image(55, 136, image=loginWidgetsImg, anchor=tk.NW)

        # loginWidgetsImg =r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\loginFrame.png"
        # base=tk.Canvas(base,width=915,height=540)
        # loginWidgetsFrame = self.Background.create_image(55, 136, image=tk.PhotoImage(file=loginWidgetsImg), anchor=tk.NW)

        # self.loginWidgetsImg = tk.PhotoImage(
        #     file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\loginFrame.png")
        # self.loginWidgetsFrame = self.Background.create_image(55, 136, image=self.loginWidgetsImg, anchor=tk.NW)

    def start_move(self, event):
        self._dragging = True
        self._x = event.x
        self._y = event.y

    def stop_move(self, event):
        self._dragging = False

    def on_move(self, event):
        if self._dragging:
            x = self.winfo_x() + event.x - self._x
            y = self.winfo_y() + event.y - self._y        # self.config(cursor="arrow")

            self.geometry(f"+{x}+{y}")

    def resourcePath(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def loginToRegister1(self):
        self.config(cursor="arrow")
        self.Background.signup.place_forget()
        self.loginGroup.removeGroup()
        self.submitLoginButton.place_forget()
        self.r1.createRegister1(self)


    def register1ToLogin(self):
        self.register1Group.removeGroup()
        self.submitRegister1Button.place_forget()
        self.login.createLogin(self)

    def register1ToRegister2(self):
        # print(self.register1Form.get())
        if self.register1Form.validate():
            self.r1.dayVar=self.dayRegisterList.get()
            self.r1.monthVar=self.monthRegisterList.get()
            self.r1.yearVar=self.yearRegisterList.get()
            self.r1.genderVar=self.genderRegisterOptionList.get()
            print(self.r1.genderVar)
            # print(self.r1.genderVar.getValue())
            self.register1Group.removeGroup()
            self.r2.createRegister2(self)

    def register2ToRegister1(self):
        self.r2.bacCityVar=self.bacCityRegister2List.get()
        self.r2.bacSectorVar=self.bacSectorRegister2List.get()
        self.r2.bacLanguageVar=self.bacLanguageRegister2List.get()
        self.r2.schoolTypeVar = self.hTypeRegisterOptionList.get()

        self.register2Group.removeGroup()
        self.r1.createRegister1(self)

    def register2ToRegister3(self):
        if self.register2Form.validate():
            self.r2.bacCityVar=self.bacCityRegister2List.get()
            self.r2.bacSectorVar=self.bacSectorRegister2List.get()
            self.r2.bacLanguageVar=self.bacLanguageRegister2List.get()
            self.r2.schoolTypeVar=self.hTypeRegisterOptionList.get()

            self.register2Group.removeGroup()
            self.nextRegister2Button.place_forget()
            self.backRegister2Button.place_forget()
            self.r3.createRegister3(self)

    def register3ToRegister2(self):
        self.register3Group.removeGroup()
        self.nextRegister3Button.place_forget()
        self.backRegister3Button.place_forget()
        self.r2.createRegister2(self)

    def register3ToRegister4(self):
        if self.register3Form.validate():
            self.r3.cityVar=self.cityRegister3List.get()
            self.r3.countryVar=self.countryRegister3List.get()


            self.register3Group.removeGroup()
            self.nextRegister3Button.place_forget()
            self.backRegister3Button.place_forget()
            self.r4.createRegister4(self)

    def register4ToRegister3(self):
        self.register4Group.removeGroup()
        self.nextRegister3Button.place_forget()
        self.backRegister3Button.place_forget()
        self.r3.createRegister3(self)







window=App()
window.mainloop()
