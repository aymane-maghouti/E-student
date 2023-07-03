import tkinter as tk

from CanvasToWidget import *
from backEndUtilities import return_data_by_id


class StudentProfile:
    def __init__(self):
        self.taskSelected = False
        self.hiddenWidgetsPlaces = []

    def remove(self):
        self.base.studentProfileGroup.removeGroup()

    def createStudentProfile(self, base):

        base.currentFrame = self
        self.base = base
        base.studentProfileTitle = base.Background.create_text(156, 130, text="Profile",
                                                               font=("Montserrat", 20, "bold"), fill="white",
                                                               anchor=tk.NW)

        base.studentProfileImg = ImageTk.PhotoImage(Image.open(
            base.resourcePath("assets/studentProfilePage/profileBackground.png")))

        base.studentProfileFrame = MyScrollableFrame(base.Background, base.studentProfileImg, "#1f1a24", 685, 297, 117,
                                                     174, 20, 20)
        l = return_data_by_id(base.connectedUser["id"])
        full_name_label = Label(base.studentProfileFrame.scrollable_frame, text="Full Name :",
                                font=("Montserrat", 8, "bold"),
                                fg="#bb86fc", bg="#1f1a24", width=60, height=0,
                                anchor=W)
        full_name_label.grid(row=1, column=0, padx=5, sticky=W)
        full_name_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[0][0]} {l[0][1]}",
                                  font=("Montserrat", 8, "bold"),
                                  fg="white", bg="#1f1a24", width=60, height=0, pady=0)
        full_name_display.grid(row=2, column=0, padx=5)

        CIN_label = Label(base.studentProfileFrame.scrollable_frame, text="CIN :", font=("Montserrat", 8, "bold"),
                          fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                          pady=0)
        CIN_label.grid(row=3, column=0, padx=5, sticky=W)
        CIN_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[0][2]}",
                            font=("Montserrat", 8, "bold"),
                            fg="white", bg="#1f1a24", width=60, height=0)
        CIN_display.grid(row=4, column=0, padx=5)

        CNE_label = Label(base.studentProfileFrame.scrollable_frame, text="CNE :", font=("Montserrat", 8, "bold"),
                          fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                          pady=0)
        CNE_label.grid(row=5, column=0, padx=5, sticky=W)
        CNE_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[0][3]}",
                            font=("Montserrat", 8, "bold"),
                            fg="white", bg="#1f1a24", width=60)
        CNE_display.grid(row=6, column=0, padx=5)

        gender_label = Label(base.studentProfileFrame.scrollable_frame, text="Gender :", font=("Montserrat", 8, "bold"),
                             fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                             pady=0)
        gender_label.grid(row=7, column=0, padx=5, sticky=W)
        gender_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[0][4]}",
                               font=("Montserrat", 8, "bold"),
                               fg="white", bg="#1f1a24", width=60)
        gender_display.grid(row=8, column=0, padx=5)

        birthday_label = Label(base.studentProfileFrame.scrollable_frame, text="Birthday :",
                               font=("Montserrat", 8, "bold"),
                               fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                               pady=0)
        birthday_label.grid(row=9, column=0, padx=5, sticky=W)
        birthday_display = Label(base.studentProfileFrame.scrollable_frame,
                                 text=f"{l[0][5][0]} / {l[0][5][1]} / {l[0][5][2]}", font=("Montserrat", 8, "bold"),
                                 fg="white", bg="#1f1a24", width=60)
        birthday_display.grid(row=10, column=0, columnspan=2, padx=5)

        bac_sector_label = Label(base.studentProfileFrame.scrollable_frame, text="Bac Sector :",
                                 font=("Montserrat", 8, "bold"),
                                 fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                                 pady=0)
        bac_sector_label.grid(row=11, column=0, padx=5, sticky=W)
        bac_sector_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[2][1]}",
                                   font=("Montserrat", 8, "bold"),
                                   fg="white", bg="#1f1a24", width=60)
        bac_sector_display.grid(row=12, column=0, columnspan=2, padx=5)

        bac_language_label = Label(base.studentProfileFrame.scrollable_frame, text="Bac language :",
                                   font=("Montserrat", 8, "bold"),
                                   fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                                   pady=0)
        bac_language_label.grid(row=11, column=0, padx=5, sticky=W)
        bac_language_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[2][2]}",
                                     font=("Montserrat", 8, "bold"),
                                     fg="white", bg="#1f1a24", width=60)
        bac_language_display.grid(row=12, column=0, columnspan=2, padx=5)

        bac_grade_label = Label(base.studentProfileFrame.scrollable_frame, text="Bac grade :",
                                font=("Montserrat", 8, "bold"),
                                fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                                pady=0)
        bac_grade_label.grid(row=13, column=0, padx=5, sticky=W)
        bac_grade_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[2][3]}",
                                  font=("Montserrat", 8, "bold"),
                                  fg="white", bg="#1f1a24", width=60)
        bac_grade_display.grid(row=14, column=0, columnspan=2, padx=5)

        bac_city_label = Label(base.studentProfileFrame.scrollable_frame, text="Bac city :",
                               font=("Montserrat", 8, "bold"),
                               fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                               pady=0)
        bac_city_label.grid(row=15, column=0, padx=5, sticky=W)
        bac_city_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[2][0]}",
                                 font=("Montserrat", 8, "bold"),
                                 fg="white", bg="#1f1a24", width=60)
        bac_city_display.grid(row=16, column=0, columnspan=2, padx=5)

        high_school_name_label = Label(base.studentProfileFrame.scrollable_frame, text="High school name :",
                                       font=("Montserrat", 8, "bold"),
                                       fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                                       pady=0)
        high_school_name_label.grid(row=17, column=0, padx=5, sticky=W)
        high_school_name_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[2][4]}",
                                         font=("Montserrat", 8, "bold"),
                                         fg="white", bg="#1f1a24", width=60)

        high_school_name_display.grid(row=18, column=0, columnspan=2, padx=5)

        high_school_type_label = Label(base.studentProfileFrame.scrollable_frame, text="High school type :",
                                       font=("Montserrat", 8, "bold"),
                                       fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                                       pady=0)
        high_school_type_label.grid(row=19, column=0, padx=5, sticky=W)
        high_school_type_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[2][5]}",
                                         font=("Montserrat", 8, "bold"),
                                         fg="white", bg="#1f1a24", width=60)
        high_school_type_display.grid(row=20, column=0, columnspan=2, padx=5)

        address1_label = Label(base.studentProfileFrame.scrollable_frame, text="Address line 1 :",
                               font=("Montserrat", 8, "bold"),
                               fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                               pady=0)
        address1_label.grid(row=21, column=0, padx=5, sticky=W)
        address1_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[3][0]}",
                                 font=("Montserrat", 8, "bold"),
                                 fg="white", bg="#1f1a24", width=60)
        address1_display.grid(row=22, column=0, columnspan=2, padx=5)

        address2_label = Label(base.studentProfileFrame.scrollable_frame, text="Address line 2 :",
                               font=("Montserrat", 8, "bold"),
                               fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                               pady=0)
        address2_label.grid(row=23, column=0, padx=5, sticky=W)
        address2_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[3][1]}",
                                 font=("Montserrat", 8, "bold"),
                                 fg="white", bg="#1f1a24", width=60)
        address2_display.grid(row=24, column=0, columnspan=2, padx=5)

        city_label = Label(base.studentProfileFrame.scrollable_frame, text="City :", font=("Montserrat", 8, "bold"),
                           fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                           pady=0)
        city_label.grid(row=25, column=0, padx=5, sticky=W)
        city_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[3][4]}",
                             font=("Montserrat", 8, "bold"),
                             fg="white", bg="#1f1a24", width=60)
        city_display.grid(row=26, column=0, columnspan=2, padx=5)

        country_label = Label(base.studentProfileFrame.scrollable_frame, text="Country :",
                              font=("Montserrat", 8, "bold"),
                              fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                              pady=0)
        country_label.grid(row=27, column=0, padx=5, sticky=W)
        country_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[3][5]}",
                                font=("Montserrat", 8, "bold"),
                                fg="white", bg="#1f1a24", width=60)
        country_display.grid(row=28, column=0, columnspan=2, padx=5)

        postal_code_label = Label(base.studentProfileFrame.scrollable_frame, text="Postal code :",
                                  font=("Montserrat", 8, "bold"),
                                  fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                                  pady=0)
        postal_code_label.grid(row=29, column=0, padx=5, sticky=W)
        postal_code_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[3][2]}",
                                    font=("Montserrat", 8, "bold"),
                                    fg="white", bg="#1f1a24", width=60)
        postal_code_display.grid(row=30, column=0, columnspan=2, padx=5)

        phone_number_label = Label(base.studentProfileFrame.scrollable_frame, text="Phone number :",
                                   font=("Montserrat", 8, "bold"),
                                   fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                                   pady=0)
        phone_number_label.grid(row=31, column=0, padx=5, sticky=W)
        phone_number_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[3][3]}",
                                     font=("Montserrat", 8, "bold"),
                                     fg="white", bg="#1f1a24", width=60)
        phone_number_display.grid(row=32, column=0, columnspan=2, padx=5)

        email_label = Label(base.studentProfileFrame.scrollable_frame, text="Email address :",
                            font=("Montserrat", 8, "bold"),
                            fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                            pady=0)
        email_label.grid(row=33, column=0, padx=5, sticky=W)
        email_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[4][0]}",
                              font=("Montserrat", 8, "bold"),
                              fg="white", bg="#1f1a24", width=60)
        email_display.grid(row=34, column=0, columnspan=2, padx=5)

        filiere_label = Label(base.studentProfileFrame.scrollable_frame, text="Filiere :",
                              font=("Montserrat", 8, "bold"),
                              fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                              pady=0)
        filiere_label.grid(row=35, column=0, padx=5, sticky=W)
        filiere_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[5][1]}",
                                font=("Montserrat", 8, "bold"),
                                fg="white", bg="#1f1a24", width=60)
        filiere_display.grid(row=36, column=0, columnspan=2, padx=5)

        class_label = Label(base.studentProfileFrame.scrollable_frame, text="Class :", font=("Montserrat", 8, "bold"),
                            fg="#bb86fc", bg="#1f1a24", width=50, height=0, anchor=W,
                            pady=0)
        class_label.grid(row=37, column=0, padx=5, sticky=W)
        class_display = Label(base.studentProfileFrame.scrollable_frame, text=f"{l[5][0]}",
                              font=("Montserrat", 8, "bold"),
                              fg="white", bg="#1f1a24", width=60)
        class_display.grid(row=38, column=0, columnspan=2, padx=5)

        # emptyImg=Image.open(
        #    (r"C:\Users\ID 1\tkinterTest\E-student\client\assets\general\emptyImg.jpg")).resize((60,60))

        emptyImg = Image.new("RGBA", (60, 60))

        # Open image in RGBA mode
        input_photo_cadre_register_7_button_img = Image.open(
            base.resourcePath(r"assets\register2Page\inputPhotoCadreStandardImg.png")).convert('RGBA')
        photo_img = l[1][0].convert('RGBA').resize((56, 56))

        # Resize image
        input_photo_cadre_register_7_button_img = input_photo_cadre_register_7_button_img.resize((60, 60))

        # Create a mask to handle the transparency
        mask = input_photo_cadre_register_7_button_img.split()[3]
        mask2 = photo_img.split()[3]

        # Paste image onto new image, using mask
        emptyImg.paste(photo_img, (2, 2, 58, 58), mask2)
        emptyImg.paste(input_photo_cadre_register_7_button_img, (0, 0, 60, 60), mask)

        profile_label = Label(base.studentProfileFrame.scrollable_frame, text="Profile photo :",
                              font=("Montserrat", 8, "bold"),
                              fg="#bb86fc", bg="#1f1a24", width=20, height=0,
                              anchor=W)

        profile_label.grid(row=1, column=1, padx=0, pady=0, sticky=W)

        # Create Label widget and assign image to it
        image_label = Label(base.studentProfileFrame.scrollable_frame, width=60, bg="#1f1a24")
        image_label.grid(row=2, column=1, padx=10, rowspan=4)

        # Convert image to PhotoImage and resize it
        photo = ImageTk.PhotoImage(emptyImg.resize((60, 60)))
        base.global_photo = photo
        # Configure image_label to display the photo
        image_label.config(image=photo)
        print(photo.width(), photo.height())
        print(emptyImg.size, emptyImg.mode)

        base.studentProfileFrame.canvas.create_image(100, 100, image=ImageTk.PhotoImage(emptyImg))

        base.studentProfileGroup = MyWidgetsGroup(base.Background, base.studentProfileTitle, base.studentProfileFrame)
        self.hideWidgets = [self.base.studentProfileFrame]
