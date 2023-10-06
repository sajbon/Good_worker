import tkinter as tk
import surveillance


class Menu:
    def __init__(self, root):
        start = tk.Button(root, text="Start", padx=50)
        start.place(x=300, y=300, anchor="center")

        l = tk.Label(
            root,
            text="Aby zacząć działanie programu GOOD_WORKER proszę nacisnąć na guzik start",
            font=("Arial", 12),
        )
        l.place(x=300, y=120, anchor="center")

        start.config(
            command=lambda: [
                Menu.close_root(start, l),
                surveillance.Surveillance(root),
            ]
        )

    def close_root(start, l):
        start.destroy()
        l.destroy()
