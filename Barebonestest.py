from tkinter import *
from tkinter import filedialog

def browse_file():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a file",
                                          filetypes=(("Audio files", ".wav"),
                                                     ("Audio files", ".mp3"),
                                                     ("All files", "*.*")))
    print(filename)
    return filename


def save_filename():
    global file_save_name
    file_save_name = filedialog.asksaveasfilename(initialdir="/home/Documents",
                                                  defaultextension=".txt",
                                                  title="Save your text file",
                                                  filetypes=(("Text files", "*.txt"),
                                                             ("All files", "*.")))
    print(file_save_name)
    return file_save_name

def get_bpm():
    text = bpm_entry.get()
    print(text)
    return text

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

root.geometry('350x350')
root.title('C1 Generator')

subMenu = Menu(menubar, tearoff=0)


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

bpm_label = Label(root, text="Estimated BPM:").grid(row=0, column=0)
bpm_entry = Entry(root, bd=2)
bpm_entry.grid(row=0, column=1)

register_bpm_button = Button(root, text="Enter", command=lambda: get_bpm()).grid(row=0, column=2)

output_text_button = Button(root, text="Get your C1 file", command=lambda: save_filename())
output_text_button.grid(row=1, column=1)


root.mainloop()