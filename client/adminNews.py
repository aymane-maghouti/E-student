from CanvasToWidget import *
import tkinter as tk
from backEndUtilities import insert_into_notification
from tkinter import messagebox

def checkListChoice(self,choice,optionName="option"):
    if self.get()==choice:
        print(f"invalide {optionName}")
        messagebox.showerror("Value Error",f"invalid {optionName}")
        return False
    print(f"valide {optionName}")
    return True

def checkLenght(self,size,labelName="entry"):
    if len(self.get())>size or len(self.get())<1 :#remake it 1
        print(f"invalide {labelName}")
        messagebox.showerror(f"Value Error",f"invalid {labelName}")
        return False
    print(f"valide {labelName}")
    return True
def checkTextAreaLenght(self,size,labelName="entry"):
    if len(self.get())>size or len(self.get())<1 :#remake it 1
        print(f"invalide {labelName}")
        messagebox.showerror(f"Value Error",f"invalid {labelName}")
        return False
    print(f"valide {labelName}")
    return True


def checkAdminNewsForm(self,register):
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


class AdminNews:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]

        self.titreVar=None
        self.titreModified=False

        self.values=[]
    def remove(self):
        self.base.adminNewsGroup.removeGroup()

    def insertToDB(self):
        if self.base.adminNewsForm.validate():
            a,b,c=self.values
            insert_into_notification(a,b,c)


    def createAdminNews(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        # base.News=adminNews()
        if self.titreVar == None:
            self.titreVar = tk.StringVar(base)
        base.menuAdminNewsClassMidStandardlImg = Image.open(
            r"assets\general\optionsmallStandardImg.png")
        base.menuAdminNewsClassMidHoverImg = Image.open(
            r"assets\general\optionSmallHoverImg.png")

        base.menuAdminNewsClassMidClickedImg = Image.open(
            r"assets\general\optionSmallClickedImg.png")

        base.menuListAdminNewsClassMidStandardImg = Image.open(
            r"assets\general\optionlistMidStandardImg.png")


        base.adminNewsTitle = base.Background.create_text(156, 130, text="Upload News",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.adminNewsImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assets/adminNewsPage/newsBackground.png")))

        base.adminNewsImg =ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/adminNewsPage/NewsBackground.png")))

        base.adminNewsFrame=base.Background.create_image(117,174,image=base.adminNewsImg,anchor=tk.NW)

        base.moduleAdminNewsStandardlImg = Image.open(base.resourcePath("assets\general\InputMidLargeLabelImg.png"))
        base.moduleAdminNewsHoverImg = Image.open(
            base.resourcePath("assets\general\InputMidLargeHoverImg.png"))

        base.titreAdminNewsText = base.Background.create_text(270, 209, text="Titre", font=("Montserrat", 6, "bold"),
                                                          fill="#bb86fc", anchor=tk.NW)
        base.titreAdminNewsEntry = tk.Entry(base.Background, border=0, bg="#382b47", fg="white",
                                               font=("Montserrat", 10, "bold"), disabledbackground="#382b47",
                                               highlightthickness=0, borderwidth=0, width=28,textvariable=self.titreVar)
        try :
            self.titreModified = base.moduleAdminNewsStandardObject.getModified()
        except:
            pass
        base.titreAdminNewsStandardObject = MyEntry(base.Background, 250, 223, entry=base.titreAdminNewsEntry,
                                                       standardImg=base.moduleAdminNewsStandardlImg,
                                                       hoverImg=base.moduleAdminNewsHoverImg, marginX=21, marginY=5,
                                                       placeholder="Architecture des ordinateurs",modified=self.titreModified,value=self.titreVar)
        base.titreAdminNewsStandardObject.validate=lambda:checkLenght(base.titreAdminNewsStandardObject,150,"Title")

        base.detailAdminNewsStandardlImg = ImageTk.PhotoImage(Image.open(base.resourcePath("assets/general/InputTextArea.png")))
        # base.moduleAdminNewsHoverImg = Image.open(
        #     base.resourcePath("assets\general\InputMidLargeHoverImg.png"))
        base.adminNewsDetailBackground=base.Background.create_image(250,273,image=base.detailAdminNewsStandardlImg,anchor=tk.NW)


        base.detailAdminNewsText = base.Background.create_text(270, 259, text="Detail", font=("Montserrat", 6, "bold"),
                                                          fill="#bb86fc", anchor=tk.NW)
        base.tmpdetailAdminNewsEntry = tk.Text(base.Background, border=0, bg="#382b47", fg="white",
                                               font=("Montserrat", 10, "bold"),height=5,
                                               highlightthickness=0, borderwidth=0, width=30)
        base.detailAdminNewsEntry=MyTextArea(base.tmpdetailAdminNewsEntry)
        base.detailAdminNewsEntry.validate=lambda:checkTextAreaLenght(base.detailAdminNewsEntry,9000,"Detail")


        base.detailAdminNewsEntry.place(x=255,y=282)


        base.adminNewsClassText = base.Background.create_text(270, 399, text="Filiere",
                                                                 font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                 anchor=tk.NW)
        base.adminNewsClassLabel = tk.Label(text="Select", foreground="white", background="#382b47", bd=0,
                                               relief="flat", font=("Montserrat", 8, "bold"), width=6, anchor=tk.NW)
        # base.adminNewsClassLabel.config(text=self.bacSectorVar if self.bacSectorVar!=None else "Select")

        base.adminNewsClassList = MyMenu(base.Background, 250, 410, base.adminNewsClassLabel,
                                            base.menuAdminNewsClassMidStandardlImg, base.menuAdminNewsClassMidHoverImg,
                                            base.menuAdminNewsClassMidClickedImg, base.menuListAdminNewsClassMidStandardImg,
                                            menuListMarginY=35,hideWidgets=[],
                                            options=["Select","ID","GI","GC","GEER"],
                                            width=20, height=5, listBoxMarginY=40,
                                            border=0, highlightthickness=0, padx=10, pady=6)
        base.adminNewsClassList.validate=lambda:checkListChoice(base.adminNewsClassList,"Select","Filiere")


        base.adminNewsForm = MyForm(base,base.titreAdminNewsStandardObject, base.detailAdminNewsEntry,base.adminNewsClassList)
        base.adminNewsForm.validate=lambda:checkAdminNewsForm(base.adminNewsForm,self)
        base.adminNewsForm.get=lambda:self.values

        base.submitAdminNewsButtonImg = Image.open(
            r"assets\loginPage\submitButton.png")
        base.submitAdminNewsHoverButtonImg = Image.open(
            r"assets\loginPage\submitClicked.png")
        base.submitAdminNewsButton = MyButton(base.Background, 350, 431, standardImg=base.submitAdminNewsButtonImg,clickImg=base.submitAdminNewsHoverButtonImg,
                                                 cursor="hand2",behavior=self.insertToDB)



        base.adminNewsGroup=MyWidgetsGroup(base.Background,base.titreAdminNewsText,base.titreAdminNewsEntry,base.titreAdminNewsStandardObject,base.adminNewsClassList,base.adminNewsClassLabel,base.adminNewsClassText,base.detailAdminNewsEntry,base.adminNewsTitle,base.adminNewsFrame,base.submitAdminNewsButton)
        self.hideWidgets=[self.base.adminNewsFrame]


