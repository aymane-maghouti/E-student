import tkinter as tk

from CanvasToWidget import *


class AdminNewsDetail:
    def __init__(self):
        self.taskSelected = False
        self.hiddenWidgetsPlaces = []

    def remove(self):
        self.base.adminNewsDetailGroup.removeGroup()

    def createAdminNewsDetail(self, base, notifications, i):
        base.currentFrame = self
        self.base = base
        base.adminNewsDetailTitle = base.Background.create_text(156, 130, text="Detail News",
                                                                font=("Montserrat", 20, "bold"), fill="white",
                                                                anchor=tk.NW)

        base.adminNewsDetailImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/adminNewsDetailPage/newsDetailBackground.png")))

        base.adminNewsDetailFrame = MyScrollableFrame(base.Background, base.adminNewsDetailImg, "#1f1a24", 685, 297,
                                                      117, 174, 20, 20)

        # Time
        base.adminNewsTimeText = Label(base.adminNewsDetailFrame.scrollable_frame, text="Published :",
                                       font=("Montserrat", 10, "bold"),
                                       relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.adminNewsTimeText.grid(row=1, column=0, sticky=W)
        base.adminNewsTime = Label(base.adminNewsDetailFrame.scrollable_frame, text=notifications[i][1],
                                   font=("Montserrat", 10, "bold"),
                                   relief="flat", foreground="white", background="#1f1a24")
        base.adminNewsTime.grid(row=2, column=0, sticky=W)

        # Title
        base.adminNewsTitleText = Label(base.adminNewsDetailFrame.scrollable_frame, text="Title :",
                                        font=("Montserrat", 10, "bold"),
                                        relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.adminNewsTitleText.grid(row=3, column=0, sticky=W)

        title_length = len(notifications[i][0])
        title_width = 70
        num_lines = int(title_length / title_width) + (1 if title_length % title_width else 0)

        base.title = Text(base.adminNewsDetailFrame.scrollable_frame, width=title_width, height=num_lines,
                          takefocus=False, font=("Montserrat", 10, "bold"),
                          relief="flat", foreground="white", background="#1f1a24")
        base.title.insert(tk.END, f"{notifications[i][0]}")
        base.title.grid(row=4, column=0, sticky=W)

        # Details
        base.adminNewsDetailsText = Label(base.adminNewsDetailFrame.scrollable_frame, text="Details :",
                                          font=("Montserrat", 10, "bold"),
                                          relief="flat", foreground="#bb86fc", background="#1f1a24")
        base.adminNewsDetailsText.grid(row=5, column=0, sticky=W)

        details_length = len(notifications[i][2])
        details_width = 70
        num_lines = int(details_length / details_width) + (1 if details_length % details_width else 0)

        base.details = Text(base.adminNewsDetailFrame.scrollable_frame, width=details_width, height=num_lines,
                            takefocus=False, font=("Montserrat", 10, "bold"),
                            relief="flat", foreground="white", background="#1f1a24")
        base.details.insert(tk.END, f"{notifications[i][2]}")
        base.details.grid(row=6, column=0, sticky=W)

        base.adminNewsDetailGroup = MyWidgetsGroup(base.Background, base.adminNewsDetailTitle,
                                                   base.adminNewsDetailFrame)
        self.hideWidgets = [self.base.adminNewsDetailFrame]
