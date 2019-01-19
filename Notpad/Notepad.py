from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext

root = Tk(className="Notepad")
txtPad = scrolledtext.ScrolledText(root, width=100, height=80)

# creating a menu defination functions


def open_command():
    file = filedialog.askopenfile(
        parent=root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        txtPad.insert('1.0', contents)
        file.close()


def save_command():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        data = txtPad.get('1.0', END + '-lc')
        file.write(data)
        file.close()


def about_command():
    about_msg = messagebox.showinfo("About", "This text editor is for you.")


menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New")
file_menu.add_command(label="Open", command=open_command)
file_menu.add_command(label="Save", command=save_command)
file_menu.add_command(label="Exit", command=exit)

menu.add_cascade(label="Edit")
menu.add_cascade(label="View")

help_menu = Menu(menu)
menu.add_cascade(label="Help")

help_menu.add_command(label="About", command=about_command)

txtPad.pack(fill=X)
root.mainloop()
