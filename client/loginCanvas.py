from CanvasToWidget import *
import tkinter as tk
import re
from backEndUtilities import sign
from tkinter import messagebox
def signUpOnClick(base):
    base.loginToRegister1()
    base.config(cursor="arrow")


def check_email(self):
    pattern = r"^[a-zA-Z0-9]+\.([a-zA-Z0-9]+)+@+etu.uae.ac.ma$"
    if re.match(pattern, self.get()):
        print("matched")
        return True
    print("not Matched")
    return False

def checkLoginForm(self,register):
    try :
        valide=sign(self.components[0].get(),self.components[1].get())
        if valide=="Password Error":
            messagebox.showerror(title="Login Failed", message="Password Error")
            print("password Error")
            return False
        if valide=='Email Error':
            messagebox.showerror(title="Login Failed", message="Email Error")
            return False
        return valide
    except:
        messagebox.showerror(title="Internal error", message="Logging failed")
        return False


class Login:
    def __init__(self):
        self.emailVar=None
        self.emailModified=False
        self.passwordVar=None
        self.passwordModified=False

        self.values=[]


    def remove(self,base):
        base.loginGroup.removeGroup()
        base.Background.signup.place_forget()
        base.submitLoginButton.place_forget()


    def createLogin(self,base):
        base.config(cursor="arrow")
        if self.emailVar == None:
            self.emailVar = tk.StringVar(base)
        if self.passwordVar == None:
            self.passwordVar = tk.StringVar(base)

        self.base=base
        self.base.currentFrame=self

        base.loginWidgetsImg = tk.PhotoImage(
            file=base.resourcePath("assets\loginPage\loginFrame.png"))
        base.loginWidgetsFrame = base.Background.create_image(55, 136, image=base.loginWidgetsImg, anchor=tk.NW)
        base.loginTitle = base.Background.create_text(94, 158, text="Login to your account",
                                                      font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)

        base.signupStandardlImg = Image.open(
            base.resourcePath("assets\loginPage\signupStandardImg.png"))
        base.signupHoverImg = Image.open(
            base.resourcePath("assets\loginPage\signupHoverImg.png"))

        base.Background.signup = MyButton(base.Background, 221, 212,base.signupStandardlImg,hoverImg=base.signupHoverImg,cursor="hand2",behavior=base.loginToRegister1)

        base.forgotStandardlImg = Image.open(
            base.resourcePath("assets\loginPage\\forgotStandardImg.png"))
        base.forgotHoverImg = Image.open(
            base.resourcePath("assets\loginPage\\forgotHoverImg.png"))

        base.Background.forgot = MyButton(base.Background, 219, 375,base.forgotStandardlImg,hoverImg=base.forgotHoverImg,cursor="hand2",behavior=base.loginToForgot)

        base.notMember = base.Background.create_text(130, 210, text="not a member ?", font=("Montserrat", 7), fill="white",
                                                     anchor=tk.NW)



        base.emailLogingStandardlImg = Image.open(base.resourcePath("assets\general\inputLabelImg.png"))
        base.emailLogingHoverImg = Image.open(
            base.resourcePath("assets\general\inputLabelHoveredImg.png"))

        base.emailLoginText = base.Background.create_text(115, 241, text="Email address", font=("Montserrat", 6, "bold"),
                                                          fill="#bb86fc", anchor=tk.NW)
        base.emailLogingEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                         font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                         highlightthickness=0, borderwidth=0, width=36,textvariable=self.emailVar)
        try :
            self.emailModified = base.emailLogingStandardObject.getModified()
        except:
            pass
        base.emailLogingStandardObject = MyEntry(base.Background, 94, 254, entry=base.emailLogingEntry,
                                                 standardImg=base.emailLogingStandardlImg,
                                                 hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                 placeholder="first.last@etu.uae.ac.ma",modified=self.emailModified,value=self.emailVar)
        base.emailLogingStandardObject.validate=lambda:check_email(base.emailLogingStandardObject)

        base.passwordLoginText = base.Background.create_text(115, 315, text="Password", font=("Montserrat", 6, "bold"),
                                                             fill="#bb86fc", anchor=tk.NW)
        base.passwordLogingEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                            font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                            highlightthickness=0, borderwidth=0, width=36,cursor="hand2", show="*",textvariable=self.passwordVar)
        try :
            self.passwordModified = base.passwordLogingStandardObject.getModified()
        except:
            pass
        base.passwordLogingStandardObject = MyEntry(base.Background, 94, 326, entry=base.passwordLogingEntry,
                                                    standardImg=base.emailLogingStandardlImg,
                                                    hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                    placeholder="**********",modified=self.passwordModified,value=self.passwordVar)

        # base.forgot = base.Background.create_text(219, 375, text="Forgot password ?", font=("Montserrat", 10, "underline"),
        #                                           fill="#bb86fc", anchor=tk.NW, activefill="white")
        # base.Background.tag_bind(base.forgot, "<Enter>", lambda event: base.config(cursor="hand2"))
        # base.Background.tag_bind(base.forgot, "<Leave>", lambda event: base.config(cursor="arrow"))
        # base.Background.tag_bind(base.forgot, "<Button-1>", lambda event: base.loginToAdminHome())

        base.loginForm = MyForm(base, base.emailLogingStandardObject, base.passwordLogingStandardObject)
        base.loginForm.validate=lambda:checkLoginForm(base.loginForm,self)
        base.loginForm.get=lambda:self.values


        base.submitLoginButtonImg = Image.open(
            base.resourcePath("assets\loginPage\submitButton.png"))
        base.submitLoginButtonClickedImg = Image.open(
            base.resourcePath("assets\loginPage\submitClicked.png"))
        base.submitLoginButton = MyButton(base.Background, 221, 412, standardImg=base.submitLoginButtonImg,
                                          clickImg=base.submitLoginButtonClickedImg, cursor="hand2",
                                          behavior=base.loginToHome)


        base.loginGroup = MyWidgetsGroup(base.Background, base.loginTitle, base.emailLogingStandardObject,
                                         base.passwordLogingStandardObject, base.notMember,
                                         base.loginWidgetsFrame, base.emailLoginText, base.passwordLoginText)

