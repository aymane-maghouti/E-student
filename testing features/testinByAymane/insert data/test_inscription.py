from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from student_registration import student_inscription
root = Tk()
root.withdraw()

file_path = askopenfilename()

img = Image.open(file_path)


img_bytes = img.tobytes()

#exemple de la liste retourne
l=[[-1,'aymane', 'Outmani', 'L122234', 'P112', 'Male', [2, 'March', 2002]],
   [img],
   ['Tanger', "Sc Mathematique 'B'", 'Spanish', '12', 'Al khawarizmi high school','State'],
   ['Av masira Nr22 ', 'App3 etage4', '98000', '0689', 'Taza', 'Morocco'],
   ['ossma.outmani@etu.uae.ac.ma', 'Nexos2002', 'Nexos2002']]




student_inscription(l)
print("done")