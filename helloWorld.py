from tkinter import *
from tkinter import ttk

# main window of a application
root = Tk()
root.title("Hello World!")

# frame is used to contain other widgets
frame = ttk.Frame(root, padding=10)
frame.grid()

ttk.Label(frame, text="Teste").grid(column=0, row=0)

root.mainloop()
