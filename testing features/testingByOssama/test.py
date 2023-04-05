import tkinter as tk


class CustomWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # Set the window size and position
        self.geometry("400x300+100+100")
        # Remove the window manager decorations
        self.overrideredirect(True)
        # Create a frame to hold the minimize button
        self.minimize_frame = tk.Frame(self, bg="#666")
        self.minimize_frame.pack(side="top", fill="x")
        # Create the minimize button
        self.minimize_button = tk.Button(self.minimize_frame, text="-", font=("Arial", 16), width=2, bd=0, bg="#666",
                                         fg="white", command=self.minimize)
        self.minimize_button.pack(side="right")

    def minimize(self):
        # Hide the window
        self.withdraw()

    def restore(self):
        # Show the window
        self.deiconify()


# Create a custom window
window = CustomWindow()

# Add widgets to the window
label = tk.Label(window, text="Hello, World!", font=("Arial", 24))
label.pack(pady=50)

# Create a button to restore the window
restore_button = tk.Button(window, text="Restore", font=("Arial", 16), width=10, bd=0, bg="#666", fg="white",
                           command=window.restore)
restore_button.pack(pady=10)

# Start the main loop
window.mainloop()
