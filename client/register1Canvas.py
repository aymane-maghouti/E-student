from CanvasToWidget import *
import tkinter as tk
import re
from tkinter import messagebox

def checkLenght(self,size,labelName="entry"):
    if len(self.get())>size or len(self.get())<1 :#remake it 1
        messagebox.showerror("Value Error","invalid name")
        print(f"invalide {labelName}")
        return False
    print(f"valide {labelName}")
    return True
def checkOption(self):
    if self.get()==None:
        print("invalide gender")
        messagebox.showerror("Value Error","invalid gender")
        return False
    print("valide gender")
    return True


def checkRegister1Form(self,register):
    valide=True
    register.values=[]
    for element in self.components:
        try:
            if not element.validate():
                valide=False
                break
        except Exception as e:
            print(e)

            continue
        register.values.append(element.get())
    print(register.values)

    return valide

def checkBirthdayGroup(self):
    day=self.components[0].get()
    month=self.components[1].get()
    year=self.components[2].get()
    valide=True
    if day=="Day"or month=="Month" or year=="Year":
        valide=False
    else:
        if month=="February":
            if day >29:
                valide=False
            else:
                if year % 4 == 0:
                    if year % 100 == 0:
                        if year % 400 == 0:
                            if day==29:
                                valide=False
                else:
                    if day == 29:
                        valide = False

        elif month in ["April","June","September","November"]and day==31:
            valide=False

    if valide==False:
        print("invalide Birthday")
        messagebox.showerror("Value Error","invalid Birthday")
    else:
        print("valide Birthday")

    return valide

def checkCNE(CNE):
    if len(CNE) != 10:
        messagebox.showerror("Value Error","invalid CNE")
        return False
    if not CNE[0].isupper():
        messagebox.showerror("Value Error","invalid CNE")
        return False
    for char in CNE[1:]:
        if not char.isdigit():
            messagebox.showerror("Value Error", "invalid CNE")
            return False
    return True

def checkCIN(CIN):
    if len(CIN) != 6:
        messagebox.showerror("Value Error", "invalid CIN")
        return False
    if CIN[0].isupper() and CIN[1:].isdigit():
        return True
    if CIN[:2].isupper() and CIN[2:].isdigit():
        return True
    messagebox.showerror("Value Error", "invalid CIN")
    return False




class Register1:

    def __init__(self):
        self.firstNameVar = None
        self.firstNameModified = False
        self.lastNameVar = None
        self.lastNameModified = False
        self.CINVar = None
        self.CINModified = False
        self.CNEVar = None
        self.CNEModified = False

        self.dayVar = None
        self.monthVar = None
        self.yearVar = None

        self.genderVar = None

        self.values=[]

    def remove(self,base):
        base.register1Group.removeGroup()
        base.submitRegister1Button.place_forget()
        base.nextRegister1Button.place_forget()



    def createRegister1(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        try:
            base.nextRegister2Button.place_forget()
        except:
            pass
        try:
            base.backRegister2Button.place_forget()
        except:
            pass


        if self.firstNameVar == None:
            self.firstNameVar = tk.StringVar(base)
        if self.lastNameVar == None:
            self.lastNameVar = tk.StringVar(base)
        if self.CINVar == None:
            self.CINVar = tk.StringVar(base)
        if self.CNEVar == None:
            self.CNEVar = tk.StringVar(base)

        base.loginWidgetsImg = tk.PhotoImage(
            file=r"assets\register1Page\registerFrame.png")
        base.register1WidgetsFrame = base.Background.create_image(55, 136, image=base.loginWidgetsImg, anchor=tk.NW)
        base.register1Title = base.Background.create_text(94, 158, text="Create your account",
                                                          font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)

        # option small
        base.optionStandardlImg = Image.open(
           base.resourcePath("assets\general\optionStandardImg.png"))
        base.optionClickImg = Image.open(
           base.resourcePath("assets\general\optionClickedImg.png"))

        # option medium
        base.optionMediumStandardlImg = Image.open(
           base.resourcePath("assets\general\optionMediumStandardImg.png"))
        base.optionMediumClickImg = Image.open(
           base.resourcePath("assets\general\optionMediumClickedImg.png"))

        # input label
        base.inputSmallStandardlImg = Image.open(
           base.resourcePath("assets\general\inputLabelSmallImg.png"))
        base.inputSmallHoverImg = Image.open(
           base.resourcePath("assets\general\inputLabelSmallHoveredImg.png"))

        # day menu list
        base.menuDayStandardlImg = Image.open(
           base.resourcePath("assets\\register1Page\dayStandardImg.png"))
        base.menuDayHoverImg = Image.open(
           base.resourcePath("assets\\register1Page\dayHoverImg.png"))

        base.menuDayClickedImg = Image.open(
           base.resourcePath("assets\\register1Page\dayClickedImg.png"))

        base.menuDayListStandardImg = Image.open(
           base.resourcePath("assets\\register1Page\dayListHoverImg.png"))

        # month menu list
        base.menuMonthStandardlImg = Image.open(
           base.resourcePath("assets\\register1Page\monthStandardImg.png"))
        base.menuMonthHoverImg = Image.open(
           base.resourcePath("assets\\register1Page\monthHoverImg.png"))

        base.menuMonthClickedImg = Image.open(
           base.resourcePath("assets\\register1Page\monthClickedImg.png"))

        base.menuMonthListStandardImg = Image.open(
           base.resourcePath("assets\\register1Page\monthListStandardImg.png"))

        # year menu list
        base.menuYearStandardlImg = Image.open(
           base.resourcePath("assets\\register1Page\yearStandardImg.png"))
        base.menuYearHoverImg = Image.open(
           base.resourcePath("assets\\register1Page\yearHoverImg.png"))
        base.menuYearClickedImg = Image.open(
           base.resourcePath("assets\\register1Page\yearClickedImg.png"))
        base.menuYearListStandardImg = Image.open(
           base.resourcePath("assets\\register1Page\dayListHoverImg.png"))

        # Firstname
        base.firstNameRegisterText = base.Background.create_text(115, 241, text="First name",
                                                                 font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                 anchor=tk.NW)

        base.firstNameRegisterEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                               highlightthickness=0, borderwidth=0, width=12,
                                               textvariable=self.firstNameVar)
        try:
            self.firstNameModified = base.firstNameRegisterStandardObject.getModified()
        except:
            pass
        base.firstNameRegisterStandardObject = MyEntry(base.Background, 94, 254, entry=base.firstNameRegisterEntry,
                                                       standardImg=base.inputSmallStandardlImg,
                                                       hoverImg=base.inputSmallHoverImg, marginX=21, marginY=5,
                                                       placeholder="Ossama", modified=self.firstNameModified,value=self.firstNameVar)
        base.firstNameRegisterStandardObject.validate=lambda :checkLenght(base.firstNameRegisterStandardObject,45,"first name")
        print(self.firstNameModified)
        # Lastname
        base.lastNameRegisterText = base.Background.create_text(325, 241, text="Last name",
                                                                font=("Montserrat", 6, "bold"),
                                                                fill="#bb86fc", anchor=tk.NW)
        base.lastNameRegisterEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                              font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                              highlightthickness=0, borderwidth=0, width=12,
                                              textvariable=self.lastNameVar)
        try:
            self.lastNameModified = base.lastNameRegisterStandardObject.getModified()
        except:
            pass
        base.lastNameRegisterStandardObject = MyEntry(base.Background, 305, 254, entry=base.lastNameRegisterEntry,
                                                      standardImg=base.inputSmallStandardlImg,
                                                      hoverImg=base.inputSmallHoverImg, marginX=21, marginY=5,
                                                      placeholder="Maghouti", modified=self.lastNameModified,value=self.lastNameVar)
        base.lastNameRegisterStandardObject.validate=lambda :checkLenght(base.lastNameRegisterStandardObject,45,"last name")

        # CIN
        base.CINRegisterText = base.Background.create_text(115, 292, text="CIN", font=("Montserrat", 6, "bold"),
                                                           fill="#bb86fc", anchor=tk.NW)
        base.CINRegisterEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                         font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                         highlightthickness=0, borderwidth=0, width=12, textvariable=self.CINVar)
        try:
            self.CINModified = base.CINRegisterStandardObject.getModified()
        except:
            pass

        base.CINRegisterStandardObject = MyEntry(base.Background, 94, 305, entry=base.CINRegisterEntry,
                                                 standardImg=base.inputSmallStandardlImg,
                                                 hoverImg=base.inputSmallHoverImg,
                                                 marginX=21, marginY=5, placeholder="RB459900",
                                                 modified=self.CINModified,value=self.CINVar)
        base.CINRegisterStandardObject.validate=lambda :checkCIN(base.CINRegisterStandardObject.get())
        # CNE
        base.CNERegisterText = base.Background.create_text(325, 292, text="CNE", font=("Montserrat", 6, "bold"),
                                                           fill="#bb86fc", anchor=tk.NW)
        base.CNERegisterEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                         font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                         highlightthickness=0, borderwidth=0, width=12, textvariable=self.CNEVar)
        try:
            self.CNEModified = base.CNERegisterStandardObject.getModified()
        except:
            pass
        base.CNERegisterStandardObject = MyEntry(base.Background, 305, 305, entry=base.CNERegisterEntry,
                                                 standardImg=base.inputSmallStandardlImg,
                                                 hoverImg=base.inputSmallHoverImg,
                                                 marginX=21, marginY=5, placeholder="P111222333",
                                                 modified=self.CNEModified,value=self.CNEVar)
        base.CNERegisterStandardObject.validate=lambda :checkCNE(base.CNERegisterStandardObject.get())
        # Gender
        base.genderRegisterText = base.Background.create_text(115, 343, text="Gender", font=("Montserrat", 6, "bold"),
                                                              fill="#bb86fc", anchor=tk.NW)

        base.genderRegisterOptionList = MyOptionList([])
        base.maleRegisterOption = MyOption(base.Background, 94, 356, value="Male", entry="Male",
                                           font=("Montserrat", 8, "bold"), standardImg=base.optionStandardlImg,
                                           clickImg=base.optionClickImg, fgSelected="#121212", fgNotSelected="white",
                                           anchor=tk.NW, padx=37, pady=8, cursor="hand2")
        base.maleRegisterOption.setOptionlist(base.genderRegisterOptionList)

        base.femaleRegisterOption = MyOption(base.Background, 186, 357, value="Female", entry="Female",
                                             font=("Montserrat", 8, "bold"), standardImg=base.optionMediumStandardlImg,
                                             clickImg=base.optionMediumClickImg, fgSelected="#121212",
                                             fgNotSelected="white", anchor=tk.NW, padx=35, pady=7, cursor="hand2")
        base.femaleRegisterOption.setOptionlist(base.genderRegisterOptionList)

        base.genderRegisterOptionList.optionsList = [base.maleRegisterOption, base.femaleRegisterOption]
        base.genderRegisterOptionList.validate=lambda :checkOption(base.genderRegisterOptionList)

        if self.genderVar!=None:
            for option in base.genderRegisterOptionList.optionsList:
                if option.getValue()==self.genderVar:
                    option.setOn()
                    break
        # Birthday
        base.birthdayRegisterText = base.Background.create_text(115, 394, text="Birthday",
                                                                font=("Montserrat", 6, "bold"),
                                                                fill="#bb86fc", anchor=tk.NW)

        base.dayLabel = tk.Label(text="Day", foreground="white", background="#1f1a24", bd=0, relief="flat",
                                 font=("Montserrat", 8, "bold"), cursor="hand2")
        base.dayLabel.config(text=self.dayVar if self.dayVar!=None else "Day")
        base.dayRegisterList = MyMenu(base.Background, 95, 405, base.dayLabel, base.menuDayStandardlImg,
                                      base.menuDayHoverImg, base.menuDayClickedImg, base.menuDayListStandardImg,
                                      menuListMarginY=35, options=["Day"]+list(range(1, 32)), width=8, height=5,
                                      listBoxMarginY=40,
                                      border=0, highlightthickness=0, padx=15, pady=7)

        base.dayMonthSlash = base.Background.create_text(178, 410, text="/", font=("Montserrat", 12, "bold"),
                                                         fill="white",
                                                         anchor=tk.NW)

        base.monthLabel = tk.Label(text="Month", foreground="white", background="#1f1a24", bd=0, relief="flat",
                                   font=("Montserrat", 8, "bold"), cursor="hand2")
        base.monthLabel.config(text=self.monthVar if self.monthVar!=None else "Month")
        base.monthRegisterList = MyMenu(base.Background, 200, 405, base.monthLabel, base.menuMonthStandardlImg,
                                        base.menuMonthHoverImg, base.menuMonthClickedImg, base.menuMonthListStandardImg,
                                        menuListMarginY=35, options=["Month","January","February","March","April","May","June","July","September","October","November","December"], width=12, height=5,
                                        listBoxMarginY=40, border=0, highlightthickness=0, padx=15, pady=7)

        base.monthYearSlash = base.Background.create_text(328, 410, text="/", font=("Montserrat", 12, "bold"),
                                                          fill="white",
                                                          anchor=tk.NW)

        base.yearLabel = tk.Label(text="Year", foreground="white", background="#1f1a24", bd=0, relief="flat",
                                  font=("Montserrat", 8, "bold"), cursor="hand2")
        base.yearLabel.config(text=self.yearVar if self.yearVar!=None else "Year")
        base.yearRegisterList = MyMenu(base.Background, 342, 405, base.yearLabel, base.menuYearStandardlImg,
                                       base.menuYearHoverImg, base.menuYearClickedImg, base.menuYearListStandardImg,
                                       menuListMarginY=35, options=["Year"]+list(range(1960, 2010)), width=8, height=5,
                                       listBoxMarginY=40, border=0, highlightthickness=0, padx=15, pady=7)

        base.birthdayGroup = MyWidgetsGroup(base, base.dayRegisterList, base.monthRegisterList, base.yearRegisterList)
        base.birthdayGroup.validate=lambda:checkBirthdayGroup(base.birthdayGroup)

        base.register1Form = MyForm(base, base.firstNameRegisterStandardObject, base.lastNameRegisterStandardObject,
                                    base.CINRegisterStandardObject, base.CNERegisterStandardObject,
                                    base.genderRegisterOptionList, base.birthdayGroup)
        base.register1Form.validate=lambda:checkRegister1Form(base.register1Form,self)
        base.register1Form.get=lambda:self.values

        # submi
        base.submitLoginButtonImg = Image.open(
           base.resourcePath("assets\general\submitDisabledButtonImg.png"))
        base.submitLoginButtonClickedImg = Image.open(
           base.resourcePath("assets\loginPage\submitClicked.png"))

        base.nextRegister1ButtonImg = Image.open(
           base.resourcePath("assets\general\\nextButtonStandardImg.png"))
        base.nextRegister1Button = MyButton(base.Background, 340, 453, standardImg=base.nextRegister1ButtonImg,
                                            cursor="hand2", behavior=base.register1ToRegister2)

        base.submitLoginButtonImg = Image.open(
           base.resourcePath("assets\general\submitDisabledButtonImg.png"))
        base.submitRegister1Button = MyButton(base.Background, 221, 453, standardImg=base.submitLoginButtonImg,
                                              cursor="X_cursor")

        base.backDisabledButtonImg = Image.open(
           base.resourcePath("assets\general\\backDisabledButtonImg.png"))
        base.backDisabledButton = MyButton(base.Background, 141, 453, standardImg=base.backDisabledButtonImg,
                                           cursor="X_cursor")

        base.register1Group = MyWidgetsGroup(base.Background, base.birthdayRegisterText, base.backDisabledButton,
                                             base.submitRegister1Button, base.dayMonthSlash, base.monthYearSlash,
                                             base.dayLabel, base.dayRegisterList, base.monthLabel,
                                             base.monthRegisterList,
                                             base.yearLabel, base.yearRegisterList, base.femaleRegisterOption,
                                             base.maleRegisterOption, base.genderRegisterText, base.CNERegisterText,
                                             base.CNERegisterStandardObject, base.CINRegisterText,
                                             base.CINRegisterStandardObject, base.firstNameRegisterStandardObject,
                                             base.firstNameRegisterText,
                                             base.lastNameRegisterText, base.lastNameRegisterStandardObject,
                                             base.register1Title, base.firstNameRegisterStandardObject)



