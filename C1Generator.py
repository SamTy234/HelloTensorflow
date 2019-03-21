
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
    text = bpm_entry.get()
    print(text)
    return text


def calculate_bpm():
    bpm = round((tempo * 2), 6)
    return bpm


def calculate_shift():
    return round(beat_times_percussive[0], 6)


def random_x_generator():
    return round(random.uniform(0.1, 0.9), 6)


def calculate_page_size():
    return round((240 / float(calculate_bpm())), 6)


def determine_holds(item):
    if item in beat_times_harmonic:
        return round(random.uniform(0.0, 0.5), 6)
    else:
        return "0.000000"


def generate_text_file():
    with open(save_filename(), "w+") as file:
        file.write("VERSION 2\n")
        file.write("BPM " + str(calculate_bpm()) + '\n')
        file.write("PAGE_SHIFT " + str(calculate_shift()) + '\n')
        file.write("PAGE_SIZE " + str(calculate_page_size()) + '\n')
        for count, item in beat_list:
            file.write("NOTE\t" + str(count) + '\t' + str(round(item, 6)) + '\t' + str(
                random_x_generator()) + '\t' + str(determine_holds(item)) + '\n')

        file.close()


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
output_text_button = Button(root, text="Get your C1 file", command=lambda: generate_text_file())
output_text_button.grid(row=1, column=1)





# Load the file and separate into harmonics/Percussives
y, sr = librosa.load(browse_file())
print("loaded file successfully")
print("Separating into harmonics...")
y_harmonic = librosa.effects.harmonic(y)
print("Separating into percussives....")
y_percussive = librosa.effects.percussive(y)

print("Getting BPM....")

estimated_bpm = get_bpm()

tempo, beats = librosa.beat.beat_track(y=y, sr=sr, start_bpm=int(estimated_bpm))

# Convert beat tracker frames to seconds
beat_times = librosa.frames_to_time(beats, sr=sr)
beat_list = list(enumerate(beat_times))

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

root.mainloop()






















