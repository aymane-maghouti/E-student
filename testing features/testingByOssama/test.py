import tkinter as tk

def change_cursor(event):
    event.widget.config(cursor="hand2")

def restore_cursor(event):
    event.widget.config(cursor="")

def sign_up(name):
    # Code to execute when clicking on the text
    print(f"{name} signed up!")

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

def create_text():
    text = canvas.create_text(
        215, 208,
        text="Sign up",
        font=("Montserrat", 8, "underline"),
        fill="#bb86fc",
        anchor=tk.NW,
        activefill="white"
    )

    canvas.tag_bind(text, "<Enter>", change_cursor)
    canvas.tag_bind(text, "<Leave>", restore_cursor)
    canvas.tag_bind(text, "<Button-1>", lambda event: sign_up("Alice"))

    return text

text = create_text()

def recreate_text():
    global text
    canvas.delete(text)
    text = create_text()

button = tk.Button(root, text="Recreate Text", command=recreate_text)
button.pack()

root.mainloop()
