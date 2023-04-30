from CanvasToWidget import *
import tkinter as tk
from backEndUtilities import id_class,connectDB,Convert_IMG,delete_student

def checkListChoice(self,choice,optionName="option"):
    print(f"valide {optionName}")
    return True

def checkAdminStudentsForm(self,register):
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


class AdminStudents:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]
        self.values=[]


    def remove(self):
        self.base.adminStudentsGroup.removeGroup()


    def createAdminStudents(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base

        base.menuAdminStudentClassMidStandardlImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionsmallStandardImg.png")
        base.menuAdminStudentClassMidHoverImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionSmallHoverImg.png")

        base.menuAdminStudentClassMidClickedImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionSmallClickedImg.png")

        base.menuListAdminStudentClassMidStandardImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionlistMidStandardImg.png")


        # base.Students=adminStudents()
        base.adminStudentsTitle = base.Background.create_text(156, 130, text="Students",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.adminStudentsImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/adminStudentsPage/StudentsBackground.png")))

        base.adminStudentsFrame=MyScrollableFrame(base.Background,base.adminStudentsImg,"blue",685,297,117,106,20,90)
        self.canvas=Canvas(base.adminStudentsFrame.scrollable_frame,width=685,height=400,bg="red",highlightthickness=0)
        self.canvas.pack()
        # class
        base.adminStudentsClassText = base.Background.create_text(445, 119, text="Class",
                                                                  font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                  anchor=tk.NW)
        base.adminStudentsClassLabel = tk.Label(text="Select", foreground="white", background="#382b47", bd=0,
                                                relief="flat", font=("Montserrat", 8, "bold"), width=6, anchor=tk.NW)

        base.adminStudentsClassList = MyMenu(base.Background, 425, 133, base.adminStudentsClassLabel,
                                             base.menuAdminStudentClassMidStandardlImg, base.menuAdminStudentClassMidHoverImg,
                                             base.menuAdminStudentClassMidClickedImg, base.menuListAdminStudentClassMidStandardImg,
                                             menuListMarginY=35,
                                             options=["Select","ID1", "ID2", "GI1","GI2","GC1","GC2","GEER1","GEER2"],
                                             hideWidgets=[self.base.adminStudentsFrame.mainFrame], width=20, height=5, listBoxMarginY=40,
                                             border=0, highlightthickness=0, padx=15, pady=7)
        base.adminStudentsClassList.validate=lambda:checkListChoice(base.adminStudentsClassList,"Select","Class")

        base.submitLoginButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\submitButton.png")
        base.submitLoginHoverButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\submitClicked.png")
        base.submitAdminStudentsButton = MyButton(base.adminStudentsFrame.baseCanvas, 714, 133, standardImg=base.submitLoginButtonImg,clickImg=base.submitLoginHoverButtonImg,
                                              cursor="hand2",behavior=lambda:self.display_students(self.base.adminStudentsClassList.get()))

        base.adminStudentsForm = MyForm(base,base.adminStudentsClassList)
        base.adminStudentsForm.validate=lambda:checkAdminStudentsForm(base.adminStudentsForm,self)
        base.adminStudentsForm.get=lambda:self.values

        base.adminStudentsGroup=MyWidgetsGroup(base.Background,base.adminStudentsClassText,base.adminStudentsClassLabel,base.adminStudentsClassList,base.submitAdminStudentsButton,base.adminStudentsTitle,base.adminStudentsFrame)
        self.hideWidgets=[self.base.adminStudentsFrame]



    def display_students(self,class_id):
        # Connect to the database
        my_conn, cursor = connectDB('student_managment')
        print(class_id)
        # Get the list of students for the given class
        cursor.execute("SELECT id_Student,firstname, lastname, image FROM student WHERE id_class = %s", (id_class(class_id),))
        students = cursor.fetchall()
        print(students)



        # Create the column headers in row 0
        tk.Label(self.canvas, text='Nom complet').grid(row=0, column=1)
        tk.Label(self.canvas, text='id').grid(row=0, column=2)
        tk.Label(self.canvas, text='Photo').grid(row=0, column=3)
        tk.Label(self.canvas, text='delete student').grid(row=0, column=4)

        i=1
        for student in students:
            imgobject = Convert_IMG(student[3])
            img = ImageTk.PhotoImage(imgobject)
            tk.Button(self.canvas, text="delete", command=lambda: delete_student(student[0])).grid(row=i, column=4)
            full_name = f"{student[1]} {student[2]}"
            tk.Label(self.canvas, text=full_name).grid(row=i, column=1, ipadx=20)
            tk.Label(self.canvas, text=student[0]).grid(row=i, column=2, ipadx=60)
            tk.Label(self.canvas, image=img).grid(row=i, column=3, ipady=7)
            # liste_images.append(img)
            i+=1
        cursor.close()

