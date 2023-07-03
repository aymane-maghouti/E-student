import re
import tkinter as tk
from tkinter import messagebox

from CanvasToWidget import *


def checkEmail(self):
    pattern = r"^[a-zA-Z0-9]+\.([a-zA-Z0-9]+)+@+etu.uae.ac.ma$"
    if re.match(pattern, self.get()):
        print("matched")
        return True
    messagebox.showerror("Value Error", f"invalid email")
    print("not Matched")
    return False


def passFunction():
    return True


def checkPassword(password, confirm_password):
    # Vérification de la longueur
    if len(password) < 8:
        print("nombre de caractere < 8")
        messagebox.showerror("Value Error", f"invalid password (nb of caracteres less than 8)")
        return False
    # Vérification de la présence d'une lettre majuscule
    if not re.search("[A-Z]", password):
        print("pas de majuscule")
        messagebox.showerror("Value Error", f"invalid password (missing upercase caracteres)")
        return False
    # Vérification de la présence d'une lettre minuscule
    if not re.search("[a-z]", password):
        print("pas de minuscule")
        messagebox.showerror("Value Error", f"invalid password (missing lowercase caracteres)")
        return False
    # Vérification de la présence d'un chiffre
    if not re.search("[0-9]", password):
        print("pas de chiffre")
        messagebox.showerror("Value Error", f"invalid password (missing digits)")
        return False
    # Vérification de la correspondance des mots de passe
    if password != confirm_password:
        print("password non identique")
        messagebox.showerror("Value Error", f"invalid password (failed confirmation)")
        return False
    return True


def getRegisterInfo(base, self):
    values = []
    for element in self.components:
        values.append(element.get())
    print(values)
    print("hi")

    return values


def checkRegister5Form(self, register):
    valide = True
    register.values = []
    for element in self.components:
        if not element.validate():
            valide = False
            break
        register.values.append(element.get())
    print(register.values)
    return valide


class Register5:
    def __init__(self):
        self.emailRegisterVar = None
        self.emailRegisterModified = False
        self.passwordRegisterVar = None
        self.passwordRegisterModified = False
        self.pConfirmationRegisterVar = None
        self.pConfirmationRegisterModified = False

        self.values = []

    def remove(self, base):
        base.register5Group.removeGroup()
        base.submitRegister5Button.place_forget()
        base.nextRegister5Button.place_forget()
        base.backRegister5Button.place_forget()

    def createRegister5(self, base):
        try:
            base.nextRegister3Button.place_forget()
        except:
            pass

        try:
            base.backRegister3Button.place_forget()
        except:
            pass

        if self.emailRegisterVar == None:
            self.emailRegisterVar = tk.StringVar(base)
        if self.passwordRegisterVar == None:
            self.passwordRegisterVar = tk.StringVar(base)
        if self.pConfirmationRegisterVar == None:
            self.pConfirmationRegisterVar = tk.StringVar(base)

        base.config(cursor="arrow")
        base.register5WidgetsImg = tk.PhotoImage(
            file=base.resourcePath("assets\\register1Page\\registerFrame.png"))
        base.register5WidgetsFrame = base.Background.create_image(55, 136, image=base.register5WidgetsImg, anchor=tk.NW)
        base.register5Title = base.Background.create_text(94, 158, text="Create your account",
                                                          font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)

        # option menu list
        base.menuRegister2MidStandardlImg = Image.open(
            base.resourcePath("assets\general\optionMidStandardImg.png"))
        base.menuRegister2MidHoverImg = Image.open(
            base.resourcePath("assets\general\optionMidHoverImg.png"))

        base.menuRegister2MidClickedImg = Image.open(
            base.resourcePath("assets\general\optionMidClickedImg.png"))

        base.menuListRegister2MidStandardImg = Image.open(
            base.resourcePath("assets\general\optionlistMidStandardImg.png"))

        # email
        base.emailRegister5Text = base.Background.create_text(115, 241, text="Email address",
                                                              font=("Montserrat", 6, "bold"),
                                                              fill="#bb86fc", anchor=tk.NW)
        base.emailRegister5Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                            font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                            highlightthickness=0, borderwidth=0, width=36,
                                            textvariable=self.emailRegisterVar)
        try:
            self.emailRegisterModified = base.emailRegister5StandardObject.getModified()
        except:
            pass

        base.emailRegister5StandardObject = MyEntry(base.Background, 94, 254, entry=base.emailRegister5Entry,
                                                    standardImg=base.emailLogingStandardlImg,
                                                    hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                    placeholder="exemple@etu.uae.ac.ma",
                                                    modified=self.emailRegisterModified, value=self.emailRegisterVar)
        base.emailRegister5StandardObject.validate = lambda: checkEmail(base.emailRegister5StandardObject)

        # password
        base.passwordRegister5Text = base.Background.create_text(115, 292, text="Password",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)
        base.passwordRegister5Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=36, show="*",
                                               textvariable=self.passwordRegisterVar)
        try:
            self.passwordRegisterModified = base.passwordRegister5StandardObject.getModified()
        except:
            pass

        base.passwordRegister5StandardObject = MyEntry(base.Background, 94, 305, entry=base.passwordRegister5Entry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="***********",
                                                       modified=self.passwordRegisterModified,
                                                       value=self.passwordRegisterVar)
        base.passwordRegister5StandardObject.validate = lambda: passFunction()

        # password confirmation
        base.confirmRegister5Text = base.Background.create_text(115, 343, text="Confirm password",
                                                                font=("Montserrat", 6, "bold"),
                                                                fill="#bb86fc", anchor=tk.NW)
        base.confirmRegister5Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                              font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                              highlightthickness=0, borderwidth=0, width=36, show="*",
                                              textvariable=self.pConfirmationRegisterVar)
        try:
            self.pConfirmationRegisterModified = base.pconfirmRegister5StandardObject.getModified()
        except:
            pass
        base.pconfirmRegister5StandardObject = MyEntry(base.Background, 94, 356, entry=base.confirmRegister5Entry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="***********",
                                                       modified=self.pConfirmationRegisterModified,
                                                       value=self.pConfirmationRegisterVar)
        base.pconfirmRegister5StandardObject.validate = lambda: checkPassword(base.passwordRegister5Entry.get(),
                                                                              base.confirmRegister5Entry.get())

        base.register5Form = MyForm(base, base.emailRegister5StandardObject, base.passwordRegister5StandardObject,
                                    base.pconfirmRegister5StandardObject)
        base.register5Form.validate = lambda: checkRegister5Form(base.register5Form, self)
        base.register5Form.get = lambda: self.values

        base.registerForm = MyForm(base, base.register1Form, base.register2Form, base.register3Form, base.register4Form,
                                   base.register5Form)
        base.registerForm.get = lambda: getRegisterInfo(base, base.registerForm)

        # next
        base.nextRegister4ButtonImg = Image.open(
            base.resourcePath("assets\general\\nextButtonStandardImg.png"))
        base.nextRegister5Button = MyButton(base.Background, 340, 453, standardImg=base.nextRegister1ButtonImg,
                                            cursor="hand2", behavior=base.register5ToRegister6)

        # submit
        base.submitLoginButtonImg = Image.open(
            base.resourcePath("assets\general\submitDisabledButtonImg.png"))
        base.submitRegister5Button = MyButton(base.Background, 221, 453, standardImg=base.submitLoginButtonImg,
                                              cursor="X_cursor")

        # back
        base.backRegister4ButtonImg = Image.open(
            base.resourcePath("assets\general\\backButtonStandardImg.png"))
        base.backRegister5Button = MyButton(base.Background, 141, 453, standardImg=base.backRegister4ButtonImg,
                                            cursor="hand2", behavior=base.register5ToRegister4)

        base.register5Group = MyWidgetsGroup(base.Background, base.register5WidgetsFrame, base.emailRegister5Text,
                                             base.passwordRegister5Text, base.confirmRegister5Text,
                                             base.emailRegister5StandardObject, base.passwordRegister5StandardObject,
                                             base.pconfirmRegister5StandardObject, base.submitRegister5Button,
                                             base.register5Title)

# l=[['Ossama', 'Outmani', 'L1234', 'P112', 'Male', [2, 'March', 1962]],"[<PIL.Image.Image image mode=RGBA size=100x100 at 0x208E193A550>]",['Tanger', "Sc Mathematique 'B'", 'Spanish', '12', 'Al khawarizmi high school'],['Av masira Nr22 ', 'App3 etage4', '98000', '0689', 'Taza', 'Morocco'],['ossama.outmani@etu.uae.ac.ma', 'Nexos2002', 'Nexos2002']]
