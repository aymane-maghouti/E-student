from CanvasToWidget import *
import tkinter as tk

def checkLenght(self,size,labelName="entry"):
    if len(self.get())>size or len(self.get())<1 :#remake it 1
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

def checkGrade(self,labelName="entry"):
    try:
        value=float(self.get())
    except:
        print(f"invalide {labelName}")
        return False
    if 0<=value<=20:
        print(f"valide {labelName}")
        return True
    print(f"invalide {labelName}")
    return False

def checkOption(self):
    if self.get()==None:
        print("invalide gender")
        return False
    print("valide gender")
    return True


def checkRegister3Form(self):
    valide=True
    values=[]
    for element in self.components:
        try:
            if not element.validate():
                valide=False
        except Exception as e:
            print(e)

            continue
        values.append(element.get())
    print(values)
    return valide


class Register3:

    def __init__(self):
        self.bacGradeVar=None
        self.bacGradeModified=False
        self.highSchoolNameVar=None
        self.highSchoolNameModified=False

        self.bacSectorVar = None
        self.bacLanguageVar = None
        self.bacCityVar = None

        self.schoolTypeVar=None


    def createRegister3(self,base):
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


        if self.bacGradeVar == None:
            self.bacGradeVar = tk.StringVar(base)
        if self.highSchoolNameVar == None:
            self.highSchoolNameVar = tk.StringVar(base)


        base.config(cursor="arrow")
        base.regiter2WidgetsImg = tk.PhotoImage(
            file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\register1Page\registerFrame.png")
        base.register3WidgetsFrame = base.Background.create_image(55, 136, image=base.regiter2WidgetsImg, anchor=tk.NW)
        base.register3Title = base.Background.create_text(94, 158, text="Create your account",
                                                          font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)

        # option menu list
        base.menuRegister3MidStandardlImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionMidStandardImg.png")
        base.menuRegister3MidHoverImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionMidHoverImg.png")

        base.menuRegister3MidClickedImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionMidClickedImg.png")

        base.menuListRegister3MidStandardImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionlistMidStandardImg.png")

        # long input
        base.longInputStandardlImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\inputLabelImg.png")
        base.longInputHoverImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\inputLabelHoveredImg.png")

        # Bac Grade
        base.gradeRegisterText = base.Background.create_text(115, 292, text="Bac Grade", font=("Montserrat", 6, "bold"),
                                                             fill="#bb86fc", anchor=tk.NW)
        base.gradeRegisterEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                           font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                           highlightthickness=0, borderwidth=0, width=12,textvariable=self.bacGradeVar)
        try :
            self.bacGradeModified = base.gradeRegisterStandardObject.getModified()
        except:
            pass
        base.gradeRegisterStandardObject = MyEntry(base.Background, 94, 305, entry=base.gradeRegisterEntry,
                                                   standardImg=base.inputSmallStandardlImg,
                                                   hoverImg=base.inputSmallHoverImg, marginX=21, marginY=5,
                                                   placeholder="15.27",modified=self.bacGradeModified,value=self.bacGradeVar)
        base.gradeRegisterStandardObject.validate=lambda :checkGrade(base.gradeRegisterStandardObject,"grade")
        # High School Name
        base.highRegisterText = base.Background.create_text(115, 343, text="High school name",
                                                            font=("Montserrat", 6, "bold"),
                                                            fill="#bb86fc", anchor=tk.NW)
        base.highRegisterEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                          font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                          highlightthickness=0, borderwidth=0, width=36,textvariable=self.highSchoolNameVar)
        try :
            self.highSchoolNameModified = base.highRegisterStandardObject.getModified()
        except:
            pass
        base.highRegisterStandardObject = MyEntry(base.Background, 94, 356, entry=base.highRegisterEntry,
                                                  standardImg=base.emailLogingStandardlImg,
                                                  hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                  placeholder="Imzoren High school",modified=self.highSchoolNameModified,value=self.highSchoolNameVar)
        base.highRegisterStandardObject.validate=lambda :checkLenght(base.highRegisterStandardObject,4,"high school name")

        # bac Sector
        base.bacSectorRegister3Text = base.Background.create_text(115, 241, text="Bac Sector",
                                                                  font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                  anchor=tk.NW)
        base.bacSectorRegister3Label = tk.Label(text="Select", foreground="white", background="#1f1a24", bd=0,
                                                relief="flat", font=("Montserrat", 8, "bold"), width=14, anchor=tk.NW)
        base.bacSectorRegister3Label.config(text=self.bacSectorVar if self.bacSectorVar!=None else "Select")

        base.bacSectorRegister3List = MyMenu(base.Background, 94, 254, base.bacSectorRegister3Label,
                                             base.menuRegister3MidStandardlImg, base.menuRegister3MidHoverImg,
                                             base.menuRegister3MidClickedImg, base.menuListRegister3MidStandardImg,
                                             menuListMarginY=35,
                                             options=["Select","Sc Mathematique 'A'", "Sc Mathematique 'B'", "Sc Physique Chimie",
                                                      "Sc de Vie et Terre", "Sc et Technologie Mecanique"],
                                             hideWidgets=[base.highRegisterEntry], width=20, height=5, listBoxMarginY=40,
                                             border=0, highlightthickness=0, padx=15, pady=7)
        base.bacSectorRegister3List.validate=lambda:checkListChoice(base.bacSectorRegister3List,"Select","bac Sector")

        # bac City
        base.bacCityRegister3Text = base.Background.create_text(324, 292, text="Bac City", font=("Montserrat", 6, "bold"),
                                                                fill="#bb86fc", anchor=tk.NW)
        base.bacCityRegister3Label = tk.Label(text="Select", foreground="white", background="#1f1a24", bd=0, relief="flat",
                                              font=("Montserrat", 8, "bold"))
        base.bacCityRegister3Label.config(text=self.bacCityVar if self.bacCityVar!=None else "Select")

        base.bacCityRegister3List = MyMenu(base.Background, 304, 305, base.bacCityRegister3Label,
                                           base.menuRegister3MidStandardlImg, base.menuRegister3MidHoverImg,
                                           base.menuRegister3MidClickedImg, base.menuListRegister3MidStandardImg,
                                           menuListMarginY=35,
                                           options=["Select","Tetouan", "Tanger", "Hoceima", "Casablanca", "Rabat", "Oujda",
                                                    "Other"], hideWidgets=[base.highRegisterEntry], width=20, height=5,
                                           listBoxMarginY=40, border=0, highlightthickness=0, padx=15, pady=7)
        base.bacCityRegister3List.validate=lambda:checkListChoice(base.bacCityRegister3List,"Select","city")

        # bac Language
        base.bacLanguageRegister3Text = base.Background.create_text(324, 241, text="Bac Language",
                                                                    font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                    anchor=tk.NW)
        base.bacLanguageRegister3Label = tk.Label(text="Select", foreground="white", background="#1f1a24", bd=0,
                                                  relief="flat", font=("Montserrat", 8, "bold"))
        base.bacLanguageRegister3Label.config(text=self.bacLanguageVar if self.bacLanguageVar!=None else "Select")

        base.bacLanguageRegister3List = MyMenu(base.Background, 304, 254, base.bacLanguageRegister3Label,
                                               base.menuRegister3MidStandardlImg, base.menuRegister3MidHoverImg,
                                               base.menuRegister3MidClickedImg, base.menuListRegister3MidStandardImg,
                                               hideWidgets=[base.bacCityRegister3Label, base.highRegisterEntry],
                                               menuListMarginY=35,
                                               options=["Select","Arabic", "French", "English", "Spanish", "Deutsh"], width=20,
                                               height=5, listBoxMarginY=40, border=0, highlightthickness=0, padx=15, pady=7)
        base.bacLanguageRegister3List.validate=lambda:checkListChoice(base.bacLanguageRegister3List,"Select","bac Language")

        # high School type

        base.hTypeRegisterText = base.Background.create_text(115, 394, text="High School type",
                                                             font=("Montserrat", 6, "bold"), fill="#bb86fc", anchor=tk.NW)

        base.hTypeRegisterOptionList = MyOptionList([])
        base.stateRegisterOption = MyOption(base.Background, 94, 405, value="State", entry="State",
                                            font=("Montserrat", 8, "bold"), standardImg=base.optionStandardlImg,
                                            clickImg=base.optionClickImg, fgSelected="#121212", fgNotSelected="white",
                                            anchor=tk.NW, padx=37, pady=8, cursor="hand2")
        base.stateRegisterOption.setOptionlist(base.hTypeRegisterOptionList)

        base.privateRegisterOption = MyOption(base.Background, 186, 405, value="Private", entry="Private",
                                              font=("Montserrat", 8, "bold"), standardImg=base.optionMediumStandardlImg,
                                              clickImg=base.optionMediumClickImg, fgSelected="#121212",
                                              fgNotSelected="white", anchor=tk.NW, padx=35, pady=7, cursor="hand2")
        base.privateRegisterOption.setOptionlist(base.hTypeRegisterOptionList)

        base.hTypeRegisterOptionList.optionsList = [base.stateRegisterOption, base.privateRegisterOption]
        base.hTypeRegisterOptionList.validate=lambda :checkOption(base.hTypeRegisterOptionList)

        if self.schoolTypeVar!=None:
            for option in base.hTypeRegisterOptionList.optionsList:
                if option.getValue()==self.schoolTypeVar:
                    option.setOn()
                    break



        base.register3Form = MyForm(base,base.bacCityRegister3List,base.bacSectorRegister3List,base.bacLanguageRegister3List,base.gradeRegisterStandardObject,base.highRegisterStandardObject )
        base.register3Form.validate=lambda:checkRegister3Form(base.register3Form)



        base.nextRegister3ButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\nextButtonStandardImg.png")
        base.nextRegister3Button = MyButton(base.Background, 340, 453, standardImg=base.nextRegister3ButtonImg,
                                            cursor="hand2", behavior=base.register3ToRegister4)

        base.backRegister3ButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\backButtonStandardImg.png")
        base.backRegister3Button = MyButton(base.Background, 141, 453, standardImg=base.backRegister3ButtonImg,
                                            cursor="hand2", behavior=base.register3ToRegister2)

        base.submitLoginButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\submitDisabledButtonImg.png")
        base.submitRegister3Button = MyButton(base.Background, 221, 453, standardImg=base.submitLoginButtonImg,
                                              cursor="X_cursor")

        base.register3Group = MyWidgetsGroup(base.Background, base.bacSectorRegister3Label, base.bacLanguageRegister3Text,
                                             base.highRegisterText, base.bacLanguageRegister3Label, base.highRegisterText,
                                             base.bacCityRegister3Text, base.bacCityRegister3Label,
                                             base.highRegisterStandardObject, base.submitRegister3Button,
                                             base.register3Title, base.bacLanguageRegister3List,
                                             base.bacSectorRegister3Text, base.bacCityRegister3List, base.highRegisterText,
                                             base.bacSectorRegister3List, base.gradeRegisterText, base.hTypeRegisterText,
                                             base.gradeRegisterStandardObject, base.stateRegisterOption,
                                             base.privateRegisterOption, base.register3WidgetsFrame)

