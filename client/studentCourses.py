from CanvasToWidget import *
import tkinter as tk

class StudentCourses:
    def __init__(self):
        self.taskSelected=False
        self.hiddenWidgetsPlaces=[]


    def remove(self):
        self.base.studentCoursesGroup.removeGroup()

    def createStudentCourses(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        base.currentFrame=self
        self.base=base
        # base.courses=StudentCourses()
        base.studentCoursesTitle = base.Background.create_text(156, 130, text="Courses",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.studentCoursesImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentCoursesPage/coursesBackground.png")))

        base.studentCoursesFrame=MyScrollableFrame(base.Background,base.studentCoursesImg,"blue",685,297,117,174,20,20)

        # base.studentHomeGraphImg =ImageTk.PhotoImage(Image.open(
        #    base.resourcePath("assest/studentHomePage/graphBackground.png")))
        #
        # base.studentCoursesGraphFrame=MyFrame(base.Background,base.studentHomeGraphImg,"blue",100,200,117,244,10,10)

        base.studentCoursesGroup=MyWidgetsGroup(base.Background,base.studentCoursesTitle,base.studentCoursesFrame)
        self.hideWidgets=[self.base.studentCoursesFrame]
