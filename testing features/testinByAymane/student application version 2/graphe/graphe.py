import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import splrep, splev
from helper import get_data
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def show_graph():
    root = tk.Tk()
    root.title("Statistiques d'accès à eServices")

    nb_visiteurs , dates = get_data()
    labels = []
    for i in range(len(nb_visiteurs)):
        label = f"{dates[i]} \n nbr.Connexions {nb_visiteurs[i][0]}"
        labels.append(label)




    dates_smooth = np.linspace(0, 4, 100)
    spl = splrep(range(len(dates)), nb_visiteurs)
    y_smooth = splev(dates_smooth, spl)

    fig , ax = plt.subplots()
    scatter = plt.scatter(dates, nb_visiteurs)

    def hover(event):
        vis = scatter.contains(event)[0]
        if vis:
            ind = scatter.contains(event)[1]["ind"][0]
            text.set_text(labels[ind])
            text.set_position((dates[ind], nb_visiteurs[ind]))
            text.set_visible(True)
        else:
            text.set_visible(False)
        fig.canvas.draw_idle()

    text = ax.text(0, 0, "", ha="center", va="center", backgroundcolor=(1, 1, 1, 0.7))

    fig.canvas.mpl_connect("motion_notify_event", hover)

    plt.plot(dates_smooth, y_smooth)

    plt.xlabel('')
    plt.ylabel('')
    plt.title("Statistiques d'accès à eServices")


    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    root.mainloop()


show_graph()