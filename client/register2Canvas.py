from CanvasToWidget import *
import tkinter as tk

def checkLenght(self,size,labelName="entry"):
    if len(self.get())>size or len(self.get())<1 :
        print(f"invalide {labelName}")
        return False
    print(f"valide {labelName}")
    return True

class Register2:

    def __init__(self):
        self.bacGradeVar=None
        self.bacGradeModified=False
        self.highSchoolNameVar=None
        self.highSchoolNameModified=False

    def createRegister2(self,base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()
        try:
            base.nextRegister1Button.place_forget()
        except:
            pass
        try:
            base.backRegister3Button.place_forget()
        except:
            pass
        try:
            base.backRegister1Button.place_forget()
        except:
            pass
        try:
            base.nextRegister3Button.place_forget()
        except:
            pass


        if self.bacGradeVar == None:
            self.bacGradeVar = tk.StringVar(base)
        if self.highSchoolNameVar == None:
            self.highSchoolNameVar = tk.StringVar(base)


        base.config(cursor="arrow")
        base.regiter2WidgetsImg = tk.PhotoImage(
            file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\register1Page\registerFrame.png")
        base.register2WidgetsFrame = base.Background.create_image(55, 136, image=base.regiter2WidgetsImg, anchor=tk.NW)
        base.register2Title = base.Background.create_text(94, 158, text="Create your account",
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

        # long input
        base.longInputStandardlImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\inputLabelImg.png")
        base.longInputHoverImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\inputLabelHoveredImg.png")

        # Bac Grade
        base.gradeRegisterTet = base.Background.create_text(115, 292, text="Bac Grade", font=("Montserrat", 6, "bold"),
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
                                                   placeholder="15.27",modified=self.bacGradeModified)

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
                                                  placeholder="Imzoren High school",modified=self.highSchoolNameModified)

        # bac Sector
        base.bacSectorRegister2Text = base.Background.create_text(115, 241, text="Bac Sector",
                                                                  font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                  anchor=tk.NW)
        base.bacSectorRegister2Label = tk.Label(text="Select", foreground="white", background="#1f1a24", bd=0,
                                                relief="flat", font=("Montserrat", 8, "bold"), width=14, anchor=tk.NW)
        base.bacSectorRegister2List = MyMenu(base.Background, 94, 254, base.bacSectorRegister2Label,
                                             base.menuRegister2MidStandardlImg, base.menuRegister2MidHoverImg,
                                             base.menuRegister2MidClickedImg, base.menuListRegister2MidStandardImg,
                                             menuListMarginY=35,
                                             options=["Select","Sc Mathematique 'A'", "Sc Mathematique 'B'", "Sc Physique Chimie",
                                                      "Sc de Vie et Terre", "Sc et Technologie Mecanique"],
                                             hideWidgets=[base.highRegisterEntry], width=20, height=5, listBoxMarginY=40,
                                             border=0, highlightthickness=0, padx=15, pady=7)

        # bac City
        base.bacCityRegister2Text = base.Background.create_text(324, 292, text="Bac City", font=("Montserrat", 6, "bold"),
                                                                fill="#bb86fc", anchor=tk.NW)
        base.bacCityRegister2Label = tk.Label(text="Select", foreground="white", background="#1f1a24", bd=0, relief="flat",
                                              font=("Montserrat", 8, "bold"))
        base.bacCityRegister2List = MyMenu(base.Background, 304, 305, base.bacCityRegister2Label,
                                           base.menuRegister2MidStandardlImg, base.menuRegister2MidHoverImg,
                                           base.menuRegister2MidClickedImg, base.menuListRegister2MidStandardImg,
                                           menuListMarginY=35,
                                           options=["Select","Tetouan", "Tanger", "Hoceima", "Casablanca", "Rabat", "Oujda",
                                                    "Other"], hideWidgets=[base.highRegisterEntry], width=20, height=5,
                                           listBoxMarginY=40, border=0, highlightthickness=0, padx=15, pady=7)

        # bac Language
        base.bacLanguageRegister2Text = base.Background.create_text(324, 241, text="Bac Language",
                                                                    font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                    anchor=tk.NW)
        base.bacLanguageRegister2Label = tk.Label(text="Select", foreground="white", background="#1f1a24", bd=0,
                                                  relief="flat", font=("Montserrat", 8, "bold"))
        base.bacLanguageRegister2List = MyMenu(base.Background, 304, 254, base.bacLanguageRegister2Label,
                                               base.menuRegister2MidStandardlImg, base.menuRegister2MidHoverImg,
                                               base.menuRegister2MidClickedImg, base.menuListRegister2MidStandardImg,
                                               hideWidgets=[base.bacCityRegister2Label, base.highRegisterEntry],
                                               menuListMarginY=35,
                                               options=["Select","Arabic", "French", "English", "Spanish", "Deutsh"], width=20,
                                               height=5, listBoxMarginY=40, border=0, highlightthickness=0, padx=15, pady=7)

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

        # submit
        # base.submitLoginButtonImg = Image.open(
        #     r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\submitDisabledButtonImg.png")
        # base.submitLoginButtonClickedImg = Image.open(
        #     r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\submitClicked.png")

        base.nextRegister2ButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\nextButtonStandardImg.png")
        base.nextRegister2Button = MyButton(base.Background, 340, 453, standardImg=base.nextRegister2ButtonImg,
                                            cursor="hand2", behavior=base.register2ToRegister3)

        base.backRegister2ButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\backButtonStandardImg.png")
        base.backRegister2Button = MyButton(base.Background, 141, 453, standardImg=base.backRegister2ButtonImg,
                                            cursor="hand2", behavior=base.register2ToRegister1)

        base.submitLoginButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\submitDisabledButtonImg.png")
        base.submitRegister2Button = MyButton(base.Background, 221, 453, standardImg=base.submitLoginButtonImg,
                                              cursor="X_cursor")

        base.register2Group = MyWidgetsGroup(base.Background, base.bacSectorRegister2Label, base.bacLanguageRegister2Text,
                                             base.highRegisterText, base.bacLanguageRegister2Label, base.highRegisterText,
                                             base.bacCityRegister2Text, base.bacCityRegister2Label,
                                             base.highRegisterStandardObject, base.submitRegister2Button,
                                             base.register2Title, base.bacLanguageRegister2List,
                                             base.bacSectorRegister2Text, base.bacCityRegister2List, base.highRegisterText,
                                             base.bacSectorRegister2List, base.gradeRegisterText, base.hTypeRegisterText,
                                             base.gradeRegisterStandardObject, base.stateRegisterOption,
                                             base.privateRegisterOption, base.register2WidgetsFrame)

