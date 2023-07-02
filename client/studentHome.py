from CanvasToWidget import *
import tkinter as tk
from studentCourses import StudentCourses
from studentStaff import StudentStaff
from studentGrades import StudentGrades
from studentProfile import StudentProfile
from studentTimeTable import StudentTimeTable
from studentAbout import StudentAbout
from studentNewsDetails import StudentNewsDetail
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.interpolate import splrep, splev
from backEndUtilities import connectDB,get_data


class StudentHome:
    def __init__(self):
        self.taskSelected=False
        self.menuOn=False
        self.hiddenWidgetsPlaces=[]

    def remove(self):
        self.base.studentHomeGroup.removeGroup()

    def removeInterface(self):
        self.base.studentHomeInterfaceGroup.removeGroup()

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

        self.detailNews=StudentNewsDetail()


        base.studentHomeTitle = base.Background.create_text(130, 158, text=f"Welcome {base.connectedUser['firstname']}",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)
        base.logoStudentImg = Image.open(r"assets\general\EstudentLogo.png")
        base.logoStudentObject=MyButton(base.Background,79,51,base.logoStudentImg,cursor="hand2",behavior=lambda:self.toStudentHome())

        base.studentHomeNewsImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assets/studentHomePage/newsBackground.png")))

        base.studentHomeNewsFrame=MyScrollableFrame(base.Background,base.studentHomeNewsImg,"#1f1a24",210,320,615,107,10,50)
        base.studentHomeNewsText=base.Background.create_text(635,117,font=("Montserrat", 20, "bold"),fill="white",text="News",anchor=tk.NW)

        # adding the logout button
        base.logoutStudentStandardImg = Image.open(r"assets\studentHomePage\logoutStandardImg.png").resize((46,46))
        base.logoutStudentHoverImg = Image.open(r"assets\studentHomePage\logoutHoverImg.png").resize((46,46))
        base.logoutStudentButton = MyButton(base.Background,standardImg=base.logoutStudentStandardImg,hoverImg=base.logoutStudentHoverImg,cursor="hand2",x=750,y=43,behavior=base.studentLogout)

        cnx, mycursor = connectDB("student_managment")
        mycursor.execute(
            "SELECT title, date_not, detail FROM notification n, filier f WHERE f.id_filier = n.id_filier AND name = %s order by date_not desc",
            (base.connectedUser['filiere'],))
        results = mycursor.fetchall()

        notifications = []
        print(results)
        for result in results:
            formatted_date = datetime.strftime(result[1], "%Y-%m-%d %H:%M:%S")
            notifications.append([result[0], formatted_date, result[2]])

        print(notifications)
        self.show(notifications)

        base.studentHomeGraphImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assets/studentHomePage/graphBackground.png")))

        base.studentHomeGraphFrame=MyFrame(base.Background,base.studentHomeGraphImg,"#1f1a24",300,200,117,244,10,10)
        self.show_graph()

        #Menu closed
        base.studentMenuImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assets/general/menuBackground.png")))

        base.studentHomeMenuFrame=MyFrame(base.Background,base.studentMenuImg,"#1f1a24",40,351,55,107,4,23)

        base.courses=StudentCourses()
        base.staff=StudentStaff()
        base.grades=StudentGrades()
        base.timeTable=StudentTimeTable()
        base.profile=StudentProfile()
        base.about=StudentAbout()

        base.selectedCircleStudentImg =Image.open(
           base.resourcePath("assets/general/selectedTaskCircle.png"))

        base.selectedCircleStudent=MyButton(base.studentHomeMenuFrame.mainFrame,0,0,base.selectedCircleStudentImg,cursor="hand2",behavior=lambda:print("hi"))
        base.selectedCircleStudent.place_forget()
        # base.selectedCircleStudent.place(0,0)


        base.studentMenuIconImg =Image.open(
           base.resourcePath("assets/general/menuIcon.png"))

        base.studentMenuIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,10,base.studentMenuIconImg,cursor="hand2",behavior=self.extendMenu)

        base.studentBooksIconImg =Image.open(
           base.resourcePath("assets/general/booksIcon.png"))

        base.studentBooksIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,67,base.studentBooksIconImg,cursor="hand2",behavior=lambda:self.toCourses())

        base.studentTimetableIconImg =Image.open(
           base.resourcePath("assets/general/timetableIcon.png"))

        base.studentTimetableIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,117,base.studentTimetableIconImg,cursor="hand2",behavior=self.toTimeTable)

        base.studentGradesIconImg =Image.open(
           base.resourcePath("assets/general/graduationIcon.png"))

        base.studentGradesIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,166,base.studentGradesIconImg,cursor="hand2",behavior=self.toGrades)

        base.studentStaffIconImg =Image.open(
           base.resourcePath("assets/general/staffIcon.png"))

        base.studentStaffIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,217,base.studentStaffIconImg,cursor="hand2",behavior=self.toStaff)

        base.studentProfileIconImg =Image.open(
           base.resourcePath("assets/general/profileIcon.png"))

        base.studentProfileIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,10,263,base.studentProfileIconImg,cursor="hand2",behavior=self.toProfile)

        base.studentAboutIconImg =Image.open(
           base.resourcePath("assets/general/aboutIcon.png"))

        base.studentAboutIconButton=MyButton(base.studentHomeMenuFrame.mainFrame,14,319,base.studentAboutIconImg,cursor="hand2",behavior=self.toAbout)

        #Menu extended
        base.studentMenuExtendedImg =ImageTk.PhotoImage(Image.open(
           base.resourcePath("assets/general/menuExtendedBackground.png")))

        base.studentMenuExtendedFrame=MyFrame(base.Background,base.studentMenuExtendedImg,"#1f1a24",187,351,55,107,4,23)
        base.studentMenuExtendedFrame.place_forget()

        base.studentMenuExtendedIconImg =Image.open(
           base.resourcePath("assets/general/menuExtended.png"))

        base.studentMenuIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,0,base.studentMenuExtendedIconImg,cursor="hand2",behavior=self.shrinkMenu)

        base.studentBooksExtendedIconImg =Image.open(
           base.resourcePath("assets/general/booksExtended.png"))

        base.studentBooksExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,57,base.studentBooksExtendedIconImg,cursor="hand2",behavior=lambda:self.toCourses())

        base.studentTimetableExtendedIconImg =Image.open(
           base.resourcePath("assets/general/timetableExtended.png"))

        base.studentTimetableExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,107,base.studentTimetableExtendedIconImg,cursor="hand2",behavior=self.toTimeTable)

        base.studentGradesExtendedIconImg =Image.open(
           base.resourcePath("assets/general/GradesExtended.png"))

        base.studentGradesExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,156,base.studentGradesExtendedIconImg,cursor="hand2",behavior=self.toGrades)

        base.studentStaffExtendedIconImg =Image.open(
           base.resourcePath("assets/general/staffExtended.png"))

        base.studentStaffExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,207,base.studentStaffExtendedIconImg,cursor="hand2",behavior=self.toStaff)

        base.studentProfileExtendedIconImg =Image.open(
           base.resourcePath("assets/general/profileExtended.png"))

        base.studentProfileExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,256,base.studentProfileExtendedIconImg,cursor="hand2",behavior=self.toProfile)

        base.studentAboutExtendedIconImg =Image.open(
           base.resourcePath("assets/general/aboutExtended.png"))

        base.studentAboutExtendedIconButton=MyButton(base.studentMenuExtendedFrame.mainFrame,0,311,base.studentAboutExtendedIconImg,cursor="hand2",behavior=self.toAbout)

        base.studentHomeGroup = MyWidgetsGroup(base.Background,base.logoutStudentButton,base.studentHomeNewsText,base.studentHomeGraphFrame,base.studentHomeNewsFrame,base.studentHomeTitle)
        base.studentHomeInterfaceGroup = MyWidgetsGroup(base.Background,base.logoStudentObject,base.logoutStudentButton,base.studentHomeNewsText,base.studentHomeGraphFrame,base.studentHomeNewsFrame,base.studentHomeTitle,base.studentHomeMenuFrame)

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

    def show(self,notifications):
        # Create a canvas and add it to the root window
        canvas = Canvas(self.base.studentHomeNewsFrame.scrollable_frame, height=500)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create a frame to hold the table
        table_frame = Frame(canvas,background="#1f1a24",width=10)
        table_frame.pack(fill=BOTH, expand=1)

        # Bind the canvas to the scrollbar
        # global texts
        for i in range(len(notifications)):
            text_length = len(notifications[i][0])
            text_width = 20
            num_lines = int(text_length / text_width) + (1 if text_length % text_width else 0)

            text = Text(table_frame, width=text_width, height=num_lines, takefocus=False,font=("Montserrat", 10, "bold"),relief="flat",cursor="hand2",foreground="#bb86fc",background="#1f1a24")
            text.bind("<Button-1>", lambda event, i=i: self.show_details(notifications,i))
            # texts.append(text)
            text.insert(END, f'{notifications[i][0]}')
            text.configure(state='disabled')
            text.grid(row=(2 * i), column=0)
            Button(table_frame, text=f'{notifications[i][1]}', command=lambda i=i: self.show_details(notifications,i),
                   width=15, height=1,pady=0,padx=0,highlightthickness=0,relief="sunken",borderwidth=0,border=0,overrelief="sunken",foreground="white",background="#1f1a24",activeforeground="white",activebackground="#1f1a24",cursor="hand2",font=("Montserrat", 8, "bold")).grid(row=(2 * i) + 1, column=0,sticky="nw")

    def show_details(self,notifications,i):
        self.base.currentFrame.remove()
        self.detailNews.createStudentNewsDetail(self.base,notifications,i)

    def show_graph(self):
        nb_visiteurs, dates = get_data()
        labels = []
        for i in range(len(nb_visiteurs)):
            label = f"{dates[i]} \n nbr.Connexions {nb_visiteurs[i][0]}"
            labels.append(label)

        dates_smooth = np.linspace(0, 4, 100)
        spl = splrep(range(len(dates)), nb_visiteurs)
        y_smooth = splev(dates_smooth, spl)

        fig, ax = plt.subplots()
        fig.set_size_inches(460 / fig.dpi, 240 / fig.dpi)
        fig.patch.set_facecolor('#1f1a24')
        ax.set_facecolor('#1f1a24')

        # Set the color of the x-axis and y-axis lines and ticks
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # Set the color of the x-axis and y-axis labels
        ax.set_xlabel('X Axis Label', color='white')
        ax.set_ylabel('Y Axis Label', color='white')

        scatter = plt.scatter(dates, nb_visiteurs,edgecolors="#bb86fc",color="#bb86fc")

        def hover(event):
            vis = scatter.contains(event)[0]
            if vis:
                ind = scatter.contains(event)[1]["ind"][0]
                text.set_text(labels[ind])
                text.set_position((dates[ind], nb_visiteurs[ind]))
                text.set_visible(True)
            else:
                text.set_visible(False)
            fig.canvas.draw_idle()

        text = ax.text(0, 0, "", ha="center", va="center", backgroundcolor=(1, 1, 1, 0.7))

        fig.canvas.mpl_connect("motion_notify_event", hover)

        plt.plot(dates_smooth, y_smooth,color="#bb86fc")

        mgr = plt.get_current_fig_manager()
        mgr.resize(40, 20)

        plt.xlabel('')
        plt.ylabel('')
        plt.title("E-student access statistics",color="white",font="Montserrat",fontsize=16, fontweight='bold')

        canvas = FigureCanvasTkAgg(fig, master=self.base.studentHomeGraphFrame.mainFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)






