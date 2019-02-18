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
    print(filename)

def save_file():
    global filesave
    filesave = filedialog.asksaveasfilename(initialdir = "/home/Documents", title = "Save your text file",
                                          filetypes=(("Text files", "*.txt"),("All files", "*.")))


def print_name():
    print("This is a test to check that the button works")

menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

outputTextButton = Button(root, text ="Get your text file", command= lambda : save_file())
outputTextButton.pack()

root.mainloop()