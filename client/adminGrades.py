from CanvasToWidget import *
import tkinter as tk
from tkinter import filedialog
import os
from backEndUtilities import save_into_affichage
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

def checkPdf(self,labelName="pdf"):
    if self==None :#remake it 1
        print(f"invalide {labelName}")
        return False
    print(f"valide {labelName}")
    return True

def checkAdminGradesForm(self,register):
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


class AdminGrades:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]

        self.moduleVar=None
        self.moduleModified=False

        self.selectedPDF=None

        self.values=[]

    def insertToDB(self):
        if self.base.adminGradesForm.validate():
            a,b,c=self.values
            save_into_affichage(a,b,c)


    def remove(self):
        self.moduleVar=None
        self.moduleModified=False
        self.base.adminGradesGroup.removeGroup()
    def importPDF(self):
        pdf_path = filedialog.askopenfilename()
        print(pdf_path)
        filename, extension = os.path.splitext(os.path.basename(pdf_path))
        if extension not in [".pdf"]:
            print(f"please a valid extension")
            return 1
        self.selectedPDF=pdf_path


    def createAdminGrades(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base

        if self.moduleVar == None:
            self.moduleVar = tk.StringVar(base)


        base.menuAdminGradesClassMidStandardlImg = Image.open(
            r"assets\general\optionsmallStandardImg.png")
        base.menuAdminGradesClassMidHoverImg = Image.open(
            r"assets\general\optionSmallHoverImg.png")

        base.menuAdminGradesClassMidClickedImg = Image.open(
            r"assets\general\optionSmallClickedImg.png")

        base.menuListAdminGradesClassMidStandardImg = Image.open(
            r"assets\general\optionlistMidStandardImg.png")


        # base.Grades=adminGrades()
        base.adminGradesTitle = base.Background.create_text(156, 130, text="Upload Grades",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.adminGradesImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assets/adminGradesPage/gradesBackground.png")))

        base.adminGradesImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assets/adminGradesPage/GradesBackground.png")))

        base.adminGradesFrame=base.Background.create_image(117,174,image=base.adminGradesImg,anchor=tk.NW)

        base.moduleAdminGradesStandardlImg = Image.open(base.resourcePath("assets\general\InputMidLargeLabelImg.png"))
        base.moduleAdminGradesHoverImg = Image.open(
            base.resourcePath("assets\general\InputMidLargeHoverImg.png"))

        base.moduleLoginText = base.Background.create_text(270, 278, text="Module", font=("Montserrat", 6, "bold"),
                                                          fill="#bb86fc", anchor=tk.NW)
        base.moduleAdminGradesEntry = tk.Entry(base.Background, border=0, bg="#382b47", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#382b47",
                                               highlightthickness=0, borderwidth=0, width=30,textvariable=self.moduleVar)
        try :
            self.moduleModified = base.moduleAdminGradesStandardObject.getModified()
        except:
            pass
        base.moduleAdminGradesStandardObject = MyEntry(base.Background, 250, 289, entry=base.moduleAdminGradesEntry,
                                                       standardImg=base.moduleAdminGradesStandardlImg,
                                                       hoverImg=base.moduleAdminGradesHoverImg, marginX=21, marginY=5,
                                                       placeholder="Architecture des ordinateur",modified=self.moduleModified,value=self.moduleVar)
        base.moduleAdminGradesStandardObject.validate=lambda:checkLenght(base.moduleAdminGradesStandardObject,45,"Module")

        base.adminGradesClassText = base.Background.create_text(270, 209, text="Class",
                                                                 font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                 anchor=tk.NW)
        base.adminGradesClassLabel = tk.Label(text="Select", foreground="white", background="#382b47", bd=0,
                                               relief="flat", font=("Montserrat", 8, "bold"), width=6, anchor=tk.NW)
        # base.adminGradesClassLabel.config(text=self.bacSectorVar if self.bacSectorVar!=None else "Select")

        base.adminGradesClassList = MyMenu(base.Background, 250, 223, base.adminGradesClassLabel,
                                            base.menuAdminGradesClassMidStandardlImg, base.menuAdminGradesClassMidHoverImg,
                                            base.menuAdminGradesClassMidClickedImg, base.menuListAdminGradesClassMidStandardImg,
                                            menuListMarginY=35,hideWidgets=[base.moduleAdminGradesEntry],
                                            options=["Select","ID1", "ID2", "GI1","GI2","GC1","GC2","GEER1","GEER2"],
                                            width=20, height=5, listBoxMarginY=40,
                                            border=0, highlightthickness=0, padx=10, pady=6)
        base.adminGradesClassList.validate=lambda:checkListChoice(base.adminGradesClassList,"Select","Class")

        #import
        base.moduleLoginText = base.Background.create_text(270, 349, text="file", font=("Montserrat", 6, "bold"),
                                                          fill="#bb86fc", anchor=tk.NW)

        base.importAdminGradesButtonImg = Image.open(
            base.resourcePath("assets/general/uploadStandardImg.png"))
        base.importAdminGradesClickedButtonImg = Image.open(
            base.resourcePath("assets/general/uploadClickedImg.png"))
        base.importAdminGradesButton = MyButton(base.Background, 250, 360, standardImg=base.importAdminGradesButtonImg,clickImg=base.importAdminGradesClickedButtonImg,
                                                 cursor="hand2",behavior=lambda :self.importPDF())
        base.importAdminGradesButton.validate=lambda:checkPdf(self.selectedPDF)
        base.importAdminGradesButton.get=lambda :self.selectedPDF

        base.adminGradesForm = MyForm(base,base.adminGradesClassList,base.moduleAdminGradesStandardObject,base.importAdminGradesButton)
        base.adminGradesForm.validate=lambda:checkAdminGradesForm(base.adminGradesForm,self)
        base.adminGradesForm.get=lambda:self.values

        base.submitAdminGradesButtonImg = Image.open(
            r"assets\loginPage\submitButton.png")
        base.submitAdminGradesHoverButtonImg = Image.open(
            r"assets\loginPage\submitClicked.png")
        base.submitAdminGradesButton = MyButton(base.Background, 350, 431, standardImg=base.submitAdminGradesButtonImg,clickImg=base.submitAdminGradesHoverButtonImg,
                                                 cursor="hand2",behavior=self.insertToDB)

        base.adminGradesGroup=MyWidgetsGroup(base.Background,base.moduleAdminGradesEntry,base.moduleAdminGradesStandardObject,base.adminGradesClassText,base.adminGradesClassLabel,base.adminGradesClassList,base.adminGradesTitle,base.adminGradesFrame)
        self.hideWidgets=[self.base.adminGradesFrame]
