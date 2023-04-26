from CanvasToWidget import *
import tkinter as tk

class StudentHome:
    def __init__(self):
        self.taskSelected=False

    def selectTask(self,base,button,x,y):
        if not self.taskSelected:
            button.place(x,y)
            self.taskSelected=True
        else:
            base.moveto(button.standardImgObject, x, y)
            # base.itemconfig(button.standardImgObject,x=x)
            # base.itemconfig(button.standardImgObject,y=y)

    def createStudentHome(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()

        try:
            base.nextRegister2Button.place_forget()
        except:
            pass
        try:
            base.backRegister2Button.place_forget()
        except:
            pass

        base.studentHomeTitle = base.Background.create_text(130, 158, text="Welcome Ossama",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)

        base.studentHomeNewsImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentHomePage/newsBackground.png")))

        base.studentHomeNewsFrame=MyScrollableFrame(base.Background,base.studentHomeNewsImg,"red",100,200,615,107,10,10)

        base.studentHomeGraphImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/studentHomePage/graphBackground.png")))

        base.studentHomeGraphFrame=MyFrame(base.Background,base.studentHomeGraphImg,"red",100,200,117,244,10,10)

        #Menu closed
        base.studentMenuImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assest/general/menuBackground.png")))

        base.studentHomeMenuFrame=MyFrame(base.Background,base.studentMenuImg,"red",40,351,55,107,4,23)

        base.selectedCircleStudentImg =Image.open(
           base.resourcePath("assest/general/selectedTaskCircle.png"))

        base.selectedCircleStudent=MyButton(base.studentHomeMenuFrame.mainFrame,0,0,base.selectedCircleStudentImg,behavior=lambda:print("hi"))
        base.selectedCircleStudent.place_forget()

        base.studentMenuIconImg =Image.open(
           base.resourcePath("assest/general/menuIcon.png"))

        base.studentMenuIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,10,base.studentMenuIconImg,cursor="hand2",behavior=lambda:self.selectTask(base.studentHomeMenuFrame.mainFrame,base.selectedCircleStudent,0,0))

        base.studentBooksIconImg =Image.open(
           base.resourcePath("assest/general/booksIcon.png"))

        base.studentBooksIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,67,base.studentBooksIconImg,cursor="hand2",behavior=lambda:self.selectTask(base.studentHomeMenuFrame.mainFrame,base.selectedCircleStudent,0,55))

        base.studentTimetableIconImg =Image.open(
           base.resourcePath("assest/general/timetableIcon.png"))

        base.studentTimetableIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,117,base.studentTimetableIconImg,cursor="hand2",behavior=lambda:self.selectTask(base.studentHomeMenuFrame.mainFrame,base.selectedCircleStudent,0,105))

        base.studentGradesIconImg =Image.open(
           base.resourcePath("assest/general/graduationIcon.png"))

        base.studentGradesIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,166,base.studentGradesIconImg,cursor="hand2",behavior=lambda:self.selectTask(base.studentHomeMenuFrame.mainFrame,base.selectedCircleStudent,0,154))

        base.studentStaffIconImg =Image.open(
           base.resourcePath("assest/general/staffIcon.png"))

        base.studentStaffIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,217,base.studentStaffIconImg,cursor="hand2",behavior=lambda:self.selectTask(base.studentHomeMenuFrame.mainFrame,base.selectedCircleStudent,0,205))

        base.studentProfileIconImg =Image.open(
           base.resourcePath("assest/general/profileIcon.png"))

        base.studentProfileIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,263,base.studentProfileIconImg,cursor="hand2",behavior=lambda:self.selectTask(base.studentHomeMenuFrame.mainFrame,base.selectedCircleStudent,0,256))

        base.studentAboutIconImg =Image.open(
           base.resourcePath("assest/general/aboutIcon.png"))

        base.studentAboutIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,14,319,base.studentAboutIconImg,cursor="hand2",behavior=lambda:self.selectTask(base.studentHomeMenuFrame.mainFrame,base.selectedCircleStudent,0,310))

        #Menu extended
        base.studentAboutIconImg =Image.open(
           base.resourcePath("assest/general/aboutIcon.png"))


