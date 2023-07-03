import tkinter as tk
from tkinter import messagebox

from CanvasToWidget import *
from backEndUtilities import update_student


def checkLenght(self, size, labelName="entry"):
    if len(self.get()) > size or len(self.get()) < 1:  # remake it 1
        print(f"invalide {labelName}")
        return False
    print(f"valide {labelName}")
    return True


def checkListChoice(self, choice, optionName="option"):
    if self.get() == choice:
        print(f"invalide {optionName}")
        return False
    print(f"valide {optionName}")
    return True


def checkAdminUpdateForm(self, register):
    valide = True
    register.values = []
    if self.components[0].get() == "Select" or self.components[1].get() == "Select":
        messagebox.showerror(title="Invalide choice", message="Class anf Filiere fields are required")
        valide = False
    else:
        filiere_class = {"ID": ["ID1", "ID2"], "GC": ["GC1", "GC2"], "GEER": ["GEER1", "GEER"], "GI": ["GI1", "GI2"]}
        if self.components[0].get() not in filiere_class[self.components[1].get()]:
            valide = False
            messagebox.showerror(title="Invalide choice", message="Not matching choice of Class and Filiere")
        register.values.append(self.components[0].get())
        register.values.append(self.components[1].get())

    return valide


class AdminUpdate:
    def __init__(self):
        self.taskSelected = False
        self.hiddenWidgetsPlaces = []

        self.moduleVar = None
        self.moduleModified = False

        self.selectedPDF = None

        self.values = []

    def updateDB(self):
        if self.base.adminUpdateForm.validate():
            a, b = self.values
            print(self.student)
            update_student("class", a, self.student[0])
            update_student("filiere", b, self.student[0])
            messagebox.showinfo("Update", "User successfully updated")

    def remove(self):
        self.moduleVar = None
        self.moduleModified = False
        self.base.adminUpdateGroup.removeGroup()

    def createAdminUpdate(self, base, student):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame = self
        self.base = base
        self.student = student

        if self.moduleVar == None:
            self.moduleVar = tk.StringVar(base)

        base.menuAdminUpdateClassMidStandardlImg = Image.open(
            r"assets\general\optionsmallStandardImg.png")
        base.menuAdminUpdateClassMidHoverImg = Image.open(
            r"assets\general\optionSmallHoverImg.png")

        base.menuAdminUpdateClassMidClickedImg = Image.open(
            r"assets\general\optionSmallClickedImg.png")

        base.menuListAdminUpdateClassMidStandardImg = Image.open(
            r"assets\general\optionlistMidStandardImg.png")

        # base.Update=adminUpdate()
        base.adminUpdateTitle = base.Background.create_text(156, 130, text=f"Update Student {student[1]}",
                                                            font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.adminUpdateImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/adminUpdatePage/updateBackground.png")))

        base.adminUpdateImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/adminUpdatePage/updateBackground.png")))

        base.adminUpdateFrame = base.Background.create_image(117, 174, image=base.adminUpdateImg, anchor=tk.NW)

        base.moduleAdminUpdateStandardlImg = Image.open(base.resourcePath("assets\general\InputMidLargeLabelImg.png"))
        base.moduleAdminUpdateHoverImg = Image.open(
            base.resourcePath("assets\general\InputMidLargeHoverImg.png"))

        # base.moduleLoginText = base.Background.create_text(270, 278, text="Module", font=("Montserrat", 6, "bold"),
        #                                                   fill="#bb86fc", anchor=tk.NW)
        # base.moduleAdminUpdateEntry = tk.Entry(base.Background, border=0, bg="#382b47", fg="white",
        #                                        font=("Montserrat", 10, "bold"), disabledbackground="#382b47",
        #                                        highlightthickness=0, borderwidth=0, width=30,textvariable=self.moduleVar)
        # try :
        #     self.moduleModified = base.moduleAdminUpdateStandardObject.getModified()
        # except:
        #     pass
        # base.moduleAdminUpdateStandardObject = MyEntry(base.Background, 250, 289, entry=base.moduleAdminUpdateEntry,
        #                                                standardImg=base.moduleAdminUpdateStandardlImg,
        #                                                hoverImg=base.moduleAdminUpdateHoverImg, marginX=21, marginY=5,
        #                                                placeholder="Architecture des ordinateur",modified=self.moduleModified,value=self.moduleVar)
        # base.moduleAdminUpdateStandardObject.validate=lambda:checkLenght(base.moduleAdminUpdateStandardObject,45,"Module")

        base.adminUpdateFiliereText = base.Background.create_text(270, 278, text="filiere",
                                                                  font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                  anchor=tk.NW)
        base.adminUpdateFiliereLabel = tk.Label(text="Select", foreground="white", background="#382b47", bd=0,
                                                relief="flat", font=("Montserrat", 8, "bold"), width=6, anchor=tk.NW)
        # base.adminUpdateClassLabel.config(text=self.bacSectorVar if self.bacSectorVar!=None else "Select")

        base.adminUpdateFiliereList = MyMenu(base.Background, 250, 289, base.adminUpdateFiliereLabel,
                                             base.menuAdminUpdateClassMidStandardlImg,
                                             base.menuAdminUpdateClassMidHoverImg,
                                             base.menuAdminUpdateClassMidClickedImg,
                                             base.menuListAdminUpdateClassMidStandardImg,
                                             menuListMarginY=35, hideWidgets=[],
                                             options=["Select", "ID", "GI", "GC", "GEER"],
                                             width=20, height=5, listBoxMarginY=40,
                                             border=0, highlightthickness=0, padx=10, pady=6)
        base.adminUpdateFiliereList.validate = lambda: checkListChoice(base.adminUpdateFiliereList, "Select", "Class")

        base.adminUpdateClassText = base.Background.create_text(270, 209, text="Class",
                                                                font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                anchor=tk.NW)
        base.adminUpdateClassLabel = tk.Label(text="Select", foreground="white", background="#382b47", bd=0,
                                              relief="flat", font=("Montserrat", 8, "bold"), width=6, anchor=tk.NW)
        # base.adminUpdateClassLabel.config(text=self.bacSectorVar if self.bacSectorVar!=None else "Select")

        base.adminUpdateClassList = MyMenu(base.Background, 250, 223, base.adminUpdateClassLabel,
                                           base.menuAdminUpdateClassMidStandardlImg,
                                           base.menuAdminUpdateClassMidHoverImg,
                                           base.menuAdminUpdateClassMidClickedImg,
                                           base.menuListAdminUpdateClassMidStandardImg,
                                           menuListMarginY=35, hideWidgets=[base.adminUpdateFiliereLabel],
                                           options=["Select", "ID1", "ID2", "GI1", "GI2", "GC1", "GC2", "GEER1",
                                                    "GEER2"],
                                           width=20, height=5, listBoxMarginY=40,
                                           border=0, highlightthickness=0, padx=10, pady=6)
        base.adminUpdateClassList.validate = lambda: checkListChoice(base.adminUpdateClassList, "Select", "Class")

        base.adminUpdateForm = MyForm(base, base.adminUpdateClassList, base.adminUpdateFiliereList)
        base.adminUpdateForm.validate = lambda: checkAdminUpdateForm(base.adminUpdateForm, self)
        base.adminUpdateForm.get = lambda: self.values

        base.submitAdminUpdateButtonImg = Image.open(
            r"assets\loginPage\submitButton.png")
        base.submitAdminUpdateHoverButtonImg = Image.open(
            r"assets\loginPage\submitClicked.png")
        base.submitAdminUpdateButton = MyButton(base.Background, 350, 431, standardImg=base.submitAdminUpdateButtonImg,
                                                clickImg=base.submitAdminUpdateHoverButtonImg,
                                                cursor="hand2", behavior=self.updateDB)

        base.adminUpdateGroup = MyWidgetsGroup(base.Background, base.adminUpdateClassList, base.adminUpdateClassLabel,
                                               base.adminUpdateClassText, base.adminUpdateFiliereList,
                                               base.adminUpdateFiliereLabel, base.adminUpdateFiliereText,
                                               base.adminUpdateTitle, base.adminUpdateFrame,
                                               base.submitAdminUpdateButton)
        self.hideWidgets = [self.base.adminUpdateFrame]
