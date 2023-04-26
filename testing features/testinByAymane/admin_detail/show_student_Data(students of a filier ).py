import tkinter as tk


root = tk.Tk()
root.geometry("600x500")
root.title("application")


def id1_students_page():
    import mysql.connector
    import io
    from PIL import Image, ImageTk
    # import tkinter as tk

    # database connection
    my_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MG1234",
        database="gestion_etudiant"
    )
    cursor = my_conn.cursor()

    cursor.execute("SELECT full_name,age,image FROM students where filier='ID' ")
    my_row = cursor.fetchall()

    # create Tkinter window and frame
    id1_students_frame = tk.Frame(main_frame)
    id1_students_frame.pack(side="left", fill="both", expand=True)
    canvas = tk.Canvas(id1_students_frame, borderwidth=0, highlightthickness=0)
    scrollbar = tk.Scrollbar(id1_students_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", update_scrollregion)

    # Column headers row 0
    l1 = tk.Label(scrollable_frame, text='Nom complet')
    l1.grid(row=0, column=1)

    l2 = tk.Label(scrollable_frame, text='Âge')
    l2.grid(row=0, column=2)

    l3 = tk.Label(scrollable_frame, text='Photo')
    l3.grid(row=0, column=3)

    i = 1  # data starts from row 1
    images = []  # to manage garbage collection.

    for student in my_row:
        stream = io.BytesIO(student[2])
        img = Image.open(stream)
        img = ImageTk.PhotoImage(img)
        e = tk.Label(scrollable_frame, text=student[0])
        e.grid(row=i, column=1, ipadx=20)
        e = tk.Label(scrollable_frame, text=student[1])
        e.grid(row=i, column=2, ipadx=60)
        e = tk.Label(scrollable_frame, image=img)
        e.grid(row=i, column=3, ipady=7)
        images.append(img)  # garbage collection
        i = i + 1

    cursor.close()

    root.mainloop()


def gi1_students_page():
    import mysql.connector
    import io
    from PIL import Image, ImageTk
    import tkinter as tk

    # database connection
    my_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MG1234",
        database="gestion_etudiant"
    )
    cursor = my_conn.cursor()

    cursor.execute("SELECT full_name,age,image FROM students where filier='GI' ")
    my_row = cursor.fetchall()

    # create Tkinter window and frame
    gi1_students_frame = tk.Frame(main_frame)
    gi1_students_frame.pack(side="left", fill="both", expand=True)
    canvas = tk.Canvas(gi1_students_frame, borderwidth=0, highlightthickness=0)
    scrollbar = tk.Scrollbar(gi1_students_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", update_scrollregion)

    # Column headers row 0
    l1 = tk.Label(scrollable_frame, text='Nom complet')
    l1.grid(row=0, column=1)

    l2 = tk.Label(scrollable_frame, text='Âge')
    l2.grid(row=0, column=2)

    l3 = tk.Label(scrollable_frame, text='Photo')
    l3.grid(row=0, column=3)

    i = 1  # data starts from row 1
    images = []  # to manage garbage collection.

    for student in my_row:
        stream = io.BytesIO(student[2])
        img = Image.open(stream)
        img = ImageTk.PhotoImage(img)
        e = tk.Label(scrollable_frame, text=student[0])
        e.grid(row=i, column=1, ipadx=20)
        e = tk.Label(scrollable_frame, text=student[1])
        e.grid(row=i, column=2, ipadx=60)
        e = tk.Label(scrollable_frame, image=img)
        e.grid(row=i, column=3, ipady=7)
        images.append(img)  # garbage collection
        i = i + 1

    cursor.close()

    root.mainloop()



def gc1_students_page():
    import mysql.connector
    import io
    from PIL import Image, ImageTk
    import tkinter as tk

    # database connection
    my_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MG1234",
        database="gestion_etudiant"
    )
    cursor = my_conn.cursor()

    cursor.execute("SELECT full_name,age,image FROM students where filier='GC' ")
    my_row = cursor.fetchall()

    # create Tkinter window and frame
    gc1_students_frame = tk.Frame(main_frame)
    gc1_students_frame.pack(side="left", fill="both", expand=True)
    canvas = tk.Canvas(gc1_students_frame, borderwidth=0, highlightthickness=0)
    scrollbar = tk.Scrollbar(gc1_students_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", update_scrollregion)

    # Column headers row 0
    l1 = tk.Label(scrollable_frame, text='Nom complet')
    l1.grid(row=0, column=1)

    l2 = tk.Label(scrollable_frame, text='Âge')
    l2.grid(row=0, column=2)

    l3 = tk.Label(scrollable_frame, text='Photo')
    l3.grid(row=0, column=3)

    i = 1  # data starts from row 1
    images = []  # to manage garbage collection.

    for student in my_row:
        stream = io.BytesIO(student[2])
        img = Image.open(stream)
        img = ImageTk.PhotoImage(img)
        e = tk.Label(scrollable_frame, text=student[0])
        e.grid(row=i, column=1, ipadx=20)
        e = tk.Label(scrollable_frame, text=student[1])
        e.grid(row=i, column=2, ipadx=60)
        e = tk.Label(scrollable_frame, image=img)
        e.grid(row=i, column=3, ipady=7)
        images.append(img)  # garbage collection
        i = i + 1

    cursor.close()

    root.mainloop()

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy() # detruire chaque cadre

def hide_indicate():
    # Réinitialisation de la couleur de fond de toutes les étiquettes d'indication de page
    id1_students_indicate.config(bg="#c3c3c3")
    gc1_students_indicate.config(bg="#c3c3c3")
    gi1_students_indicate.config(bg="#c3c3c3")


def indicate(lb,page):
    hide_indicate() # masquer toutes les etiquettes
    lb.config(bg='#158aff') # definir la couleur de fond  de l'etiquette d'indication de page selectionnee
    delete_pages() # detruire toutes les pages actuelles dans le cadre principale
    page() # Afficher la page sélectionnée dans le cadre principal



# Création du panneau d'options à gauche de la fenêtre principale
options_frame = tk.Frame(root,bg='#c3c3c3')

id1_students_btn = tk.Button(options_frame,text='ID1',font=('bold',15),
                     fg='#158aff',bd=0,bg='#c3c3c3', command=lambda :indicate(id1_students_indicate,id1_students_page))
id1_students_btn.place(x=5,y=50)

id1_students_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
id1_students_indicate.place(x=3,y=50,width=5,height=40)

gc1_students_btn = tk.Button(options_frame,text='CG1',font=('bold',15),
                     fg='#158aff',bd=0,bg='#c3c3c3', command=lambda :indicate(gc1_students_indicate,gc1_students_page))
gc1_students_btn.place(x=5,y=100)

gc1_students_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
gc1_students_indicate.place(x=3,y=100,width=5,height=40)



gi1_students_btn = tk.Button(options_frame,text='GI1',font=('bold',15),
                     fg='#158aff',bd=0,bg='#c3c3c3', command=lambda :indicate(gi1_students_indicate,gi1_students_page))
gi1_students_btn.place(x=5,y=150)

gi1_students_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
gi1_students_indicate.place(x=3,y=150,width=5,height=40)



options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100,height=400)
main_frame = tk.Frame(root,highlightbackground='black',highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400,width=500)
root.mainloop()