from tkinter import *

top = Tk()

menubar = Menu(top)

menubar.add_command(label="File", command=quit)

top.config(menu=menubar)

top.mainloop()
