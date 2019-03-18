from tkinter import *
from tkinter import filedialog
import os

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

# This saves the file that doesn't exist. Returns File path name
def save_filename():
    global filesavename
    filesavename = filedialog.asksaveasfilename(initialdir="/home/Documents", defaultextension=".txt",title="Save your text file",
                                                filetypes=(("Text files", "*.txt"),("All files", "*.")))
    
    # filesavename = filedialog.asksaveasfilename(confirmoverwrite='w', defaultextension=".txt")
    # if filesavename is None:
    #     return
    #
    # filesavename.write(" ")
    # filesavename.close()


    # print(filesavename)



#This actually works but is a roundabout method.
def save_the_damn_file():
    textfilename = input("Enter file name: ")
    open(textfilename + ".txt", "wt")

def print_name():
    print("This is a test to check that the button works")

menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

outputTextButton = Button(root, text="Get your text file", command=lambda : save_filename())
outputTextButton.pack()

root.mainloop()