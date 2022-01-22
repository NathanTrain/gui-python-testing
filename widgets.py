from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Testing Widgets")

mainFrame = ttk.Frame(root, padding=20)
mainFrame.grid(column=1, row=1, sticky=(N, W, E, S))

ttk.Label(mainFrame, text="Frame:").grid(column=1, row=1, sticky=W)
ttk.Label(mainFrame, text="Label (text and image):").grid(
    column=1, row=3, sticky=W)
ttk.Label(mainFrame, text="Button:").grid(column=1, row=5, sticky=W)
ttk.Label(mainFrame, text="CheckButton:").grid(
    column=1, row=8, sticky=W)
ttk.Label(mainFrame, text="RatioButton:").grid(
    column=1, row=10, sticky=W)
ttk.Label(mainFrame, text="Entry:").grid(column=1, row=13, sticky=W)
ttk.Label(mainFrame, text="ComboBox:").grid(column=1, row=16, sticky=W)

# frame
widget_frame = ttk.Frame(mainFrame, width=100, height=20)
widget_frame["borderwidth"] = 5
widget_frame["relief"] = "raised"
widget_frame.grid(column=3, row=2, sticky=E)

# label
widget_label_text = ttk.Label(mainFrame, text="Hello World!")
widget_label_text.grid(column=3, row=4, sticky=E)

# button
widget_button = ttk.Button(
    mainFrame, text="Hi")
widget_button.grid(column=3, row=6, sticky=E)
# using Enter on keyboard to press the button
root.bind("<Return>", lambda e: widget_button.invoke())

widget_button_disabled = ttk.Button(mainFrame, text="Disabled")
widget_button_disabled.state(["disabled"])
widget_button_disabled.grid(column=3, row=7, sticky=E)

# checkbutton
free = BooleanVar()
widget_checkbtn = ttk.Checkbutton(
    mainFrame, text="Free?", variable=free, onvalue=True, offvalue=False)
widget_checkbtn.grid(column=3, row=9, sticky=E)

# radiobutton
language = StringVar()
english = ttk.Radiobutton(
    mainFrame, text="English", variable=language, value="english")
portuguese = ttk.Radiobutton(
    mainFrame, text="Portuguese", variable=language, value="portuguese")
english.grid(column=3, row=11)
portuguese.grid(column=3, row=12)

# entry
ttk.Label(mainFrame, text="Username:").grid(column=2, row=14, sticky=E)
ttk.Label(mainFrame, text="Password:").grid(column=2, row=15, sticky=E)

username = StringVar()
password = StringVar()
usernameWidget = ttk.Entry(mainFrame, textvariable=username)
passwordWidget = ttk.Entry(mainFrame, textvariable=password, show="*")
usernameWidget.grid(column=3, row=14, sticky=E)
passwordWidget.grid(column=3, row=15, sticky=E)

# ComboBox
day = StringVar()
widget_combobox = ttk.Combobox(
    mainFrame, textvariable=day, state="readonly")
dayList = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
widget_combobox["values"] = dayList
widget_combobox.grid(column=3, row=17, sticky=E)

quitButton = ttk.Button(
    mainFrame, text="Quit", command=root.destroy).grid(column=2, row=18, sticky=(W, E, S))
# using Enter on keyboard to press the button
root.bind("<Return>", lambda e: root.destroy)

for child in mainFrame.winfo_children():
    child.grid_configure(padx=2, pady=2)

root.mainloop()
