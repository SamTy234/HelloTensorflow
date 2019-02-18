from tkinter import *
from tkinter import filedialog

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

root.geometry('350x350')
root.title('test')

subMenu = Menu(menubar, tearoff=0)

def browse_file():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file",
                                          filetypes= (("Audio files", "*.wav"),("All files", "*.*")))

menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

root.mainloop()