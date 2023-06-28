from CanvasToWidget import *
import tkinter as tk
from backEndUtilities import id_class,connectDB,Convert_IMG,delete_student
from tkinter import messagebox

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
        self.liste_images=[]
        self.delete_images=[]


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

        base.adminStudentsFrame=MyScrollableFrame(base.Background,base.adminStudentsImg,"#1f1a24",685,297,117,106,20,90)

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
                                              cursor="hand2",behavior=lambda:self.id_class(base.adminStudentsClassList.get()))

        base.adminStudentsForm = MyForm(base,base.adminStudentsClassList)
        base.adminStudentsForm.validate=lambda:checkAdminStudentsForm(base.adminStudentsForm,self)
        base.adminStudentsForm.get=lambda:self.values

        base.adminStudentsGroup=MyWidgetsGroup(base.Background,base.adminStudentsClassText,base.adminStudentsClassLabel,base.adminStudentsClassList,base.submitAdminStudentsButton,base.adminStudentsTitle,base.adminStudentsFrame)
        self.hideWidgets=[self.base.adminStudentsFrame]

    # # Display the list of students for a given class
    # def display_students(self,class_id):
    #     # Connect to the database
    #     my_conn, cursor = connectDB('student_managment')
    #
    #     # Get the list of students for the given class
    #     cursor.execute("SELECT id_Student,firstname, lastname, image FROM student WHERE id_class = %s", (class_id,))
    #     students = cursor.fetchall()
    #
    #     for widgets in self.base.adminStudentsFrame.table_frame.winfo_children():
    #         widgets.destroy()
    #     # Create a scrollable frame for displaying the students
    #     # Create a canvas and add it to the root window
    #     canvas = Canvas(self.base.adminStudentsFrame.table_frame, width=600, height=500)
    #     canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #
    #     # Create a frame to hold the table
    #     table_frame = Frame(canvas,background="#1f1a24",width=10)
    #     table_frame.pack(fill=BOTH, expand=1)
    #
    #     # Create the column headers in row 0
    #     tk.Label(table_frame, text='Nom complet').grid(row=0, column=1)
    #     tk.Label(table_frame, text='id').grid(row=0, column=2)
    #     tk.Label(table_frame, text='Photo').grid(row=0, column=3)
    #     tk.Label(table_frame, text='delete').grid(row=0, column=4)
    #     tk.Label(table_frame, text='details').grid(row=0, column=5)
    #
    #     deleteStandardIcon = ImageTk.PhotoImage(Image.open(
    #         self.base.resourcePath("assest/general/deleteStandardIcon.png")))
    #     deleteClickedIcon = ImageTk.PhotoImage(Image.open(
    #         self.base.resourcePath("assest/general/deleteClickedIcon.png")))
    #
    #     i=1
    #     for student in students:
    #
    #         imgobject = Convert_IMG(student[3])
    #         img = ImageTk.PhotoImage(imgobject)
    #         # b=MyButton(delete_canvas,standardImg=deleteStandardIcon,hoverImg=deleteClickedIcon,x=0,y=0)
    #         # b=tk.Button(table_frame,image=deleteStandardIcon, command=lambda: delete_student(student[0]))
    #         b=tk.Button(table_frame,relief="sunken",borderwidth=0,cursor="hand2",activebackground="#1f1a24",background="#1f1a24",image=deleteStandardIcon)
    #         b.bind("<Button-1>",lambda event:b.configure(image=deleteClickedIcon))
    #         b.bind("<ButtonRelease-1>",lambda event:b.configure(image=deleteStandardIcon))
    #         b.grid(row=i, column=4)
    #         self.delete_images.append(deleteStandardIcon)
    #
    #         full_name = f"{student[1]} {student[2]}"
    #         tk.Label(table_frame, text=full_name).grid(row=i, column=1, ipadx=20)
    #         tk.Label(table_frame, text=student[0]).grid(row=i, column=2, ipadx=60)
    #         tk.Label(table_frame, image=img,background="#1f1a24").grid(row=i, column=3, ipady=2,ipadx=2)
    #         self.liste_images.append(img)
    #         i+=1
    #     cursor.close()

    # Display the list of students for a given class
    def display_students(self,class_id):
        # Connect to the database
        my_conn, cursor = connectDB('student_managment')

        # Get the list of students for the given class
        cursor.execute("SELECT id_Student,firstname, lastname, image FROM student WHERE id_class = %s", (class_id,))
        students = cursor.fetchall()

        for widgets in self.base.adminStudentsFrame.scrollable_frame.winfo_children():
            widgets.destroy()

        # Create a canvas and add it to the root window
        canvas = Canvas(self.base.adminStudentsFrame.scrollable_frame, width=600, height=500)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create a frame to hold the table
        table_frame = Frame(canvas,background="#1f1a24",width=10)
        table_frame.pack(fill=BOTH, expand=1)

        # Create the column headers in row 0
        tk.Label(table_frame, text='Full name',font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24", width=22, height=2).grid(row=0, column=1)
        tk.Label(table_frame, text='id',font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24", width=5, height=2).grid(row=0, column=2)
        tk.Label(table_frame, text='Photo',font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24", width=5, height=2).grid(row=0, column=3)
        tk.Label(table_frame, text='Delete',font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24", width=5, height=2).grid(row=0, column=4,padx=5)
        tk.Label(table_frame, text='Search',font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24", width=5, height=2).grid(row=0, column=5,padx=5)
        tk.Label(table_frame, text='Update',font=("Montserrat", 12, "bold"),foreground="#bb86fc",background="#1f1a24", width=5, height=2).grid(row=0, column=6,padx=5)

        self.deleteStandardIcon = ImageTk.PhotoImage(Image.open(
            self.base.resourcePath("assest/general/deleteStandardIcon.png")))
        self.searchStandardIcon = ImageTk.PhotoImage(Image.open(
            self.base.resourcePath("assest/general/searchStudentStandardIcon.png")))
        self.editStandardIcon = ImageTk.PhotoImage(Image.open(
            self.base.resourcePath("assest/general/editStandardIcon.png")))


        i=1
        for student in students:
            imgobject = Convert_IMG(student[3])
            img = ImageTk.PhotoImage(imgobject)
            # tk.Button(table_frame, text="delete", command=lambda: delete_student(student[0])).grid(row=i, column=4)
            full_name = f"{student[1]} {student[2]}"
            tk.Label(table_frame, text=full_name,font=("Montserrat", 10),foreground="white",background="#1f1a24", width=38, height=2).grid(row=i, column=1)
            tk.Label(table_frame, text=student[0],font=("Montserrat", 10),foreground="white",background="#1f1a24", width=10, height=2).grid(row=i, column=2)
            tk.Label(table_frame, image=img,background="#1f1a24").grid(row=i, column=3, ipady=7)
            self.liste_images.append(img)

            deleteButton=tk.Button(table_frame,relief="sunken",borderwidth=0,cursor="hand2",activebackground="#1f1a24",background="#1f1a24",image=self.deleteStandardIcon,command=lambda i=i,student=student:self.deleteClicked(student))
            deleteButton.grid(row=i, column=4)

            detailButton=tk.Button(table_frame,relief="sunken",borderwidth=0,cursor="hand2",activebackground="#1f1a24",background="#1f1a24",image=self.searchStandardIcon,command=lambda i=i,student=student:self.searchClicked(student))
            detailButton.grid(row=i, column=5)

            editButton=tk.Button(table_frame,relief="sunken",borderwidth=0,cursor="hand2",activebackground="#1f1a24",background="#1f1a24",image=self.editStandardIcon,command=lambda i=i,student=student:self.editClicked(student))
            editButton.grid(row=i, column=6)
            # self.delete_images.append(deleteStandardIcon)
            # self.delete_images.append(deleteClickedIcon)
            # self.delete_images.append(b)

            i+=1
        cursor.close()

    def id_class(self,class_name):
        class_id = -1
        if class_name == 'ID1':
            class_id = 1
        elif class_name == 'ID2':
            class_id = 2
        elif class_name == 'GI1':
            class_id = 3
        elif class_name == 'GI2':
            class_id = 4
        elif class_name == 'GC1':
            class_id = 5
        elif class_name == 'GC2':
            class_id = 6
        elif class_name == 'GEER1':
            class_id = 7
        elif class_name == 'GEER2':
            class_id = 8
        self.display_students(class_id)


    def deleteClicked(self,student):
        if delete_student(student[0]):
        # self.delete_images[i-1].bind("<Button-1>",lambda event: self.delete_images[i-1].configure(image=img))
            messagebox.showinfo(title="deletion", message=f"{student[1]} {student[2]} deleted successfully")
        else:
            messagebox.showinfo(title="deletion", message=f"{student[1]} {student[2]} deletion Failed")

    def searchClicked(self,student):
        # self.delete_images[i-1].bind("<Button-1>",lambda event: self.delete_images[i-1].configure(image=img))
        self.remove()
        self.base.advancedSearch.createAdminAdvancedSearch(self.base,student)

    def editClicked(self,student):
        # self.delete_images[i-1].bind("<Button-1>",lambda event: self.delete_images[i-1].configure(image=img))
        self.remove()
        self.base.update.createAdminUpdate(self.base,student)

