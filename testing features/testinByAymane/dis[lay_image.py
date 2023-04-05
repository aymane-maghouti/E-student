# import tkinter as tk
# from PIL import Image, ImageTk
# root = tk.Tk()
# root.title("dispaly image")
# root.geometry("300x150")
#
# # photo = tk.PhotoImage(file="logo-ensah.png")
#
# photo2 = Image.open("logo-ensah.png")
# resized_image = photo2.resize((300,150),Image.ANTIALIAS)
# converted_image = ImageTk.PhotoImage(resized_image)
#
#
#
# label = tk.Label(root, image = converted_image, width=300,height=150,
#                  bg="black",fg="yellow")
#
# label.pack()
#
# root.mainloop()



# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("logo-ensah.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

win.mainloop()
