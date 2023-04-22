from CanvasToWidget import *
import tkinter as tk
from tkinter import filedialog
from io import BytesIO
import os

def checkPhoto(self,labelName):
    if self.photoVar==None:
        print(f"invalide {labelName}")
        return False
    filename, extension = os.path.splitext(os.path.basename(self.photopath))
    if extension not in [".jpg",".jpeg"]:
        print(f"invalide {labelName}")
        return False
    print(f"valide {labelName}")
    return True


def checkRegister2Form(self,register):
    valide=True
    register.values=[]
    for element in self.components:
        try:
            if not element.validate():
                valide=False
        except Exception as e:
            print(e)

            continue
        register.values.append(element.get())
    print(register.values)

    return valide

class Register2:
    def __init__(self):
        self.photoVar = None
        self.photopath=None

        self.values=[]

    def removePhoto(self,source):
        source.inputPhotoRegister2Button.setImage(self, ImageTk.PhotoImage(source.inputPhotoRegister2ButtonImg),value=None)
        print(self.photoVar)
        self.photopath=None
    def importPhoto(self,base):
        image_path = filedialog.askopenfilename()
        self.photopath=image_path
        print(image_path)
        filename, extension = os.path.splitext(os.path.basename(self.photopath))
        if extension not in [".jpg", ".jpeg"]:
            print(f"please a valid extension")
            return 1

        # Lire les données de l'image et les stocker sous forme de bytes
        try:
            with open(image_path, "rb") as f:
                image_bytes = f.read()
        except FileNotFoundError:
            return 1
        img_stream = BytesIO(image_bytes)
        image = Image.open(img_stream)

        faces=base.detectFaces(image)
        if len(faces)!=1:
            print("please choose another image")
            return 1

        resized=base.cropFace(image,faces)
        facesResized=base.detectFaces(resized)
        base.drawFace(resized,facesResized)
        photo=Image.fromarray(resized)
        # # Ouvrir l'image avec Pillow
        # photo = Image.open(img_stream)
        base.inputPhotoRegister2Button.setImage(self,ImageTk.PhotoImage(photo))
        print(self.photoVar)


    def createRegister2(self, base):
        # base=tk.Tk()
        # base.Background=tk.Canvas()
        base.config(cursor="arrow")

        try:
            base.nextRegister1Button.place_forget()
        except:
            pass
        try:
            base.backRegister3Button.place_forget()
        except:
            pass
        try:
            base.backRegister1Button.place_forget()
        except:
            pass
        try:
            base.nextRegister3Button.place_forget()
        except:
            pass

        base.config(cursor="arrow")

        base.loginWidgetsImg = tk.PhotoImage(
            file=r"C:\Users\ID 1\tkinterTest\E-student\client\assest\register1Page\registerFrame.png")
        base.register1WidgetsFrame = base.Background.create_image(55, 136, image=base.loginWidgetsImg, anchor=tk.NW)
        base.register1Title = base.Background.create_text(94, 158, text="Create your account",
                                                          font=("Montserrat", 23, "bold"), fill="white", anchor=tk.NW)


        base.photoRegisterText = base.Background.create_text(115, 241, text="Profile image",
                                                                 font=("Montserrat", 6, "bold"), fill="#bb86fc",
                                                                 anchor=tk.NW)

        #import
        base.importRegister2ButtonImg = Image.open(
           base.resourcePath("assest/register2Page/importRegister2StandardImg.png"))
        base.importRegister2ClickedButtonImg = Image.open(
           base.resourcePath("assest/register2Page/importRegisterClickedImg.png"))
        base.importRegister2Button = MyButton(base.Background, 191, 254, standardImg=base.importRegister2ButtonImg,clickImg=base.importRegister2ClickedButtonImg,
                                            cursor="hand2",behavior=lambda :self.importPhoto(base))

        #remove
        base.removeRegister2ButtonImg = Image.open(
           base.resourcePath("assest/register2Page/removeRegisterStandardImg.png"))
        base.removeRegister2ClickedButtonImg = Image.open(
           base.resourcePath("assest/register2Page/removeRegisterClickedImg.png"))
        base.removeRegister2Button = MyButton(base.Background, 280, 254, standardImg=base.removeRegister2ButtonImg,clickImg=base.removeRegister2ClickedButtonImg,
                                            cursor="hand2", behavior=lambda :self.removePhoto(base))

        #Input photo
        base.inputPhotoRegister2ButtonImg = Image.open(
           base.resourcePath("assest/register2Page/inputPhotoStandardImg.png"))
        base.inputPhotoRegister2Button = MyButton(base.Background, 223, 322, standardImg=base.inputPhotoRegister2ButtonImg if self.photoVar==None else self.photoVar,
                                            cursor="hand2",behavior=lambda :self.importPhoto(base))

        #Input cadre
        base.inputPhotoCadreRegister2ButtonImg = Image.open(
           base.resourcePath("assest/register2Page/inputPhotoCadreStandardImg.png"))
        base.inputPhotoCadreRegister2Button = MyButton(base.Background, 220, 319, standardImg=base.inputPhotoCadreRegister2ButtonImg,
                                            cursor="hand2", behavior=lambda:print("hi"))
        base.inputPhotoCadreRegister2Button.get=lambda :self.photoVar
        base.inputPhotoCadreRegister2Button.validate=lambda :checkPhoto(self,"Profile photo")


        # Firstname
        #
        # base.firstNameRegisterEntry = tk.Entry(base.Background, border=0, bg="#1f1a24", fg="white",
        #                                        font=("Montserrat", 10, "bold"), disabledbackground="#1f1a24",
        #                                        highlightthickness=0, borderwidth=0, width=12,
        #                                        textvariable=self.firstNameVar)
        # try:
        #     self.firstNameModified = base.firstNameRegisterStandardObject.getModified()
        # except:
        #     pass
        # base.firstNameRegisterStandardObject = MyEntry(base.Background, 94, 254, entry=base.firstNameRegisterEntry,
        #                                                standardImg=base.inputSmallStandardlImg,
        #                                                hoverImg=base.inputSmallHoverImg, marginX=21, marginY=5,
        #                                                placeholder="Ossama", modified=self.firstNameModified,value=self.firstNameVar)
        # base.firstNameRegisterStandardObject.validate=lambda :checkLenght(base.firstNameRegisterStandardObject,4,"first name")
        # print(self.firstNameModified)



        base.register2Form = MyForm(base,base.inputPhotoCadreRegister2Button)
        base.register2Form.validate=lambda:checkRegister2Form(base.register2Form,self)
        # submi
        base.nextRegister2ButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\nextButtonStandardImg.png")
        base.nextRegister2Button = MyButton(base.Background, 340, 453, standardImg=base.nextRegister2ButtonImg,
                                            cursor="hand2", behavior=base.register2ToRegister3)

        base.backRegister2ButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\backButtonStandardImg.png")
        base.backRegister2Button = MyButton(base.Background, 141, 453, standardImg=base.backRegister2ButtonImg,
                                            cursor="hand2", behavior=base.register2ToRegister1)

        base.submitLoginButtonImg = Image.open(
            r"C:\Users\ID 1\tkinterTest\E-student\client\assest\general\submitDisabledButtonImg.png")
        base.submitRegister2Button = MyButton(base.Background, 221, 453, standardImg=base.submitLoginButtonImg,
                                              cursor="X_cursor")

        base.register2Group = MyWidgetsGroup(base.Background,base.photoRegisterText,base.submitRegister2Button,base.inputPhotoCadreRegister2Button,base.inputPhotoRegister2Button,base.removeRegister2Button,base.importRegister2Button )


        # base.register1Group.validate=lambda:checkRegister1Form(base.register1Group)

        # base.emailLogingStandardObject.validate=lambda:check_email(base.emailLogingStandardObject)
