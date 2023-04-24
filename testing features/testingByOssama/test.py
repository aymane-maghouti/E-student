from tkinter import *

root = Tk()

# create a frame with a scrollbar
canvas = Canvas(root)
scrollable_frame = Frame(canvas)

# add some widgets to the frame
Label(scrollable_frame, text="Column 1", width=15, height=5, bg="red").grid(row=0, column=0, padx=5, pady=5)
Label(scrollable_frame, text="Column 2", width=25, height=5, bg="green").grid(row=0, column=1, padx=5, pady=5)
Label(scrollable_frame, text="Column 3", width=35, height=5, bg="blue").grid(row=0, column=2, padx=5, pady=5)
Label(scrollable_frame, text="Science mathematique A", font=("Montserrat", 8, "bold"), fg="white", bg="#1f1a24", width=30, justify=CENTER).grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

# pack the frame and scrollbar
scrollable_frame.pack()
canvas.pack(side="left", fill="both", expand=True)
root.mainloop()
