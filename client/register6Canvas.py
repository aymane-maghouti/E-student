from tkinter import messagebox

from CanvasToWidget import *
import tkinter as tk
import re
# from client import *
from backEndUtilities import student_inscription
from loginCanvas import Login



class Register6:
    def __init__(self):
        self.emailRegisterVar=None
        self.emailRegisterModified=False
        self.passwordRegisterVar=None
        self.passwordRegisterModified=False
        self.pConfirmationRegisterVar=None
        self.pConfirmationRegisterModified=False

    def remove(self,base):
        base.register6Group.removeGroup()
        base.submitRegister6Button.place_forget()
        base.nextRegister6Button.place_forget()
        base.backRegister6Button.place_forget()

    def createRegister6(self,base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()
        try:
            base.nextRegister5Button.place_forget()
        except:
            pass

        try:
            base.backRegister5Button.place_forget()
        except:
            pass

        if self.emailRegisterVar == None:
            self.emailRegisterVar = tk.StringVar(base)
        if self.passwordRegisterVar == None:
            self.passwordRegisterVar = tk.StringVar(base)
        if self.pConfirmationRegisterVar == None:
            self.pConfirmationRegisterVar = tk.StringVar(base)

        base.config(cursor="arrow")
        base.register6WidgetsImg = tk.PhotoImage(
            file=base.resourcePath("assets\\register1Page\\registerFrame.png"))
        base.register6WidgetsFrame = base.Background.create_image(55, 136, image=base.register6WidgetsImg, anchor=tk.NW)


        base.register6Title = base.Background.create_text(94, 158, text="Create your account",
                                                          font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)

        base.confirmChoicesText = base.Background.create_text(223, 241, text="Confirm your choices",
                                                                 font=("Montserrat", 6, "bold"),
                                                                 fill="#bb86fc", anchor=tk.NW)

        base.register6BackgroundWidgetsImg = tk.PhotoImage(
            file=base.resourcePath("assets/register6Page/backgroundRegister6Img.png"))

        registerInfo=MyScrollableFrame(base.Background,base.register6BackgroundWidgetsImg,"#1f1a24",315,159,95,255,14,15)
        l=base.getRegisterValues()

        full_name_label = Label(registerInfo.scrollable_frame, text="Full Name :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=30,height=0,anchor=W)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        full_name_label.grid(row=1, column=0, padx=5,sticky=W)
        full_name_display = Label(registerInfo.scrollable_frame, text=f"{l[0][0]} {l[0][1]}",font=("Montserrat", 8, "bold"),
                                                                  fg="white",bg="#1f1a24",width=30,height=0,pady=0)
        full_name_display.grid(row=2, column=0, padx=5)

        CIN_label =  Label(registerInfo.scrollable_frame, text="CIN :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        CIN_label.grid(row=3, column=0, padx=5, sticky=W)
        CIN_display = Label(registerInfo.scrollable_frame, text=f"{l[0][2]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30,height=0)
        CIN_display.grid(row=4, column=0, padx=5)

        CNE_label = Label(registerInfo.scrollable_frame,text="CNE :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        CNE_label.grid(row=5, column=0, padx=5, sticky=W)
        CNE_display = Label(registerInfo.scrollable_frame, text=f"{l[0][3]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        CNE_display.grid(row=6, column=0, padx=5)

        gender_label = Label(registerInfo.scrollable_frame,text="Gender :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        gender_label.grid(row=7, column=0, padx=5, sticky=W)
        gender_display = Label(registerInfo.scrollable_frame, text=f"{l[0][4]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        gender_display.grid(row=8, column=0, padx=5)

        birthday_label = Label(registerInfo.scrollable_frame,text="Birthday :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        birthday_label.grid(row=9, column=0, padx=5, sticky=W)
        birthday_display = Label(registerInfo.scrollable_frame, text=f"{l[0][5][0]} / {l[0][5][1]} / {l[0][5][2]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        birthday_display.grid(row=10, column=0,columnspan=2, padx=5)

        bac_sector_label = Label(registerInfo.scrollable_frame,text="Bac Sector :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        bac_sector_label.grid(row=11, column=0, padx=5, sticky=W)
        bac_sector_display = Label(registerInfo.scrollable_frame, text=f"{l[2][1]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        bac_sector_display.grid(row=12, column=0,columnspan=2, padx=5)

        bac_language_label = Label(registerInfo.scrollable_frame,text="Bac language :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        bac_language_label.grid(row=11, column=0, padx=5, sticky=W)
        bac_language_display = Label(registerInfo.scrollable_frame, text=f"{l[2][2]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        bac_language_display.grid(row=12, column=0,columnspan=2, padx=5)

        bac_grade_label = Label(registerInfo.scrollable_frame,text="Bac grade :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        bac_grade_label.grid(row=13, column=0, padx=5, sticky=W)
        bac_grade_display = Label(registerInfo.scrollable_frame, text=f"{l[2][3]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        bac_grade_display.grid(row=14, column=0,columnspan=2, padx=5)

        bac_city_label = Label(registerInfo.scrollable_frame,text="Bac city :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        bac_city_label.grid(row=15, column=0, padx=5, sticky=W)
        bac_city_display = Label(registerInfo.scrollable_frame, text=f"{l[2][0]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        bac_city_display.grid(row=16, column=0,columnspan=2, padx=5)

        high_school_name_label = Label(registerInfo.scrollable_frame,text="High school name :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        high_school_name_label.grid(row=17, column=0, padx=5, sticky=W)
        high_school_name_display = Label(registerInfo.scrollable_frame, text=f"{l[2][4]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)

        high_school_name_display.grid(row=18, column=0,columnspan=2, padx=5)

        high_school_type_label = Label(registerInfo.scrollable_frame,text="High school type :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        high_school_type_label.grid(row=19, column=0, padx=5, sticky=W)
        high_school_type_display = Label(registerInfo.scrollable_frame, text=f"{l[2][5]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        high_school_type_display.grid(row=20, column=0,columnspan=2, padx=5)

        address1_label = Label(registerInfo.scrollable_frame,text="Address line 1 :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        address1_label.grid(row=21, column=0, padx=5, sticky=W)
        address1_display = Label(registerInfo.scrollable_frame, text=f"{l[3][0]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        address1_display.grid(row=22, column=0,columnspan=2, padx=5)

        address2_label = Label(registerInfo.scrollable_frame,text="Address line 2 :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        address2_label.grid(row=23, column=0, padx=5, sticky=W)
        address2_display = Label(registerInfo.scrollable_frame, text=f"{l[3][1]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        address2_display.grid(row=24, column=0,columnspan=2, padx=5)

        city_label = Label(registerInfo.scrollable_frame,text="City :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        city_label.grid(row=25, column=0, padx=5, sticky=W)
        city_display = Label(registerInfo.scrollable_frame, text=f"{l[3][4]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        city_display.grid(row=26, column=0,columnspan=2, padx=5)

        country_label = Label(registerInfo.scrollable_frame,text="Country :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        country_label.grid(row=27, column=0, padx=5, sticky=W)
        country_display = Label(registerInfo.scrollable_frame, text=f"{l[3][5]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        country_display.grid(row=28, column=0,columnspan=2, padx=5)

        postal_code_label = Label(registerInfo.scrollable_frame,text="Postal code :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        postal_code_label.grid(row=29, column=0, padx=5, sticky=W)
        postal_code_display = Label(registerInfo.scrollable_frame, text=f"{l[3][2]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        postal_code_display.grid(row=30, column=0,columnspan=2, padx=5)

        phone_number_label = Label(registerInfo.scrollable_frame,text="Phone number :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        phone_number_label.grid(row=31, column=0, padx=5, sticky=W)
        phone_number_display = Label(registerInfo.scrollable_frame, text=f"{l[3][3]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        phone_number_display.grid(row=32, column=0,columnspan=2, padx=5)

        email_label = Label(registerInfo.scrollable_frame,text="Email address :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",width=20,height=0,anchor=W,pady=0)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")
        email_label.grid(row=33, column=0, padx=5, sticky=W)
        email_display = Label(registerInfo.scrollable_frame, text=f"{l[4][0]}",font=("Montserrat", 8, "bold"),
                                                                 fg="white",bg="#1f1a24",width=30)
        email_display.grid(row=34, column=0,columnspan=2, padx=5)


        emptyImg = Image.new("RGBA", (60, 60))

        # Open image in RGBA mode
        input_photo_cadre_register_7_button_img = Image.open(
            base.resourcePath(r"assets\register2Page\inputPhotoCadreStandardImg.png")).convert('RGBA')
        photo_img = l[1][0].convert('RGBA').resize((56,56))

        # Resize image
        input_photo_cadre_register_7_button_img = input_photo_cadre_register_7_button_img.resize((60, 60))

        # Create a mask to handle the transparency
        mask = input_photo_cadre_register_7_button_img.split()[3]
        mask2 = photo_img.split()[3]

        # Paste image onto new image, using mask
        emptyImg.paste(photo_img, (2, 2,58,58),mask2)
        emptyImg.paste(input_photo_cadre_register_7_button_img, (0, 0,60,60),mask)

        profile_label = Label(registerInfo.scrollable_frame, text="Profile photo :",font=("Montserrat", 8, "bold"),
                                                                 fg="#bb86fc",bg="#1f1a24",height=0,anchor=W)        # age_label = Label(registerInfo.scrollable_frame, text="Age :")

        profile_label.grid(row=1, column=1,padx=0,pady=0, sticky=W)

        # Create Label widget and assign image to it
        image_label = Label(registerInfo.scrollable_frame, bg="#1f1a24", anchor=W)
        image_label.grid(row=2, column=1, padx=10, rowspan=4, sticky=W)

        # Convert image to PhotoImage and resize it
        photo = ImageTk.PhotoImage(emptyImg.resize((60, 60)))
        base.global_photo = photo
        # Configure image_label to display the photo
        image_label.config(image=photo)
        print(photo.width(), photo.height())
        print(emptyImg.size, emptyImg.mode)

        registerInfo.canvas.create_image(100,100,image=ImageTk.PhotoImage(emptyImg))

        # next
        base.nextRegister6ButtonImg = Image.open(
            base.resourcePath("assets\general\\nextDisabledButtonImg.png"))
        base.nextRegister6Button = MyButton(base.Background, 340, 453, standardImg=base.nextRegister6ButtonImg,
                                            cursor="X_cursor")

        # submit
        base.submitRegister6ButtonImg = Image.open(
            base.resourcePath("assets\loginPage\submitButton.png"))
        base.submitRegister6Button = MyButton(base.Background, 221, 453, standardImg=base.submitRegister6ButtonImg,
                                              cursor="hand2",behavior=lambda :self.submit(base.getRegisterValues(),base))

        # back
        base.backRegister6ButtonImg = Image.open(
            base.resourcePath("assets\general\\backButtonStandardImg.png"))
        base.backRegister6Button = MyButton(base.Background, 141, 453, standardImg=base.backRegister6ButtonImg,
                                            cursor="hand2",behavior=base.register6ToRegister5)

        base.register6Group = MyWidgetsGroup(base.Background,registerInfo,base.register6WidgetsFrame,base.register6Title,base.confirmChoicesText,base.submitRegister6Button)

    def submit(self,values,base):
        try:
            student_inscription(values)
            messagebox.showinfo("Success", f"Submission done successfully")
            base.register6ToLogin()

        except :
            messagebox.showerror("Internal Error", f"Submission failed please try again")




