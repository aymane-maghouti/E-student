from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

root = Tk()
image = PhotoImage(file='vector2.png')

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(True)

root.config(background="#2F6C60")

welcome_label = Label(text="M|O - services", bg="#2F6C60",font=("Trebuchet Ms",15,"bold"),fg="#FFFFFF")
welcome_label.place(x=130,y=25)

bg_label = Label(root, image=image, bg="#2F6C60")
bg_label.place(x=130,y=65)


progress_label = Label(root, text="Loading...",font=("Trebuchet Ms",15,"bold"),fg="#FFFFFF",bg="#2F6C60")
progress_label.place(x=190,y=330)

progress = ttk.Style()
progress. theme_use('clam')
progress.configure("red.Horizontal.TProgressbar", background = "#108cff")

progress = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate', style="red.Horizontal.TProgressbar")
progress.place(x=60,y=370)


def top():
    root.withdraw()
    os.system("python test2.py")
    root.destroy()


i=0


def load():
    global i
    if i<=10:
        txt = 'Loading... '+(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(600,load)
        progress['value'] = 10*i
        i+= 1
    else :
        top()



load()

root.resizable(False, False)
root.mainloop()
