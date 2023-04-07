import tkinter as tk

root = tk.Tk()

top = tk.Toplevel(root)

# Remove the title bar and borders
top.overrideredirect(True)

# Set the transparency level (0=fully transparent, 1=fully opaque)
top.wm_attributes('-transparentcolor', '#ab23ff')

# Create a canvas with a transparent background
canvas = tk.Canvas(top, bg="blue", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Draw a transparent rectangle on the canvas
frame=tk.Frame(canvas,background="#ab23ff",width=400,height=100)
frame.pack()

# Add some content to the canvas
label = tk.Label(frame, text="Hello, world!", font=("Arial", 24))
label.place(relx=0.5, rely=0.5, anchor="center")


top.mainloop()
