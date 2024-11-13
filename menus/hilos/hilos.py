import tkinter as tk

def create_label(window, name):
    label = tk.Label(window, text=name)
    label.pack()

def create_window():
    window = tk.Tk()
    window.title("Nombres")

    names = ["Enrique", "Alan", "Wan", "Alex"]
    list(map(lambda name: create_label(window, name), names))

    window.mainloop()

create_window()