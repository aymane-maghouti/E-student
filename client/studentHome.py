from CanvasToWidget import *
import tkinter as tk
from studentCourses import StudentCourses
from studentStaff import StudentStaff
from studentGrades import StudentGrades
from studentProfile import StudentProfile
from studentTimeTable import StudentTimeTable
from studentAbout import StudentAbout

class StudentHome:
    def __init__(self):
        self.taskSelected=False
        self.menuOn=False
        self.hiddenWidgetsPlaces=[]

    def remove(self):
        self.base.studentHomeGroup.removeGroup()

    def toStudentHome(self):
        self.base.logoStudentObject.place_forget()
        if self.menuOn==True:
            self.shrinkMenu()
        self.base.currentFrame.remove()
        print("inside toStudentHome")
        self.createStudentHome(self.base)

    def selectTask(self,base,button,x,y):
        if not self.taskSelected:
            button.place(x,y)
            self.taskSelected=True
        else:
            base.moveto(button.standardImgObject, x, y)

    def createStudentHome(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.taskSelected=False
        self.base=base
        # self.hideWidgets=[]


        base.studentHomeTitle = base.Background.create_text(130, 158, text="Welcome Ossama",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)
        base.logoStudentImg = Image.open(r"assest\general\EstudentLogo.png")
        base.logoStudentObject=MyButton(base.Background,79,51,base.logoStudentImg,cursor="hand2",behavior=lambda:self.toStudentHome())

        base.studentHomeNewsImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentHomePage/newsBackground.png")))

        base.studentHomeNewsFrame=MyScrollableFrame(base.Background,base.studentHomeNewsImg,"red",100,200,615,107,10,10)

        base.studentHomeGraphImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentHomePage/graphBackground.png")))

        base.studentHomeGraphFrame=MyFrame(base.Background,base.studentHomeGraphImg,"red",300,200,117,244,10,10)

        #Menu closed
        base.studentMenuImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/general/menuBackground.png")))

        base.studentHomeMenuFrame=MyFrame(base.Background,base.studentMenuImg,"#1f1a24",40,351,55,107,4,23)

        base.courses=StudentCourses()
        base.staff=StudentStaff()
        base.grades=StudentGrades()
        base.timeTable=StudentTimeTable()
        base.profile=StudentProfile()
        base.about=StudentAbout()

        base.selectedCircleStudentImg =Image.open(
           base.resourcePath("assest/general/selectedTaskCircle.png"))

        base.selectedCircleStudent=MyButton(base.studentHomeMenuFrame.mainFrame,0,0,base.selectedCircleStudentImg,cursor="hand2",behavior=lambda:print("hi"))
        base.selectedCircleStudent.place_forget()
        # base.selectedCircleStudent.place(0,0)


        base.studentMenuIconImg =Image.open(
           base.resourcePath("assest/general/menuIcon.png"))

        base.studentMenuIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,10,base.studentMenuIconImg,cursor="hand2",behavior=self.extendMenu)

        base.studentBooksIconImg =Image.open(
           base.resourcePath("assest/general/booksIcon.png"))

        base.studentBooksIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,67,base.studentBooksIconImg,cursor="hand2",behavior=lambda:self.toCourses())

        base.studentTimetableIconImg =Image.open(
           base.resourcePath("assest/general/timetableIcon.png"))

        base.studentTimetableIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,117,base.studentTimetableIconImg,cursor="hand2",behavior=self.toTimeTable)

        base.studentGradesIconImg =Image.open(
           base.resourcePath("assest/general/graduationIcon.png"))

        base.studentGradesIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,166,base.studentGradesIconImg,cursor="hand2",behavior=self.toGrades)

        base.studentStaffIconImg =Image.open(
           base.resourcePath("assest/general/staffIcon.png"))

        base.studentStaffIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,217,base.studentStaffIconImg,cursor="hand2",behavior=self.toStaff)

        base.studentProfileIconImg =Image.open(
           base.resourcePath("assest/general/profileIcon.png"))

        base.studentProfileIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,263,base.studentProfileIconImg,cursor="hand2",behavior=self.toProfile)

        base.studentAboutIconImg =Image.open(
           base.resourcePath("assest/general/aboutIcon.png"))

        base.studentAboutIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,14,319,base.studentAboutIconImg,cursor="hand2",behavior=self.toAbout)

        #Menu extended
        base.studentMenuExtendedImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/general/menuExtendedBackground.png")))

        base.studentMenuExtendedFrame=MyFrame(base.Background,base.studentMenuExtendedImg,"#1f1a24",187,351,55,107,4,23)
        base.studentMenuExtendedFrame.place_forget()

        base.studentMenuExtendedIconImg =Image.open(
           base.resourcePath("assest/general/menuExtended.png"))

        base.studentMenuIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,0,base.studentMenuExtendedIconImg,cursor="hand2",behavior=self.shrinkMenu)

        base.studentBooksExtendedIconImg =Image.open(
           base.resourcePath("assest/general/booksExtended.png"))

        base.studentBooksExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,57,base.studentBooksExtendedIconImg,cursor="hand2",behavior=lambda:self.toCourses())

        base.studentTimetableExtendedIconImg =Image.open(
           base.resourcePath("assest/general/timetableExtended.png"))

        base.studentTimetableExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,107,base.studentTimetableExtendedIconImg,cursor="hand2",behavior=self.toTimeTable)

        base.studentGradesExtendedIconImg =Image.open(
           base.resourcePath("assest/general/GradesExtended.png"))

        base.studentGradesExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,156,base.studentGradesExtendedIconImg,cursor="hand2",behavior=self.toGrades)

        base.studentStaffExtendedIconImg =Image.open(
           base.resourcePath("assest/general/staffExtended.png"))

        base.studentStaffExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,207,base.studentStaffExtendedIconImg,cursor="hand2",behavior=self.toStaff)

        base.studentProfileExtendedIconImg =Image.open(
           base.resourcePath("assest/general/profileExtended.png"))

        base.studentProfileExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,256,base.studentProfileExtendedIconImg,cursor="hand2",behavior=self.toProfile)

        base.studentAboutExtendedIconImg =Image.open(
           base.resourcePath("assest/general/aboutExtended.png"))

        base.studentAboutExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,311,base.studentAboutExtendedIconImg,cursor="hand2",behavior=self.toAbout)

        base.studentHomeGroup = MyWidgetsGroup(base.Background,base.studentHomeGraphFrame,base.studentHomeNewsFrame,base.studentHomeTitle)

        self.hideWidgets=[self.base.studentHomeGraphFrame]

    def toCourses(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.courses.createStudentCourses(self.base)
        self.selectTask(self.base.studentHomeMenuFrame.mainFrame, self.base.selectedCircleStudent, 0, 55)
        print("courses")
        self.menuOn=False

    def toProfile(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.profile.createStudentProfile(self.base)
        self.selectTask(self.base.studentHomeMenuFrame.mainFrame, self.base.selectedCircleStudent, 0, 256)
        print("profile")
        self.menuOn=False

    def toStaff(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.staff.createStudentStaff(self.base)
        self.selectTask(self.base.studentHomeMenuFrame.mainFrame, self.base.selectedCircleStudent, 0, 205)
        print("staff")
        self.menuOn=False

    def toGrades(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.grades.createStudentGrades(self.base)
        self.selectTask(self.base.studentHomeMenuFrame.mainFrame, self.base.selectedCircleStudent, 0, 154)
        print("grades")
        self.menuOn=False
    def toTimeTable(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.timeTable.createStudentTimeTable(self.base)
        self.selectTask(self.base.studentHomeMenuFrame.mainFrame, self.base.selectedCircleStudent, 0, 105)
        print("time table")
        self.menuOn=False

    def toAbout(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.about.createStudentAbout(self.base)
        self.selectTask(self.base.studentHomeMenuFrame.mainFrame, self.base.selectedCircleStudent, 0, 310)
        print("about")
        self.menuOn=False
    def extendMenu(self):
        if self.menuOn==False:
            self.base.studentHomeMenuFrame.place_forget()
            # saving the coorinates of widgets to hide while menu is active
            self.base.currentFrame.hiddenWidgetsPlaces.clear()
            for widget in self.base.currentFrame.hideWidgets:
                print(widget.mainFrame.place_info()["x"])
                self.base.currentFrame.hiddenWidgetsPlaces.append((widget.mainFrame, (int(widget.mainFrame.place_info()["x"]), int(widget.mainFrame.place_info()["y"]))))

            # hiding the widgets while menu is active
            for widget in  self.base.currentFrame.hiddenWidgetsPlaces:
                widget[0].place_forget()
            self.base.studentMenuExtendedFrame.place()
            self.menuOn=True


    def shrinkMenu(self):
        if self.menuOn==True:
            self.base.studentMenuExtendedFrame.place_forget()
            for widget in  self.base.currentFrame.hiddenWidgetsPlaces:
                try:#to avoid an unexplained error
                    widget[0].place(x=widget[1][0],y=widget[1][1])
                except:
                    print("menu list error")

            self.base.studentHomeMenuFrame.place()
            self.menuOn=False




