import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.interpolate import splrep, splev

# Define the window
root = tk.Tk()
root.title("Statistiques d'accès à eServices")

# Original data
dates = np.array(['2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05'])
y = np.array([10, 20, 15, 25, 18])
labels = ['2023-03-01 \n nbr.Connexions 10', '2023-03-02 \n nbr.Connexions 20', '2023-03-03 \n nbr.Connexions 15',
          '2023-03-04 \n nbr.Connexions 25', '2023-03-04 \n nbr.Connexions 18']

# Smooth the data
dates_smooth = np.linspace(0, 4, 100)
spl = splrep(range(len(dates)), y)
y_smooth = splev(dates_smooth, spl)

# Plot the original data as a scatter plot
fig, ax = plt.subplots()
scatter = plt.scatter(dates, y)


def hover(event):
    vis = scatter.contains(event)[0]
    if vis:
        ind = scatter.contains(event)[1]["ind"][0]
        text.set_text(labels[ind])
        text.set_position((dates[ind], y[ind]))
        text.set_visible(True)
    else:
        text.set_visible(False)
    fig.canvas.draw_idle()


text = ax.text(0, 0, "", ha="center", va="center", backgroundcolor=(1, 1, 1, 0.7))

fig.canvas.mpl_connect("motion_notify_event", hover)

# Plot the smoothed line on top of the scatter plot
plt.plot(dates_smooth, y_smooth)

# Add labels and a title
plt.xlabel('Date')
plt.ylabel('Nbr.Connexion')
plt.title("Statistiques d'accès à eServices")

# Embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start the Tkinter event loop
tk.mainloop()
