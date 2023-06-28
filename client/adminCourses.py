from CanvasToWidget import *
import tkinter as tk
from tkinter import filedialog
import os
from backEndUtilities import insert_into_document

def checkLenght(self,size,labelName="entry"):
    if len(self.get())>size or len(self.get())<1 :#remake it 1
        print(f"invalide {labelName}")
        return False
    print(f"valide {labelName}")
    return True
def checkPdf(self,labelName="pdf"):
    if self==None :#remake it 1
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

def checkAdminCoursesForm(self,register):
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

class AdminCourses:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]

        self.titreVar=None
        self.titreModified=False

        self.pdfEncoded=None
        self.selectedPdf=None

        self.values=None

    def insertToDB(self):
        if self.base.adminCoursesForm.validate():
            a,b,c,d=self.values
            insert_into_document(a,b,c,d)



    def remove(self):
        self.base.adminCoursesGroup.removeGroup()

    def importPDF(self):
        pdf_path = filedialog.askopenfilename()
        print(pdf_path)
        filename, extension = os.path.splitext(os.path.basename(pdf_path))
        if extension not in [".pdf"]:
            print(f"please a valid extension")
            return 1
        self.selectedPdf=pdf_path



    def createAdminCourses(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        self.selectedPdf=None
        # base.Courses=adminCourses()

        if self.titreVar == None:
            self.titreVar = tk.StringVar(base)

        base.menuAdminCoursesClassMidStandardlImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionsmallStandardImg.png")
        base.menuAdminCoursesClassMidHoverImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionSmallHoverImg.png")

        base.menuAdminCoursesClassMidClickedImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionSmallClickedImg.png")

        base.menuListAdminCoursesClassMidStandardImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionlistMidStandardImg.png")


        base.adminCoursesTitle = base.Background.create_text(156, 130, text="Upload Courses",
                                                             font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.adminCoursesImg =ImageTk.PhotoImage(Image.open(
            base.resourcePath("assest/adminCoursesPage/coursesBackground.png")))

        base.adminCoursesFrame=base.Background.create_image(117,174,image=base.adminCoursesImg,anchor=tk.NW)

        base.moduleAdminCoursesStandardlImg = Image.open(base.resourcePath("assest\general\InputMidLargeLabelImg.png"))
        base.moduleAdminCoursesHoverImg = Image.open(
            base.resourcePath("assest\general\InputMidLargeHoverImg.png"))

        base.moduleAdminCoursesText = base.Background.create_text(270, 278, text="Title", font=("Montserrat", 6, "bold"),
                                                          fill="#bb86fc", anchor=tk.NW)
        base.moduleAdminCoursesEntry = tk.Entry(base.Background, border=0, bg="#382b47", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#382b47",
                                               highlightthickness=0, borderwidth=0, width=30,textvariable=self.titreVar)
        try :
            self.titreModified = base.moduleAdminCoursesStandardObject.getModified()
        except:
            pass
        base.moduleAdminCoursesStandardObject = MyEntry(base.Background, 250, 289, entry=base.moduleAdminCoursesEntry,
                                                       standardImg=base.moduleAdminCoursesStandardlImg,
                                                       hoverImg=base.moduleAdminCoursesHoverImg, marginX=21, marginY=5,
                                                       placeholder="Architecture des ordinateur",modified=self.titreModified,value=self.titreVar)
        base.moduleAdminCoursesStandardObject.validate=lambda:checkLenght(base.moduleAdminCoursesStandardObject,45,"Titre")

        base.adminCoursesClassText = base.Background.create_text(270, 209, text="Class",
                                                                 font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                 anchor=tk.NW)
        base.adminCoursesClassLabel = tk.Label(text="Select", foreground="white", background="#382b47", bd=0,
                                               relief="flat", font=("Montserrat", 8, "bold"), width=6, anchor=tk.NW)
        # base.adminCoursesClassLabel.config(text=self.bacSectorVar if self.bacSectorVar!=None else "Select")

        base.adminCoursesClassList = MyMenu(base.Background, 250, 223, base.adminCoursesClassLabel,
                                            base.menuAdminCoursesClassMidStandardlImg, base.menuAdminCoursesClassMidHoverImg,
                                            base.menuAdminCoursesClassMidClickedImg, base.menuListAdminCoursesClassMidStandardImg,
                                            menuListMarginY=35,hideWidgets=[base.moduleAdminCoursesEntry],
                                            options=["Select","ID1", "ID2", "GI1","GI2","GC1","GC2","GEER1","GEER2"],
                                            width=20, height=5, listBoxMarginY=40,
                                            border=0, highlightthickness=0, padx=10, pady=6)
        base.adminCoursesClassList.validate=lambda:checkListChoice(base.adminCoursesClassList,"Select","Class")

        base.adminCoursesTypeText = base.Background.create_text(420, 209, text="Type",
                                                                 font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                 anchor=tk.NW)
        base.adminCoursesTypeLabel = tk.Label(text="Select", foreground="white", background="#382b47", bd=0,
                                               relief="flat", font=("Montserrat", 8, "bold"), width=6, anchor=tk.NW)
        # base.adminCoursesClassLabel.config(text=self.bacSectorVar if self.bacSectorVar!=None else "Select")

        base.adminCoursesTypeList = MyMenu(base.Background, 400, 223, base.adminCoursesTypeLabel,
                                            base.menuAdminCoursesClassMidStandardlImg, base.menuAdminCoursesClassMidHoverImg,
                                            base.menuAdminCoursesClassMidClickedImg, base.menuListAdminCoursesClassMidStandardImg,
                                            menuListMarginY=35,hideWidgets=[base.moduleAdminCoursesEntry],
                                            options=["Select","Cours","TP","TD"],
                                            width=20, height=4, listBoxMarginY=40,
                                            border=0, highlightthickness=0, padx=10, pady=6)
        base.adminCoursesTypeList.validate=lambda:checkListChoice(base.adminCoursesTypeList,"Select","Type")
        #import
        base.moduleAdminCoursesFileText = base.Background.create_text(270, 349, text="file", font=("Montserrat", 6, "bold"),
                                                          fill="#bb86fc", anchor=tk.NW)

        base.importAdminCoursesButtonImg = Image.open(
            base.resourcePath("assest/general/uploadStandardImg.png"))
        base.importAdminCoursesClickedButtonImg = Image.open(
            base.resourcePath("assest/general/uploadClickedImg.png"))
        base.importAdminCoursesButton = MyButton(base.Background, 250, 360, standardImg=base.importAdminCoursesButtonImg,clickImg=base.importAdminCoursesClickedButtonImg,
                                                 cursor="hand2",behavior=lambda :self.importPDF())
        base.importAdminCoursesButton.validate=lambda:checkPdf(self.selectedPdf)
        base.importAdminCoursesButton.get=lambda :self.selectedPdf

        base.adminCoursesForm = MyForm(base,base.adminCoursesTypeList,base.adminCoursesClassList, base.moduleAdminCoursesStandardObject,base.importAdminCoursesButton)
        base.adminCoursesForm.validate=lambda:checkAdminCoursesForm(base.adminCoursesForm,self)
        base.adminCoursesForm.get=lambda:self.values

        base.submitAdminCoursesButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\submitButton.png")
        base.submitAdminCoursesHoverButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\submitClicked.png")
        base.submitAdminCoursesButton = MyButton(base.Background, 350, 431, standardImg=base.submitAdminCoursesButtonImg,clickImg=base.submitAdminCoursesHoverButtonImg,
                                                 cursor="hand2",behavior=self.insertToDB)


        base.adminCoursesGroup=MyWidgetsGroup(base.Background,base.adminCoursesClassText,base.moduleAdminCoursesEntry,base.moduleAdminCoursesText,base.adminCoursesTypeText,base.adminCoursesClassLabel,base.adminCoursesTypeLabel,base.adminCoursesTitle,base.adminCoursesFrame,base.adminCoursesTypeList,base.adminCoursesClassList,base.moduleAdminCoursesStandardObject,base.moduleAdminCoursesFileText,base.importAdminCoursesButton)
        self.hideWidgets=[]
