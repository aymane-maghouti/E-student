from CanvasToWidget import *
import tkinter as tk
import re


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


# def signupOnHover(base):
#     base.config(cursor="hand2")
#     base.Background.itemconfig(base.Background.signup, fill="white")
# def signupOnLeave(base):
#     base.config(cursor="arrow")
#     # base.Background.itemconfig(base.Background.signup, fill="white")

class Login:
    def __init__(self):
        self.emailVar=None
        self.emailModified=False
        self.passwordVar=None
        self.passwordModified=False

    def remove(self,base):
        base.loginGroup.removeGroup()
        base.Background.signup.place_forget()
        base.submitLoginButton.place_forget()


    def createLogin(self,base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()
        base.config(cursor="arrow")
        if self.emailVar == None:
            self.emailVar = tk.StringVar(base)
        if self.passwordVar == None:
            self.passwordVar = tk.StringVar(base)


        base.loginWidgetsImg = tk.PhotoImage(
            file=base.resourcePath("assest\loginPage\loginFrame.png"))
        base.loginWidgetsFrame = base.Background.create_image(55, 136, image=base.loginWidgetsImg, anchor=tk.NW)
        base.loginTitle = base.Background.create_text(94, 158, text="Login to your account",
                                                      font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)

        base.signupStandardlImg = Image.open(
            base.resourcePath("assest\loginPage\signupStandardImg.png"))
        base.signupHoverImg = Image.open(
            base.resourcePath("assest\loginPage\signupHoverImg.png"))

        base.Background.signup = MyButton(base.Background, 221, 212,base.signupStandardlImg,hoverImg=base.signupHoverImg,cursor="hand2",behavior=base.loginToRegister1)
        base.notMember = base.Background.create_text(130, 210, text="not a member ?", font=("Montserrat", 7), fill="white",
                                                     anchor=tk.NW)



        # base.Background.tag_bind(base.Background.signup, "<Enter>",
        #                          lambda event: signupOnHover(base))  # event: base.config(cursor="hand2")
        # base.Background.tag_bind(base.Background.signup, "<Leave>", lambda event: signupOnLeave(base))
        # base.Background.tag_bind(base.Background.signup, "<ButtonRelease-1>", lambda event: base.config(cursor="arrow"))
        # base.Background.tag_bind(base.Background.signup, "<Button-1>", lambda event: base.loginToRegister1())

        base.emailLogingStandardlImg = Image.open(base.resourcePath("assest\general\inputLabelImg.png"))
        base.emailLogingHoverImg = Image.open(
            base.resourcePath("assest\general\inputLabelHoveredImg.png"))

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
                                                 placeholder="exemple@etu.uae.ac.ma",modified=self.emailModified,value=self.emailVar)
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

        base.forgot = base.Background.create_text(219, 375, text="Forgot password ?", font=("Montserrat", 10, "underline"),
                                                  fill="#bb86fc", anchor=tk.NW, activefill="white")
        base.Background.tag_bind(base.forgot, "<Enter>", lambda event: base.config(cursor="hand2"))
        base.Background.tag_bind(base.forgot, "<Leave>", lambda event: base.config(cursor="arrow"))
        base.Background.tag_bind(base.forgot, "<Button-1>", lambda event:base.loginToRegister6())

        base.submitLoginButtonImg = Image.open(
            base.resourcePath("assest\loginPage\submitButton.png"))
        base.submitLoginButtonClickedImg = Image.open(
            base.resourcePath("assest\loginPage\submitClicked.png"))
        base.submitLoginButton = MyButton(base.Background, 221, 412, standardImg=base.submitLoginButtonImg,
                                          clickImg=base.submitLoginButtonClickedImg, cursor="hand2",
                                          behavior=base.loginToStudentHome)


        base.loginGroup = MyWidgetsGroup(base.Background, base.loginTitle, base.emailLogingStandardObject,
                                         base.passwordLogingStandardObject, base.forgot, base.notMember,
                                         base.loginWidgetsFrame, base.emailLoginText, base.passwordLoginText)

