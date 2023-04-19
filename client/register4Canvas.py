from CanvasToWidget import *
import tkinter as tk
import re

def checkEmail(self):
    pattern = r"^[a-zA-Z0-9]+\.([a-zA-Z0-9]+)+@+etu.uae.ac.ma$"
    if re.match(pattern, self.get()):
        print("matched")
        return True
    print("not Matched")
    return False

def passFunction():
    pass
def checkPassword(password, confirm_password):
    # Vérification de la longueur
    if len(password) < 8:
        print("nombre de caractere < 8")
        return False
    # Vérification de la présence d'une lettre majuscule
    if not re.search("[A-Z]", password):
        print("pas de majuscule")
        return False
    # Vérification de la présence d'une lettre minuscule
    if not re.search("[a-z]", password):
        print("pas de minuscule")
        return False
    # Vérification de la présence d'un chiffre
    if not re.search("[0-9]", password):
        print("pas de chiffre")
        return False
    # Vérification de la correspondance des mots de passe
    if password != confirm_password:
        print("password non identique")
        return False
    return True

def getRegisterInfo(self):
    values=[]
    for element in self.components:
            values.append(element.validate())
    print(values)
    return values

def checkRegister4Form(self,base):

    valide=True
    for element in self.components:
        try:
            if not element.validate():
                valide=False
        except Exception as e:
            print(e)

            continue

    print(self.get())
    return valide


class Register4:
    def __init__(self):
        self.emailRegisterVar=None
        self.emailRegisterModified=False
        self.passwordRegisterVar=None
        self.passwordRegisterModified=False
        self.pConfirmationRegisterVar=None
        self.pConfirmationRegisterModified=False

    def createRegister4(self,base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()
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
        base.register4WidgetsImg = tk.PhotoImage(
            file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\register1Page\registerFrame.png")
        base.register4WidgetsFrame = base.Background.create_image(55, 136, image=base.register3WidgetsImg, anchor=tk.NW)
        base.register4Title = base.Background.create_text(94, 158, text="Create your account",
                                                          font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)

        # option menu list
        base.menuRegister2MidStandardlImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionMidStandardImg.png")
        base.menuRegister2MidHoverImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionMidHoverImg.png")

        base.menuRegister2MidClickedImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionMidClickedImg.png")

        base.menuListRegister2MidStandardImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionlistMidStandardImg.png")

        # email
        base.emailRegister4Text = base.Background.create_text(115, 241, text="Email address",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)
        base.emailRegister4Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=36,textvariable=self.emailRegisterVar)
        try :
            self.emailRegisterModified = base.emailRegister4StandardObject.getModified()
        except:
            pass

        base.emailRegister4StandardObject = MyEntry(base.Background, 94, 254, entry=base.emailRegister4Entry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="exemple@etu.uae.ac.ma",modified=self.emailRegisterModified,value=self.emailRegisterVar)
        base.emailRegister4StandardObject.validate=lambda :checkEmail( base.emailRegister4StandardObject)

        # password
        base.passwordRegister4Text = base.Background.create_text(115, 292, text="Password",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)
        base.passwordRegister4Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=36,show="*",textvariable=self.passwordRegisterVar)
        try :
            self.passwordRegisterModified = base.passwordRegister4StandardObject.getModified()
        except:
            pass

        base.passwordRegister4StandardObject = MyEntry(base.Background, 94, 305, entry=base.passwordRegister4Entry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="***********",modified=self.passwordRegisterModified,value=self.passwordRegisterVar)
        base.passwordRegister4StandardObject.validate=lambda :passFunction()

        # password confirmation
        base.confirmRegister4Text = base.Background.create_text(115, 343, text="Confirm password",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)
        base.confirmRegister4Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=36, show="*",textvariable=self.pConfirmationRegisterVar)
        try :
            self.pConfirmationRegisterModified = base.pconfirmRegister4StandardObject.getModified()
        except:
            pass
        base.pconfirmRegister4StandardObject = MyEntry(base.Background, 94, 356, entry=base.confirmRegister4Entry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="***********",modified=self.pConfirmationRegisterModified,value=self.pConfirmationRegisterVar)
        base.pconfirmRegister4StandardObject.validate=lambda :checkPassword(base.passwordRegister4Entry.get(),base.confirmRegister4Entry.get())

        base.register4Form = MyForm(base,base.emailRegister4StandardObject,base.passwordRegister4StandardObject,base.pconfirmRegister4StandardObject)
        base.register4Form.validate=lambda:checkRegister4Form(base.register4Form,base)
        base.registerForm = MyForm(base,base.register1Form,base.register2Form,base.register3Form,base.register4Form)
        base.registerForm.validate=lambda:getRegisterInfo(base.registerForm)



        # next
        base.nextRegister4ButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\nextDisabledButtonImg.png")
        base.nextRegister4Button = MyButton(base.Background, 340, 453, standardImg=base.nextRegister4ButtonImg,
                                            cursor="X_cursor", behavior=lambda :print("hi"))

        # submit
        base.submitRegister4ButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\submitButton.png")
        base.submitRegister4Button = MyButton(base.Background, 221, 453, standardImg=base.submitRegister4ButtonImg,
                                              cursor="hand2",behavior=base.registerForm.validate)

        # back
        base.backRegister4ButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\backButtonStandardImg.png")
        base.backRegister4Button = MyButton(base.Background, 141, 453, standardImg=base.backRegister4ButtonImg,
                                            cursor="hand2", behavior=base.register4ToRegister3)

        base.register4Group = MyWidgetsGroup(base.Background,base.emailRegister4Text,base.passwordRegister4Text,base.confirmRegister4Text, base.emailRegister4StandardObject,base.passwordRegister4StandardObject,base.pconfirmRegister4StandardObject,base.submitRegister4Button)


