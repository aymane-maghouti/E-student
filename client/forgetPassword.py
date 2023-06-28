from CanvasToWidget import *
import tkinter as tk
import re
from backEndUtilities import connectDB,hash_password

def checkEmail(self):
    pattern = r"^[a-zA-Z0-9]+\.([a-zA-Z0-9]+)+@+etu.uae.ac.ma$"
    if re.match(pattern, self.get()):
        print("matched")
        return True
    print("not Matched")
    return False

def passFunction():
    return True
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

def getRegisterInfo(base,self):
    values=[]
    for element in self.components:
            values.append(element.get())
    print(values)
    print("hi")

    return values

def checkForgotForm(self,register):

    valide=True
    register.values=[]
    for element in self.components:
        if not element.validate():
            valide=False
        register.values.append(element.get())
    print(register.values)
    return valide






class Forgot:
    def __init__(self):
        self.emailRegisterVar=None
        self.emailRegisterModified=False
        self.passwordRegisterVar=None
        self.passwordRegisterModified=False
        self.pConfirmationRegisterVar=None
        self.pConfirmationRegisterModified=False

        self.values=[]

    def remove(self,base):
        base.forgotGroup.removeGroup()
        base.submitForgotButton.place_forget()


    def createForgot(self,base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        self.base=base
        if self.emailRegisterVar == None:
            self.emailRegisterVar = tk.StringVar(base)
        if self.passwordRegisterVar == None:
            self.passwordRegisterVar = tk.StringVar(base)
        if self.pConfirmationRegisterVar == None:
            self.pConfirmationRegisterVar = tk.StringVar(base)

        base.currentFrame=self
        base.config(cursor="arrow")
        base.ForgotWidgetsImg = tk.PhotoImage(
            file=base.resourcePath("assest\\register1Page\\registerFrame.png"))
        base.ForgotWidgetsFrame = base.Background.create_image(55, 136, image=base.ForgotWidgetsImg, anchor=tk.NW)
        base.ForgotTitle = base.Background.create_text(94, 158, text="Forgot Password",
                                                          font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)


        # email
        base.emailForgotText = base.Background.create_text(115, 241, text="Email address",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)
        base.emailForgotEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=36,textvariable=self.emailRegisterVar)
        try :
            self.emailRegisterModified = base.emailForgotStandardObject.getModified()
        except:
            pass

        base.emailForgotStandardObject = MyEntry(base.Background, 94, 254, entry=base.emailForgotEntry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="fname.lname@etu.uae.ac.ma",modified=self.emailRegisterModified,value=self.emailRegisterVar)
        base.emailForgotStandardObject.validate=lambda :checkEmail( base.emailForgotStandardObject)

        # password
        base.passwordForgotText = base.Background.create_text(115, 292, text="New Password",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)
        base.passwordForgotEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=36,show="*",textvariable=self.passwordRegisterVar)
        try :
            self.passwordRegisterModified = base.passwordForgotStandardObject.getModified()
        except:
            pass

        base.passwordForgotStandardObject = MyEntry(base.Background, 94, 305, entry=base.passwordForgotEntry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="***********",modified=self.passwordRegisterModified,value=self.passwordRegisterVar)
        base.passwordForgotStandardObject.validate=lambda :passFunction()

        # password confirmation
        base.confirmForgotText = base.Background.create_text(115, 343, text="Confirm New Password",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)
        base.confirmForgotEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=36, show="*",textvariable=self.pConfirmationRegisterVar)
        try :
            self.pConfirmationRegisterModified = base.pconfirmForgotStandardObject.getModified()
        except:
            pass
        base.pconfirmForgotStandardObject = MyEntry(base.Background, 94, 356, entry=base.confirmForgotEntry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="***********",modified=self.pConfirmationRegisterModified,value=self.pConfirmationRegisterVar)
        base.pconfirmForgotStandardObject.validate=lambda :checkPassword(base.passwordForgotEntry.get(),base.confirmForgotEntry.get())

        base.forgotForm = MyForm(base,base.emailForgotStandardObject,base.passwordForgotStandardObject,base.pconfirmForgotStandardObject)
        base.forgotForm.validate=lambda:checkForgotForm(base.forgotForm,self)
        base.forgotForm.get=lambda:self.values




        # submit
        base.submitLoginButtonImg = Image.open(
            base.resourcePath("assest/loginPage/submitButton.png"))
        base.submitForgotButton = MyButton(base.Background, 221, 453, standardImg=base.submitLoginButtonImg,
                                              cursor="hand2",behavior=self.forget)


        base.forgotGroup = MyWidgetsGroup(base.Background,base.ForgotWidgetsFrame,base.emailForgotText,base.passwordForgotText,base.confirmForgotText, base.emailForgotStandardObject,base.passwordForgotStandardObject,base.pconfirmForgotStandardObject,base.ForgotTitle)

    def forget(self):
        if self.base.forgotForm.validate():
            conn, mycursor = connectDB('student_managment')

            mycursor.execute("SELECT email_acadymic FROM login")
            results = mycursor.fetchall()
            email=self.base.forgotForm.get()[0]
            emails = [result[0] for result in results]
            if email in emails:
                new_password = self.base.forgotForm.get()[1]
                print('the new password is ', new_password)
                new_password_hashed = hash_password(new_password)
                print(new_password_hashed)
                sql = "UPDATE login SET password = %s WHERE email_acadymic =  %s"
                values = (new_password_hashed, email)
                mycursor.execute(sql, values)
                conn.commit()
                self.base.onLogoClick()
                print("password changed")
                return 'password changed'

            else:
                print("Email not found ")
                return 'Email Error'


# l=[['Ossama', 'Outmani', 'L1234', 'P112', 'Male', [2, 'March', 1962]],"[<PIL.Image.Image image mode=RGBA size=100x100 at 0x208E193A550>]",['Tanger', "Sc Mathematique 'B'", 'Spanish', '12', 'Al khawarizmi high school'],['Av masira Nr22 ', 'App3 etage4', '98000', '0689', 'Taza', 'Morocco'],['ossama.outmani@etu.uae.ac.ma', 'Nexos2002', 'Nexos2002']]