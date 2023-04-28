from tkinter import *

def show_details(details):
    root1 = Tk()
    root1.geometry('200x200')
    paragraph = details
    n = len(paragraph)
    label =Label(root1, text=paragraph, wraplength=n, anchor="nw", justify='left')
    label.pack()
    required_height = label.winfo_reqheight()
    label.config(height=required_height)

    root1.mainloop()


def show(notifications):
    root = Tk()
    root.geometry('800x200')
    root.title("Affichage")

    # Create a canvas and add it to the root window
    canvas = Canvas(root, width=600, height=500)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Create a frame to hold the table
    table_frame = Frame(canvas)
    table_frame.pack(fill=BOTH, expand=1)

    # Add the table frame to the canvas
    canvas.create_window(0, 0, anchor=NW, window=table_frame)

    # Add a scrollbar to the canvas
    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Bind the canvas to the scrollbar
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all"), yscrollincrement=5))



    texts=[]
    buttons=[]
    # Add the data to the table
    for i in range(len(notifications)):
        text_length = len(notifications[i][0])
        text_width = 30
        num_lines = int(text_length / text_width) + (1 if text_length % text_width else 0)

        text = Text(table_frame,width=text_width,height=num_lines, takefocus=False,cursor="hand2")
        text.bind("<Button-1>",lambda event,i=i:print(f"{notifications[i][1]}"))
        texts.append(text)
        text.insert(END, f'{notifications[i][0]}')
        text.configure(state='disabled')
        text.grid(row=(2 * i), column=0)
        Button(table_frame, text=f'{notifications[i][1]}', command=lambda i=i: show_details(notifications[i][2]), width=15, height=2).grid(row=(2*i)+1, column=0)
    root.mainloop()
l=[['avis', '2023-04-24 23:54:45', 'ashauschc\ndsdvsvv\nds\n'], ['Avis aux élèves ingénhhhhhhhhhhhhhhhhhhhhhhhhhhhhhieursssssssssssssssss ID1', '2023-04-02 13:12:34', 'Il est porté à la connaissance des élèves ingénieurs de la première année Ingénieurie des données (ID1) que leDS du module Data Mining aura lieu le Jeudi 12/04/2023 à 09h00 à l’amphi A.']]
show(l)