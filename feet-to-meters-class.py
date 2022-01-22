from tkinter import *
from tkinter import ttk


class FeetToMeters:
  # defining the initiation of the class
    def __init__(self, root):
        # naming the window
        root.title("Feet to Meters")

        # frame is what "hold" the widgets
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        # sticky configure the way column/row will expand if a blank space is avaliable
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # row/column configure tell that the frame should expand with extra space
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # here we set the var that will receive the entry and where the widget will be
        self.feet = StringVar()
        feetEntry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feetEntry.grid(column=2, row=1, sticky=(W, E))

        # setting meters var
        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(
            column=2, row=2, sticky=W)

        # setting buttons and texts
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(
            column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(
            column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        # adding padding to each child of mainframe
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # for start focus on the entry and to click "Enter" and calculate
        feetEntry.focus()
        root.bind("<Return>", self.calculate)

  # defining the extra function
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass


root = Tk()
# calling the class and passing the root
FeetToMeters(root)
root.mainloop()
