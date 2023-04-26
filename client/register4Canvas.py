from CanvasToWidget import *
import tkinter as tk

def checkLenght(self,size,labelName="entry"):
    size=20
    if len(self.get())>size or len(self.get())<0 :#remake it 0
        print(f"invalide {labelName}")
        return False
    print(f"valide {labelName}")
    return True

def checkPhone(self,size,labelName="entry"):
    try:
        value=float(self.get())
    except:
        print(f"invalide {labelName}")
        return False

    if len(self.get())>size or len(self.get())<1 :#remake it 0
        print(f"invalide {labelName}")
        return False
    print(f"valide {labelName}")
    return True


def checkListChoice(self,choice,optionName="option"):
    if self.get()==choice:
        print(f"invalide {optionName}")
        return False
    print(f"valide {optionName}")
    return True

def checkPostal(self,labelName="entry"):
    try:
        value=float(self.get())
    except:
        print(f"invalide {labelName}")
        return False
    if 0<=value<=99999:
        print(f"valide {labelName}")
        return True
    print(f"invalide {labelName}")
    return False


def checkRegister4Form(self,register):
    valide=True
    register.values=[]
    for element in self.components:
        try:
            if not element.validate():
                valide=False
        except Exception as e:
            print(e)

            continue
        register.values.append(element.get())
    print(register.values)
    return valide

class Register4:
    def __init__(self):
        self.address1Var=None
        self.address1Modified=False
        self.address2Var=None
        self.address2Modified=False
        self.postalCodeVar=None
        self.postalCodeModified=False
        self.phoneVar=None
        self.phoneModified=False

        self.cityVar=None
        self.countryVar=None

        self.values=[]

    def remove(self,base):
        base.register4Group.removeGroup()
        base.submitRegister4Button.place_forget()
        base.nextRegister4Button.place_forget()
        base.backRegister4Button.place_forget()

    def createRegister4(self,base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()
        try:
            base.nextRegister2Button.place_forget()
        except:
            pass

        try:
            base.backRegister4Button.place_forget()
        except:
            pass
        try:
            base.backRegister2Button.place_forget()
        except:
            pass

        try:
            base.nextRegister4Button.place_forget()
        except:
            pass

        if self.address1Var == None:
            self.address1Var = tk.StringVar(base)
        if self.address2Var == None:
            self.address2Var = tk.StringVar(base)
        if self.postalCodeVar == None:
            self.postalCodeVar = tk.StringVar(base)
        if self.phoneVar == None:
            self.phoneVar = tk.StringVar(base)

        base.config(cursor="arrow")
        base.register4WidgetsImg = tk.PhotoImage(
            file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\register1Page\registerFrame.png")
        base.register4WidgetsFrame = base.Background.create_image(55, 136, image=base.register4WidgetsImg, anchor=tk.NW)
        base.register4Title = base.Background.create_text(94, 158, text="Create your account",
                                                          font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)

        # option menu list
        base.menuRegister2MidStandardlImg = Image.open(
            base.resourcePath("assest\general\optionMidStandardImg.png"))
        base.menuRegister2MidHoverImg = Image.open(
            base.resourcePath("assest\general\optionMidHoverImg.png"))

        base.menuRegister2MidClickedImg = Image.open(
            base.resourcePath("assest\general\optionMidClickedImg.png"))

        base.menuListRegister2MidStandardImg = Image.open(
            base.resourcePath("assest\general\optionlistMidStandardImg.png"))

        # address line 1
        base.address1Register4Text = base.Background.create_text(115, 241, text="Address Line 1",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)
        base.address1Register4Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=36,textvariable=self.address1Var)
        try :
            self.address1Modified = base.address1Register4StandardObject.getModified()
        except:
            pass
        base.address1Register4StandardObject = MyEntry(base.Background, 94, 254, entry=base.address1Register4Entry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="Av Najah Nr 12 bouki Hoceima",modified=self.address1Modified,value=self.address1Var)
        base.address1Register4StandardObject.validate=lambda :checkLenght(base.address1Register4StandardObject,4,"Address line 1")

        # address line 2
        base.address2Register4Text = base.Background.create_text(115, 292, text="Address Line 2",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)
        base.address2Register4Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=36,textvariable=self.address2Var)
        try :
            self.address2Modified = base.address2Register4StandardObject.getModified()
        except:
            pass
        base.address2Register4StandardObject = MyEntry(base.Background, 94, 305, entry=base.address2Register4Entry,
                                                       standardImg=base.emailLogingStandardlImg,
                                                       hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                       placeholder="floor Nr 2 App 7",modified=self.address2Modified,value=self.address2Var)
        base.address2Register4StandardObject.validate=lambda :checkLenght(base.address2Register4StandardObject,4,"Address line 2")


        # Postal code
        base.postalRegisterText = base.Background.create_text(115, 394, text="Postal code", font=("Montserrat", 6, "bold"),
                                                              fill="#bb86fc", anchor=tk.NW)
        base.postalRegisterEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                            font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                            highlightthickness=0, borderwidth=0, width=12,textvariable=self.postalCodeVar)
        try :
            self.postalCodeModified = base.postalRegisterStandardObject.getModified()
        except:
            pass
        base.postalRegisterStandardObject = MyEntry(base.Background, 94, 405, entry=base.postalRegisterEntry,
                                                    standardImg=base.inputSmallStandardlImg,
                                                    hoverImg=base.inputSmallHoverImg, marginX=21, marginY=5,
                                                    placeholder="93000",modified=self.postalCodeModified,value=self.postalCodeVar)
        base.postalRegisterStandardObject.validate=lambda :checkPostal(base.postalRegisterStandardObject,"Postal code")

        # Country
        base.countryRegister4Text = base.Background.create_text(115, 343, text="Country", font=("Montserrat", 6, "bold"),
                                                                fill="#bb86fc", anchor=tk.NW)
        base.countryRegister4Label = tk.Label(text="Select", foreground="white", background="#1f1a24", bd=0, relief="flat",
                                              font=("Montserrat", 8, "bold"), width=14, anchor=tk.NW)
        base.countryRegister4Label.config(text=self.countryVar if self.countryVar!=None else "Select")

        base.countryRegister4List = MyMenu(base.Background, 94, 356, base.countryRegister4Label,
                                           base.menuRegister2MidStandardlImg, base.menuRegister2MidHoverImg,
                                           base.menuRegister2MidClickedImg, base.menuListRegister2MidStandardImg,
                                           menuListMarginY=35, hideWidgets=[base.postalRegisterEntry],options=["Select", "Morocco", "USA", "UK", "Canada"],
                                           width=20, height=5, listBoxMarginY=40, border=0, highlightthickness=0, padx=15,
                                           pady=7)
        base.countryRegister4List.validate=lambda:checkListChoice(base.countryRegister4List,"Select","Country")


        # Phone number
        base.phoneRegisterText = base.Background.create_text(324, 394, text="Phone number", font=("Montserrat", 6, "bold"),
                                                             fill="#bb86fc", anchor=tk.NW)
        base.phoneRegisterEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                           font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                           highlightthickness=0, borderwidth=0, width=12,textvariable=self.phoneVar)
        try :
            self.phoneModified = base.phoneRegisterStandardObject.getModified()
        except:
            pass
        base.phoneRegisterStandardObject = MyEntry(base.Background, 304, 405, entry=base.phoneRegisterEntry,
                                                   standardImg=base.inputSmallStandardlImg,
                                                   hoverImg=base.inputSmallHoverImg, marginX=21, marginY=5,
                                                   placeholder="0680992244",modified=self.phoneModified,value=self.phoneVar)
        base.phoneRegisterStandardObject.validate=lambda :checkPhone( base.phoneRegisterStandardObject,4,"Phone number")

        # City
        base.cityRegister4Text = base.Background.create_text(324, 343, text="City", font=("Montserrat", 6, "bold"),
                                                             fill="#bb86fc", anchor=tk.NW)
        base.cityRegister4Label = tk.Label(text="Select", foreground="white", background="#1f1a24", bd=0, relief="flat",
                                           font=("Montserrat", 8, "bold"), width=14, anchor=tk.NW)
        base.cityRegister4Label.config(text=self.cityVar if self.cityVar!=None else "Select")


        base.cityRegister4List = MyMenu(base.Background, 304, 356, base.cityRegister4Label,
                                        base.menuRegister2MidStandardlImg, base.menuRegister2MidHoverImg,
                                        base.menuRegister2MidClickedImg, base.menuListRegister2MidStandardImg,
                                        menuListMarginY=35,hideWidgets=[base.phoneRegisterEntry],
                                        options=["Tetouan", "Hoceima", "Taza", "Tangier", "Rabat", "Casablanca"], width=20,
                                        height=5, listBoxMarginY=40, border=0, highlightthickness=0, padx=15, pady=7)
        base.cityRegister4List.validate=lambda:checkListChoice(base.cityRegister4List,"Select","City")


        base.register4Form = MyForm(base,base.address1Register4StandardObject,base.address2Register4StandardObject,base.postalRegisterStandardObject,base.phoneRegisterStandardObject,base.cityRegister4List,base.countryRegister4List)
        base.register4Form.validate=lambda:checkRegister4Form(base.register4Form,self)
        base.register4Form.get=lambda:self.values

        # #submit
        # base.submitLoginButtonImg = Image.open(
        #     base.resourcePath("assest\general\submitDisabledButtonImg.png")
        # base.submitLoginButtonClickedImg = Image.open(
        #     base.resourcePath("assest\loginPage\submitClicked.png")

        # next
        base.nextRegister4ButtonImg = Image.open(
            base.resourcePath("assest\general\\nextButtonStandardImg.png"))
        base.nextRegister4Button = MyButton(base.Background, 340, 453, standardImg=base.nextRegister1ButtonImg,
                                            cursor="hand2", behavior=base.register4ToRegister5)

        # submit
        base.submitLoginButtonImg = Image.open(
            base.resourcePath("assest\general\submitDisabledButtonImg.png"))
        base.submitRegister4Button = MyButton(base.Background, 221, 453, standardImg=base.submitLoginButtonImg,
                                              cursor="X_cursor")

        # back
        base.backRegister4ButtonImg = Image.open(
            base.resourcePath("assest\general\\backButtonStandardImg.png"))
        base.backRegister4Button = MyButton(base.Background, 141, 453, standardImg=base.backRegister4ButtonImg,
                                            cursor="hand2", behavior=base.register4ToRegister3)

        base.register4Group = MyWidgetsGroup(base.Background,base.register4Title, base.postalRegisterText,
                                             base.postalRegisterEntry, base.postalRegisterStandardObject,
                                             base.phoneRegisterText, base.phoneRegisterEntry,
                                             base.phoneRegisterStandardObject, base.cityRegister4Text,
                                             base.cityRegister4Label, base.cityRegister4List, base.countryRegister4Text,
                                             base.countryRegister4Label, base.countryRegister4List,
                                             base.address1Register4Text, base.address1Register4StandardObject,
                                             base.address2Register4Text, base.address2Register4StandardObject, base.submitRegister4Button,base.register4WidgetsFrame)
