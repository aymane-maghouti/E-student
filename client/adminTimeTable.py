import os
import tkinter as tk
from tkinter import filedialog

from CanvasToWidget import *
from backEndUtilities import save_into_emploi_temps


def checkListChoice(self, choice, optionName="option"):
    if self.get() == choice:
        print(f"invalide {optionName}")
        return False
    print(f"valide {optionName}")
    return True


def checkPdf(self, labelName="pdf"):
    if self == None:  # remake it 1
        print(f"invalide {labelName}")
        return False
    print(f"valide {labelName}")
    return True


def checkAdminTimeTableForm(self, register):
    valide = True
    register.values = []
    for element in self.components:
        try:
            if not element.validate():
                valide = False
        except Exception as e:
            print(e)

            continue
        register.values.append(element.get())
    print(register.values)
    return valide


class AdminTimeTable:
    def __init__(self):
        self.taskSelected = False
        self.hiddenWidgetsPlaces = []

        self.moduleVar = None
        self.moduleModified = False

        self.selectedPDF = None

        self.values = []

    def insertToDB(self):
        if self.base.adminTimeTableForm.validate():
            a, b = self.values
            save_into_emploi_temps(a, b)

    def remove(self):
        self.base.adminTimeTableGroup.removeGroup()

    def importPDF(self):
        pdf_path = filedialog.askopenfilename()
        print(pdf_path)
        filename, extension = os.path.splitext(os.path.basename(pdf_path))
        if extension not in [".pdf"]:
            print(f"please a valid extension")
            return 1
        self.selectedPDF = pdf_path

    def createAdminTimeTable(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame = self
        self.base = base

        base.menuAdminTimeTableClassMidStandardlImg = Image.open(
            r"assets\general\optionsmallStandardImg.png")
        base.menuAdminTimeTableClassMidHoverImg = Image.open(
            r"assets\general\optionSmallHoverImg.png")

        base.menuAdminTimeTableClassMidClickedImg = Image.open(
            r"assets\general\optionSmallClickedImg.png")

        base.menuListAdminTimeTableClassMidStandardImg = Image.open(
            r"assets\general\optionlistMidStandardImg.png")

        # base.TimeTable=adminTimeTable()
        base.adminTimeTableTitle = base.Background.create_text(156, 130, text="Upload TimeTable",
                                                               font=("Montserrat", 20, "bold"), fill="white",
                                                               anchor=tk.NW)

        base.adminTimeTableImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/adminTimeTablePage/TimeTableBackground.png")))

        base.adminTimeTableFrame = base.Background.create_image(117, 174, image=base.adminTimeTableImg, anchor=tk.NW)

        base.adminTimeTableClassText = base.Background.create_text(270, 209, text="Class",
                                                                   font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                   anchor=tk.NW)
        base.adminTimeTableClassLabel = tk.Label(text="Select", foreground="white", background="#382b47", bd=0,
                                                 relief="flat", font=("Montserrat", 8, "bold"), width=6, anchor=tk.NW)
        # base.adminTimeTableClassLabel.config(text=self.bacSectorVar if self.bacSectorVar!=None else "Select")

        base.adminTimeTableClassList = MyMenu(base.Background, 250, 223, base.adminTimeTableClassLabel,
                                              base.menuAdminTimeTableClassMidStandardlImg,
                                              base.menuAdminTimeTableClassMidHoverImg,
                                              base.menuAdminTimeTableClassMidClickedImg,
                                              base.menuListAdminTimeTableClassMidStandardImg,
                                              menuListMarginY=35,
                                              options=["Select", "ID1", "ID2", "GI1", "GI2", "GC1", "GC2", "GEER1",
                                                       "GEER2"],
                                              width=20, height=5, listBoxMarginY=40,
                                              border=0, highlightthickness=0, padx=10, pady=6)
        base.adminTimeTableClassList.validate = lambda: checkListChoice(base.adminTimeTableClassList, "Select", "Class")

        # import
        base.moduleLoginText = base.Background.create_text(270, 277, text="file", font=("Montserrat", 6, "bold"),
                                                           fill="#bb86fc", anchor=tk.NW)

        base.importAdminTimeTableButtonImg = Image.open(
            base.resourcePath("assets/general/uploadStandardImg.png"))
        base.importAdminTimeTableClickedButtonImg = Image.open(
            base.resourcePath("assets/general/uploadClickedImg.png"))
        base.importAdminTimeTableButton = MyButton(base.Background, 250, 289,
                                                   standardImg=base.importAdminTimeTableButtonImg,
                                                   clickImg=base.importAdminTimeTableClickedButtonImg,
                                                   cursor="hand2", behavior=lambda: self.importPDF())
        base.importAdminTimeTableButton.validate = lambda: checkPdf(self.selectedPDF)
        base.importAdminTimeTableButton.get = lambda: self.selectedPDF

        base.adminTimeTableForm = MyForm(base, base.adminTimeTableClassList, base.importAdminTimeTableButton)
        base.adminTimeTableForm.validate = lambda: checkAdminTimeTableForm(base.adminTimeTableForm, self)
        base.adminTimeTableForm.get = lambda: self.values

        base.submitAdminTimeTableButtonImg = Image.open(
            r"assets\loginPage\submitButton.png")
        base.submitAdminTimeTableHoverButtonImg = Image.open(
            r"assets\loginPage\submitClicked.png")
        base.submitAdminTimeTableButton = MyButton(base.Background, 350, 431,
                                                   standardImg=base.submitAdminTimeTableButtonImg,
                                                   clickImg=base.submitAdminTimeTableHoverButtonImg,
                                                   cursor="hand2", behavior=self.insertToDB)

        base.adminTimeTableGroup = MyWidgetsGroup(base.Background, base.adminTimeTableTitle,
                                                  base.adminTimeTableClassText, base.adminTimeTableFrame,
                                                  base.adminTimeTableClassLabel, base.adminTimeTableClassList)
        self.hideWidgets = [self.base.adminTimeTableFrame]
