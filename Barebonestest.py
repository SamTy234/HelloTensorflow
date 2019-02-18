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

def save_filename():
    global filesavename
    filesavename = filedialog.asksaveasfilename(initialdir = "/home/Documents", title = "Save your text file",
                                          filetypes=(("Text files", "*.txt"),("All files", "*.")))
    print(filesavename)

def save_the_actual_file():
    textfilename = input("Enter file name: ")
    open(textfilename + ".txt", "wt")

def print_name():
    print("This is a test to check that the button works")

menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

outputTextButton = Button(root, text ="Get your text file", command= lambda : save_the_actual_file())
outputTextButton.pack()

root.mainloop()