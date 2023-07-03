import tkinter as tk
from datetime import datetime

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.interpolate import splrep, splev

from CanvasToWidget import *
from adminAbout import AdminAbout
from adminAdvancedSearch import AdminAdvancedSearch
from adminCourses import AdminCourses
from adminGrades import AdminGrades
from adminNews import AdminNews
from adminNewsDetails import AdminNewsDetail
from adminStudents import AdminStudents
from adminTimeTable import AdminTimeTable
from adminUpdate import AdminUpdate
from backEndUtilities import connectDB, get_data


def resizePlot():
    # Get the DPI of the screen
    dpi = mpl.rcParams['figure.dpi']

    # Set the desired size of the plot in inches
    width = 400  # inches
    height = 200  # inches

    # Calculate the size of the plot in pixels
    figwidth = int(width * dpi)
    figheight = int(height * dpi)

    # Create the figure with the desired size in pixels
    return plt.subplots(figsize=(figwidth / 100, figheight / 100), dpi=dpi)


class AdminHome:
    def __init__(self):
        self.taskSelected = False
        self.menuOn = False
        self.hiddenWidgetsPlaces = []
        self.firstTime=True

    def remove(self):
        self.base.adminHomeGroup.removeGroup()

    def removeInterface(self):
        self.base.adminHomeInterfaceGroup.removeGroup()

    def toAdminHome(self):
        self.base.logoadminObject.place_forget()
        if self.menuOn == True:
            self.shrinkMenu()
        self.base.currentFrame.remove()
        print("inside toadminHome")
        self.createAdminHome(self.base)

    def selectTask(self, base, button, x, y):
        if not self.taskSelected:
            button.place(x, y)
            self.taskSelected = True
        else:
            base.moveto(button.standardImgObject, x, y)

    def createAdminHome(self, base):

        base.currentFrame = self
        self.taskSelected = False
        self.base = base

        self.detailNews = AdminNewsDetail()

        base.adminHomeTitle = base.Background.create_text(130, 158, text="Welcome Admin",
                                                          font=("Montserrat", 20, "bold"), fill="white", anchor=tk.NW)
        base.logoadminImg = Image.open(r"assets\general\EstudentLogo.png")
        base.logoadminObject = MyButton(base.Background, 79, 51, base.logoadminImg, cursor="hand2",
                                        behavior=lambda: self.toAdminHome())

        # adding the logout button
        base.logoutStudentStandardImg = Image.open(r"assets\studentHomePage\logoutStandardImg.png").resize((46, 46))
        base.logoutStudentHoverImg = Image.open(r"assets\studentHomePage\logoutHoverImg.png").resize((46, 46))
        base.logoutStudentButton = MyButton(base.Background, standardImg=base.logoutStudentStandardImg,
                                            hoverImg=base.logoutStudentHoverImg, cursor="hand2", x=750, y=43,
                                            behavior=base.studentLogout)

        base.adminHomeNewsImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/adminHomePage/newsBackground.png")))

        base.adminHomeNewsFrame = MyScrollableFrame(base.Background, base.adminHomeNewsImg, "#1f1a24", 210, 320, 615,
                                                    107, 10, 50)
        base.adminHomeNewsText = base.Background.create_text(635, 117, font=("Montserrat", 20, "bold"), fill="white",
                                                             text="News", anchor=tk.NW)
        cnx, mycursor = connectDB("student_managment")
        mycursor.execute(
            "SELECT title, date_not, detail FROM notification n  order by date_not desc ")
        results = mycursor.fetchall()

        notifications = []
        print(results)
        for result in results:
            formatted_date = datetime.strftime(result[1], "%Y-%m-%d %H:%M:%S")
            notifications.append([result[0], formatted_date, result[2]])

        print(notifications)
        self.show(notifications)

        base.adminHomeGraphImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/adminHomePage/graphBackground.png")))

        base.adminHomeGraphFrame = MyFrame(base.Background, base.adminHomeGraphImg, "red", 460, 240, 117, 244, 10, 10)
        self.show_graph()

        # Menu closed
        base.adminMenuImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/general/menuBackground.png")))

        base.courses = AdminCourses()
        base.News = AdminNews()
        base.grades = AdminGrades()
        base.timeTable = AdminTimeTable()
        base.students = AdminStudents()
        base.about = AdminAbout()
        base.advancedSearch = AdminAdvancedSearch()
        base.advancedSearch = AdminAdvancedSearch()
        base.update = AdminUpdate()

        if self.firstTime:
            base.adminHomeMenuFrame = MyFrame(base.Background, base.adminMenuImg, "#1f1a24", 40, 351, 55, 107, 4, 23)
            self.firstTime=False

            base.adminBooksIconImg = Image.open(
                base.resourcePath("assets/general/booksUpIcon.png"))

            base.adminBooksIconButton = MyButton(base.adminHomeMenuFrame.mainFrame, 10, 67, base.adminBooksIconImg,
                                                 cursor="hand2", behavior=lambda: self.toCourses())

            base.selectedCircleadminImg = Image.open(
                base.resourcePath("assets/general/selectedTaskCircle.png"))

            base.selectedCircleadmin = MyButton(base.adminHomeMenuFrame.mainFrame, 0, 0, base.selectedCircleadminImg,
                                                cursor="hand2", behavior=lambda: print("hi"))
            base.selectedCircleadmin.place_forget()

            base.adminMenuIconImg = Image.open(
                base.resourcePath("assets/general/menuIcon.png"))

            base.adminMenuIconButton = MyButton(base.adminHomeMenuFrame.mainFrame, 10, 10, base.adminMenuIconImg,
                                                cursor="hand2", behavior=self.extendMenu)


            base.adminTimetableIconImg = Image.open(
                base.resourcePath("assets/general/timetableUpIcon.png"))

            base.adminTimetableIconButton = MyButton(base.adminHomeMenuFrame.mainFrame, 10, 117, base.adminTimetableIconImg,
                                                     cursor="hand2", behavior=self.toTimeTable)

            base.adminGradesIconImg = Image.open(
                base.resourcePath("assets/general/graduationUpIcon.png"))

            base.adminGradesIconButton = MyButton(base.adminHomeMenuFrame.mainFrame, 10, 166, base.adminGradesIconImg,
                                                  cursor="hand2", behavior=self.toGrades)

            base.adminNewsIconImg = Image.open(
                base.resourcePath("assets/general/annoucementUpIcon.png"))

            base.adminNewsIconButton = MyButton(base.adminHomeMenuFrame.mainFrame, 10, 217, base.adminNewsIconImg,
                                                cursor="hand2", behavior=self.toNews)

            base.adminStudentsIconImg = Image.open(
                base.resourcePath("assets/general/searchIcon.png"))

            base.adminStudentsIconButton = MyButton(base.adminHomeMenuFrame.mainFrame, 10, 263, base.adminStudentsIconImg,
                                                    cursor="hand2", behavior=self.toStudents)

            base.adminAboutIconImg = Image.open(
                base.resourcePath("assets/general/aboutIcon.png"))

            base.adminAboutIconButton = MyButton(base.adminHomeMenuFrame.mainFrame, 14, 319, base.adminAboutIconImg,
                                                 cursor="hand2", behavior=self.toAbout)
        else :
            base.selectedCircleadmin.place_forget()

        # Menu extended
        base.adminMenuExtendedImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/general/menuExtendedBackground.png")))

        base.adminMenuExtendedFrame = MyFrame(base.Background, base.adminMenuExtendedImg, "#1f1a24", 187, 351, 55, 107,
                                              4, 23)
        base.adminMenuExtendedFrame.place_forget()

        base.adminMenuExtendedIconImg = Image.open(
            base.resourcePath("assets/general/menuExtended.png"))

        base.adminMenuIconButton = MyButton(base.adminMenuExtendedFrame.mainFrame, 0, 0, base.adminMenuExtendedIconImg,
                                            cursor="hand2", behavior=self.shrinkMenu)

        base.adminBooksExtendedIconImg = Image.open(
            base.resourcePath("assets/general/booksUpExtended.png"))

        base.adminBooksExtendedIconButton = MyButton(base.adminMenuExtendedFrame.mainFrame, 0, 57,
                                                     base.adminBooksExtendedIconImg, cursor="hand2",
                                                     behavior=lambda: self.toCourses())

        base.adminTimetableExtendedIconImg = Image.open(
            base.resourcePath("assets/general/timetableUpExtended.png"))

        base.adminTimetableExtendedIconButton = MyButton(base.adminMenuExtendedFrame.mainFrame, 0, 107,
                                                         base.adminTimetableExtendedIconImg, cursor="hand2",
                                                         behavior=self.toTimeTable)

        base.adminGradesExtendedIconImg = Image.open(
            base.resourcePath("assets/general/GradesUpExtended.png"))

        base.adminGradesExtendedIconButton = MyButton(base.adminMenuExtendedFrame.mainFrame, 0, 156,
                                                      base.adminGradesExtendedIconImg, cursor="hand2",
                                                      behavior=self.toGrades)

        base.adminNewsExtendedIconImg = Image.open(
            base.resourcePath("assets/general/newsUpExtended.png"))

        base.adminNewsExtendedIconButton = MyButton(base.adminMenuExtendedFrame.mainFrame, 0, 209,
                                                    base.adminNewsExtendedIconImg, cursor="hand2", behavior=self.toNews)

        base.adminSearchExtendedIconImg = Image.open(
            base.resourcePath("assets/general/studentsUpExtended.png"))

        base.adminSearchExtendedIconButton = MyButton(base.adminMenuExtendedFrame.mainFrame, 0, 254,
                                                      base.adminSearchExtendedIconImg, cursor="hand2",
                                                      behavior=self.toStudents)

        base.adminAboutExtendedIconImg = Image.open(
            base.resourcePath("assets/general/aboutExtended.png"))

        base.adminAboutExtendedIconButton = MyButton(base.adminMenuExtendedFrame.mainFrame, 0, 311,
                                                     base.adminAboutExtendedIconImg, cursor="hand2",
                                                     behavior=self.toAbout)

        base.adminHomeGroup = MyWidgetsGroup(base.Background, base.logoutStudentButton, base.adminHomeNewsText,
                                             base.adminHomeGraphFrame, base.adminHomeNewsFrame, base.adminHomeTitle)
        base.adminHomeInterfaceGroup = MyWidgetsGroup(base.Background, base.logoadminObject, base.logoutStudentButton,
                                                      base.adminHomeNewsText, base.adminHomeGraphFrame,
                                                      base.adminHomeNewsFrame, base.adminHomeTitle,
                                                      base.adminHomeMenuFrame)

        self.hideWidgets = [self.base.adminHomeGraphFrame]

    def toCourses(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.courses.createAdminCourses(self.base)
        self.selectTask(self.base.adminHomeMenuFrame.mainFrame, self.base.selectedCircleadmin, 0, 55)
        print("courses")
        self.menuOn = False

    def toStudents(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.students.createAdminStudents(self.base)
        self.selectTask(self.base.adminHomeMenuFrame.mainFrame, self.base.selectedCircleadmin, 0, 253)
        print("Students")
        self.menuOn = False

    def toNews(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.News.createAdminNews(self.base)
        self.selectTask(self.base.adminHomeMenuFrame.mainFrame, self.base.selectedCircleadmin, 0, 205)
        print("News")
        self.menuOn = False

    def toGrades(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.grades.createAdminGrades(self.base)
        self.selectTask(self.base.adminHomeMenuFrame.mainFrame, self.base.selectedCircleadmin, 0, 154)
        print("grades")
        self.menuOn = False

    def toTimeTable(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.timeTable.createAdminTimeTable(self.base)
        self.selectTask(self.base.adminHomeMenuFrame.mainFrame, self.base.selectedCircleadmin, 0, 105)
        print("time table")
        self.menuOn = False

    def toAbout(self):
        self.shrinkMenu()
        self.base.currentFrame.remove()
        self.base.about.createAdminAbout(self.base)
        self.selectTask(self.base.adminHomeMenuFrame.mainFrame, self.base.selectedCircleadmin, 0, 310)
        print("about")
        self.menuOn = False

    def extendMenu(self):
        if self.menuOn == False:
            self.base.adminHomeMenuFrame.place_forget()
            # saving the coorinates of widgets to hide while menu is active
            self.base.currentFrame.hiddenWidgetsPlaces.clear()
            try:
                for widget in self.base.currentFrame.hideWidgets:
                    print(widget.mainFrame.place_info()["x"])
                    self.base.currentFrame.hiddenWidgetsPlaces.append((widget.mainFrame, (
                    int(widget.mainFrame.place_info()["x"]), int(widget.mainFrame.place_info()["y"]))))

                # hiding the widgets while menu is active
                for widget in self.base.currentFrame.hiddenWidgetsPlaces:
                    widget[0].place_forget()
            except:
                pass
            self.base.adminMenuExtendedFrame.place()
            self.menuOn = True

    def shrinkMenu(self):
        if self.menuOn == True:
            self.base.adminMenuExtendedFrame.place_forget()
            try:
                for widget in self.base.currentFrame.hiddenWidgetsPlaces:
                    try:  # to avoid an unexplained error
                        widget[0].place(x=widget[1][0], y=widget[1][1])
                    except:
                        print("menu list error")
            except:
                pass

            self.base.adminHomeMenuFrame.place()
            self.menuOn = False

    def show(self, notifications):
        # Create a canvas and add it to the root window
        canvas = Canvas(self.base.adminHomeNewsFrame.scrollable_frame, height=500)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create a frame to hold the table
        table_frame = Frame(canvas, background="#1f1a24", width=10)
        table_frame.pack(fill=BOTH, expand=1)

        # global texts
        for i in range(len(notifications)):
            text_length = len(notifications[i][0])
            text_width = 20
            num_lines = int(text_length / text_width) + (1 if text_length % text_width else 0)

            text = Text(table_frame, width=text_width, height=num_lines, takefocus=False,
                        font=("Montserrat", 10, "bold"), relief="flat", cursor="hand2", foreground="#bb86fc",
                        background="#1f1a24")
            text.bind("<Button-1>", lambda event, i=i: self.show_details(notifications, i))
            text.insert(END, f'{notifications[i][0]}')
            text.configure(state='disabled')
            text.grid(row=(2 * i), column=0)
            Button(table_frame, text=f'{notifications[i][1]}', command=lambda i=i: self.show_details(notifications, i),
                   width=20, height=1, pady=0, padx=0, highlightthickness=0, relief="sunken", borderwidth=0, border=0,
                   overrelief="sunken", foreground="white", background="#1f1a24", activeforeground="white",
                   activebackground="#1f1a24", cursor="hand2", font=("Montserrat", 8, "bold")).grid(row=(2 * i) + 1,
                                                                                                    column=0,
                                                                                                    sticky="nw")

    def show_details(self, notifications, i):
        self.base.currentFrame.remove()
        self.detailNews.createAdminNewsDetail(self.base, notifications, i)

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

        scatter = plt.scatter(dates, nb_visiteurs, edgecolors="#bb86fc", color="#bb86fc")

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

        plt.plot(dates_smooth, y_smooth, color="#bb86fc")

        mgr = plt.get_current_fig_manager()
        mgr.resize(40, 20)

        plt.xlabel('')
        plt.ylabel('')
        plt.title("E-student access statistics", color="white", font="Montserrat", fontsize=16, fontweight='bold')

        canvas = FigureCanvasTkAgg(fig, master=self.base.adminHomeGraphFrame.mainFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
