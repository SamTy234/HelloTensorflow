
"""
Created on Thu Mar 21 02:02:42 2019

@author: Sam Tyson Gasper
"""
import librosa
import random
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
    bpm = bpm_entry.get()
    string_display = "Your estimated BPM is " + bpm
    label = Label(root)
    label["text"] = string_display
    label.grid(row=3, column=1)
    return bpm


def get_shift():
    shift = shift_entry.get()
    string_display = "Your current shift: " + shift
    label = Label(root)
    label["text"] = string_display
    label.grid(row=4, column=1)
    return shift


def calculate_bpm():
    bpm = round((tempo * 2), 6)
    return bpm


def calculate_shift():
    return round(onset_times[0], 6)


def random_x_generator():
    return round(random.uniform(0.1, 0.9), 6)


def calculate_page_size():
    return round((240 / float(calculate_bpm())), 6)


def determine_holds(item):
    if item in beat_times_harmonic:
        return round(random.uniform(0.0, 0.5), 6)
    else:
        return "0.000000"


def choose_between_auto_shift_or_user_shift():
    user_shift = get_shift()
    if user_shift is not None:
        return user_shift
    else:
        return calculate_shift()

def get_c1_file():
    global tempo, beat_times_percussive, beat_times_harmonic, onset_times
    # Load the file and separate into harmonics/Percussives
    y, sr = librosa.load(browse_file())
    #Label(root, text="File loaded successfully").grid(row=2, column=1)
    print("File loaded successfully")
    #Label(root, text="Separating Harmonics...").grid(row=3, column=1)
    print("Seperating Harmonic beats..")

    y_harmonic = librosa.effects.harmonic(y)
    # Label(root, text="Separating Percussives...").grid(row=4, column=1)
    print("Seperating percussives..")

    y_percussive = librosa.effects.percussive(y)
    # Label(root, text="Getting BPM...").grid(row=5, column=1)
    print("Getting BPM...")

    estimated_bpm = get_bpm()
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr, start_bpm=int(estimated_bpm))

    # Convert beat tracker frames to seconds
    # Label(root, text="Generating Beat times...").grid(row=6, column=1)
    print("Generating Beat times...")

    beat_times = librosa.frames_to_time(beats, sr=sr)
    beat_list = list(enumerate(beat_times))
    print("Beat times sucessfully converted to a list")


    # Onset tracker
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    # Convert percussive beat frames to seconds
    tempo, beat_frames_percussive = librosa.beat.beat_track(y=y_percussive, sr=sr)
    beat_times_percussive = librosa.frames_to_time(beat_frames_percussive, sr=sr)
    percussive_list = list(enumerate(beat_times_percussive))

    # Convert beattracker harmonic
    tempo, beat_frames_harmonic = librosa.beat.beat_track(y=y_harmonic, sr=sr)
    beat_times_harmonic = librosa.frames_to_time(beat_frames_harmonic, sr=sr)

    with open(save_filename(), "w+") as file:
        file.write("VERSION 2\n")
        file.write("BPM " + str(calculate_bpm()) + '\n')
        file.write("PAGE_SHIFT " + str(choose_between_auto_shift_or_user_shift()) + '\n')
        file.write("PAGE_SIZE " + str(calculate_page_size()) + '\n')
        for count, item in beat_list:
            file.write("NOTE\t" + str(count) + '\t' + str(round(item, 6)) + '\t' + str(
                random_x_generator()) + '\t' + '0.000000' + '\n')

        print("Chart done!")

        file.close()


root = Tk()
menubar = Menu(root)

root.config(menu=menubar)
root.geometry('350x150')

root.title('C1 Generator')

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
#subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

bpm_label = Label(root, text="Estimated BPM:").grid(row=0, column=0)
bpm_entry = Entry(root, bd=2)
bpm_entry.grid(row=0, column=1)
register_bpm_button = Button(root, text="Enter", command=lambda: get_bpm()).grid(row=0, column=2)

shift_label = Label(root, text="Shift Timestamp:").grid(row=1, column=0)
shift_entry = Entry(root, bd=2)
shift_entry.grid(row=1, column=1)
register_shift_button = Button(root, text="Enter", command=lambda: get_shift()).grid(row=1, column=2)

output_text_button = Button(root, text="Get your C1 file", command=lambda: get_c1_file())
output_text_button.grid(row=2, column=1)


root.mainloop()


