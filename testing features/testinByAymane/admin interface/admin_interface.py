import tkinter as tk

root = tk.Tk()
root.geometry("700x600")
root.title("application")

def data_student_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame,text='data students',font=('Bold',30))
    lb.pack()
    home_frame.pack(pady=20)
# definition des fonction pour chaque page de l'application( actually they are frams hhhh)
def delete_std_page():
    menu_frame = tk.Frame(main_frame) # creation d'une cadre a l'interieur du cadre principale
    lb = tk.Label(menu_frame,text='delete students',font=('Bold',30)) #ajouter un text
    lb.pack() # placememt du text dans le cadre
    menu_frame.pack(pady=20) # placement du cadre dans la cadre principale avec une espace ( =padding)

def noti_page():
    contact_frame = tk.Frame(main_frame)
    lb = tk.Label(contact_frame,text='Add notification',font=('Bold',30))
    lb.pack()
    contact_frame.pack(pady=20)

def change_Data_page():
    about_frame = tk.Frame(main_frame)
    lb = tk.Label(about_frame,text='Change data ',font=('Bold',30))
    lb.pack()
    about_frame.pack(pady=20)

def publication_page():
    about_frame = tk.Frame(main_frame)
    lb = tk.Label(about_frame,text='publicate a file ',font=('Bold',30))
    lb.pack()
    about_frame.pack(pady=20)


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy() # detruire chaque cadre

def hide_indicate():
    # Réinitialisation de la couleur de fond de toutes les étiquettes d'indication de page
    data_student_indicate.config(bg="#c3c3c3")
    delete_std_indicate.config(bg="#c3c3c3")
    add_noti_indicate.config(bg="#c3c3c3")
    change_data_indicate.config(bg="#c3c3c3")
    publicate_data_indicate.config(bg="#c3c3c3")

def indicate(lb,page):
    hide_indicate() # masquer toutes les etiquettes
    lb.config(bg='#158aff') # definir la couleur de fond  de l'etiquette d'indication de page selectionnee
    delete_pages() # detruire toutes les pages actuelles dans le cadre principale
    page() # Afficher la page sélectionnée dans le cadre principal



# Création du panneau d'options à gauche de la fenêtre principale
options_frame = tk.Frame(root,bg='#c3c3c3')

data_student_btn = tk.Button(options_frame,text='data std',font=('bold',15),
                     fg='#158aff',bd=0,bg='#c3c3c3', command=lambda :indicate(data_student_indicate,data_student_page))
data_student_btn.place(x=5,y=50)

data_student_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
data_student_indicate.place(x=3,y=50,width=5,height=40)


delete_std_btn = tk.Button(options_frame,text='delete std',font=('bold',15),
                     fg='#158aff',bd=0,bg='#c3c3c3', command=lambda :indicate(delete_std_indicate,delete_std_page))
delete_std_btn.place(x=5,y=100)

delete_std_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
delete_std_indicate.place(x=3,y=100,width=5,height=40)



add_noti_btn = tk.Button(options_frame,text='add noti',font=('bold',15),
                     fg='#158aff',bd=0,bg='#c3c3c3', command=lambda :indicate(add_noti_indicate,noti_page))
add_noti_btn.place(x=5,y=150)

add_noti_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
add_noti_indicate.place(x=3,y=150,width=5,height=40)


change_data_btn = tk.Button(options_frame,text='Chge data',font=('bold',15),
                     fg='#158aff',bd=0,bg='#c3c3c3', command=lambda :indicate(change_data_indicate,change_Data_page))
change_data_btn.place(x=0,y=200)

change_data_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
change_data_indicate.place(x=3,y=200,width=5,height=40)


publicate_data_btn = tk.Button(options_frame,text='pbl data',font=('bold',15),
                     fg='#158aff',bd=0,bg='#c3c3c3', command=lambda :indicate(publicate_data_indicate,publication_page))
publicate_data_btn.place(x=0,y=250)

publicate_data_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
publicate_data_indicate.place(x=3,y=250,width=5,height=40)




options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100,height=400)
main_frame = tk.Frame(root,highlightbackground='black',highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400,width=500)
root.mainloop()