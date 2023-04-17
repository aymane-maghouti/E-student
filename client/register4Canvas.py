from CanvasToWidget import *
import tkinter as tk


def createRegister4(base):
    # base=tk.Tk()
    # base.Background=tk.Canvas()
    try:
        base.nextRegister3Button.place_forget()
    except:
        pass

    try:
        base.backRegister4Button.place_forget()
    except:
        pass

    base.config(cursor="arrow")
    base.register4WidgetsImg = tk.PhotoImage(
        file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\register1Page\registerFrame.png")
    base.register4WidgetsFrame = base.Background.create_image(55, 136, image=base.register3WidgetsImg, anchor=tk.NW)
    base.register4Title = base.Background.create_text(94, 158, text="Create your account",
                                                      font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)

    # option menu list
    base.menuRegister2MidStandardlImg = Image.open(
        r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionMidStandardImg.png")
    base.menuRegister2MidHoverImg = Image.open(
        r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionMidHoverImg.png")

    base.menuRegister2MidClickedImg = Image.open(
        r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionMidClickedImg.png")

    base.menuListRegister2MidStandardImg = Image.open(
        r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\optionlistMidStandardImg.png")

    # email
    base.emailRegister4Text = base.Background.create_text(115, 241, text="Email address",
                                                             font=("Montserrat", 6, "bold"),
                                                             fill="#bb86fc", anchor=tk.NW)
    base.emailRegister4Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                           font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                           highlightthickness=0, borderwidth=0, width=36)
    base.emailRegister4StandardObject = MyEntry(base.Background, 94, 254, entry=base.emailRegister4Entry,
                                                   standardImg=base.emailLogingStandardlImg,
                                                   hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                   placeholder="exemple@etu.uae.ac.ma")

    # password
    base.passwordRegister4Text = base.Background.create_text(115, 292, text="Password",
                                                             font=("Montserrat", 6, "bold"),
                                                             fill="#bb86fc", anchor=tk.NW)
    base.passwordRegister4Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                           font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                           highlightthickness=0, borderwidth=0, width=36,show="*")
    base.passwordRegister4StandardObject = MyEntry(base.Background, 94, 305, entry=base.passwordRegister4Entry,
                                                   standardImg=base.emailLogingStandardlImg,
                                                   hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                   placeholder="***********")

    # password confirmation
    base.confirmRegister4Text = base.Background.create_text(115, 343, text="Confirm password",
                                                             font=("Montserrat", 6, "bold"),
                                                             fill="#bb86fc", anchor=tk.NW)
    base.confirmRegister4Entry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
                                           font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
                                           highlightthickness=0, borderwidth=0, width=36, show="*")
    base.pconfirmRegister4StandardObject = MyEntry(base.Background, 94, 356, entry=base.confirmRegister4Entry,
                                                   standardImg=base.emailLogingStandardlImg,
                                                   hoverImg=base.emailLogingHoverImg, marginX=21, marginY=5,
                                                   placeholder="***********")

    # next
    base.nextRegister4ButtonImg = Image.open(
        r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\nextDisabledButtonImg.png")
    base.nextRegister4Button = MyButton(base.Background, 340, 453, standardImg=base.nextRegister4ButtonImg,
                                        cursor="X_cursor", behavior=lambda :print("hi"))

    # submit
    base.submitRegister4ButtonImg = Image.open(
        r"C:\Users\ID 1\tkinterTest\E-student\client\assest\loginPage\submitButton.png")
    base.submitRegister4Button = MyButton(base.Background, 221, 453, standardImg=base.submitRegister4ButtonImg,
                                          cursor="hand2")

    # back
    base.backRegister4ButtonImg = Image.open(
        r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\backButtonStandardImg.png")
    base.backRegister4Button = MyButton(base.Background, 141, 453, standardImg=base.backRegister4ButtonImg,
                                        cursor="hand2", behavior=base.register3ToRegister2)

    base.register3Group = MyWidgetsGroup(base.Background, base.register3Title, base.postalRegisterText,
                                         base.postalRegisterEntry, base.postalRegisterStandardObject,
                                         base.phoneRegisterText, base.phoneRegisterEntry,
                                         base.phoneRegisterStandardObject, base.cityRegister3Text,
                                         base.cityRegister3Label, base.cityRegister3List, base.countryRegister3Text,
                                         base.countryRegister3Label, base.countryRegister3List,
                                         base.address1Register3Text, base.address1Register3StandardObject,
                                         base.address2Register3Text, base.address2Register3StandardObject)


