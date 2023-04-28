from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from student_registration import student_inscription

root = Tk()
root.withdraw()

file_path = askopenfilename()

img = Image.open(file_path)
print(img)

#exemple de la liste retourne
l=[['aymane', 'Outmani', 'L1258', 'P112', 'Male', [2, 'March', 2002]],
   [img],
   ['Tanger', "Sc Mathematique 'B'", 'Spanish', '12', 'Al khawarizmi high school','State'],
   ['Av masira Nr22 ', 'App3 etage4', '98000', '0689', 'Taza', 'Morocco'],
   ['majid.outmani@etu.uae.ac.ma', 'Majid1234', 'Majid1234']]




student_inscription(l)
print("done")