from PIL import Image,ImageTk
import numpy as np
import tkinter as tk
from admin import connectDB,delete_student


liste_images = []

# Create the main application window
root = tk.Tk()
root.geometry("600x500")
root.title("Gestion des étudiants")

# Create a frame to contain all the widgets
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=False)

# Create an entry widget to enter the class name
class_entry = tk.Entry(main_frame)
class_entry.pack(pady=10)



def Convert_IMG(binary_data):
    array = np.frombuffer(binary_data, dtype=np.uint8).reshape((60,60,3))
    return Image.fromarray(array)


# Get the class ID from the class name and display the students
def id_class():
    class_name = class_entry.get()
    class_id = -1
    if class_name == 'ID1' :
        class_id = 1
    elif class_name == 'ID2':
        class_id = 2
    elif class_name == 'GI1':
        class_id = 3
    elif class_name == 'GI2':
        class_id = 4
    elif class_name == 'GC1':
        class_id = 5
    elif class_name == 'GC2':
        class_id = 6
    elif class_name == 'GEER1':
        class_id = 7
    elif class_name == 'GEER2':
        class_id = 8
    display_students(class_id)





# Display the list of students for a given class
def display_students(class_id):
    global liste_images
    # Connect to the database
    my_conn, cursor = connectDB('student_managment')

    # Get the list of students for the given class
    cursor.execute("SELECT id_Student,firstname, lastname, image FROM student WHERE id_class = %s", (class_id,))
    students = cursor.fetchall()

    # Create a scrollable frame for displaying the students
    students_frame = tk.Frame(main_frame)
    students_frame.pack(side="left", fill="both", expand=False)
    canvas = tk.Canvas(students_frame, borderwidth=0, highlightthickness=0)
    scrollbar = tk.Scrollbar(students_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    scrollbar.config(troughcolor="blue")
    canvas.configure(yscrollcommand=scrollbar.set, background="pink")

    canvas.pack(side="left", fill="both", expand=False)
    scrollbar.pack(side="right", fill="y")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Update the scroll region when the size of the frame changes
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    scrollable_frame.bind("<Configure>", update_scrollregion)

    # Create the column headers in row 0
    tk.Label(scrollable_frame, text='Nom complet').grid(row=0, column=1)
    tk.Label(scrollable_frame, text='id').grid(row=0, column=2)
    tk.Label(scrollable_frame, text='Photo').grid(row=0, column=3)
    tk.Label(scrollable_frame,text='delete student').grid(row=0,column=4)

    for i, student in enumerate(students, start=1):
        imgobject = Convert_IMG(student[3])
        img = ImageTk.PhotoImage(imgobject)
        tk.Button(scrollable_frame, text="delete", command=lambda : delete_student(student[0])).grid(row=i, column=4)
        full_name = f"{student[1]} {student[2]}"
        tk.Label(scrollable_frame, text=full_name).grid(row=i, column=1, ipadx=20)
        tk.Label(scrollable_frame, text=student[0]).grid(row=i, column=2, ipadx=60)
        tk.Label(scrollable_frame, image=img).grid(row=i, column=3, ipady=7)
        liste_images.append(img)
    cursor.close()

# Create a button to display the list of students
display_button = tk.Button(main_frame, text="Afficher les étudiants", command=display_students)
display_button.pack(pady=10,expand=False)

# Start the main event loop
root.mainloop()
