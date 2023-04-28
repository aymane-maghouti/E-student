import tkinter as tk

root = tk.Tk()

# create a Text widget with a fixed width
text = tk.Text(root, width=50)

# disable the ability of the parent widget to shrink to fit its contents
root.pack_propagate(False)

# set the text widget to expand to fill the entire parent widget
text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
