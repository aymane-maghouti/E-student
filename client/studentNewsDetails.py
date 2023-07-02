import tkinter as tk

from CanvasToWidget import *


class StudentNewsDetail:
    def __init__(self):
        self.taskSelected = False
        self.hiddenWidgetsPlaces = []

    def remove(self):
        self.base.studentNewsDetailGroup.removeGroup()

    def createStudentNewsDetail(self, base, notifications, i):
        base.currentFrame = self
        self.base = base
        # base.=studentNewsDetail()
        base.studentNewsDetailTitle = base.Background.create_text(156, 130, text="Detail News",
                                                                  font=("Montserrat", 20, "bold"), fill="white",
                                                                  anchor=tk.NW)

        base.studentNewsDetailImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/studentNewsDetailPage/newsDetailBackground.png")))

        base.studentNewsDetailFrame = MyScrollableFrame(base.Background, base.studentNewsDetailImg, "#1f1a24", 685, 297,
                                                        117, 174, 20, 20)

        # Time
        base.studentNewsTimeText = Label(base.studentNewsDetailFrame.scrollable_frame, text="Published :",
                                         font=("Montserrat", 10, "bold"),
                                         relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.studentNewsTimeText.grid(row=1, column=0, sticky=W)
        base.studentNewsTime = Label(base.studentNewsDetailFrame.scrollable_frame, text=notifications[i][1],
                                     font=("Montserrat", 10, "bold"),
                                     relief="flat", foreground="white", background="#1f1a24")
        base.studentNewsTime.grid(row=2, column=0, sticky=W)

        # Title
        base.studentNewsTitleText = Label(base.studentNewsDetailFrame.scrollable_frame, text="Title :",
                                          font=("Montserrat", 10, "bold"),
                                          relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.studentNewsTitleText.grid(row=3, column=0, sticky=W)

        title_length = len(notifications[i][0])
        title_width = 70
        num_lines = int(title_length / title_width) + (1 if title_length % title_width else 0)

        base.title = Text(base.studentNewsDetailFrame.scrollable_frame, width=title_width, height=num_lines,
                          takefocus=False, font=("Montserrat", 10, "bold"),
                          relief="flat", foreground="white", background="#1f1a24")
        base.title.insert(tk.END, f"{notifications[i][0]}")
        base.title.grid(row=4, column=0, sticky=W)

        # Details
        base.studentNewsDetailsText = Label(base.studentNewsDetailFrame.scrollable_frame, text="Details :",
                                            font=("Montserrat", 10, "bold"),
                                            relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.studentNewsDetailsText.grid(row=5, column=0, sticky=W)

        details_length = len(notifications[i][2])
        details_width = 70
        num_lines = int(details_length / details_width) + (1 if details_length % details_width else 0)

        base.details = Text(base.studentNewsDetailFrame.scrollable_frame, width=details_width, height=num_lines,
                            takefocus=False, font=("Montserrat", 10, "bold"),
                            relief="flat", foreground="white", background="#1f1a24")
        base.details.insert(tk.END, f"{notifications[i][2]}")
        base.details.grid(row=6, column=0, sticky=W)

        base.studentNewsDetailGroup = MyWidgetsGroup(base.Background, base.studentNewsDetailTitle,
                                                     base.studentNewsDetailFrame)
        self.hideWidgets = [self.base.studentNewsDetailFrame]
