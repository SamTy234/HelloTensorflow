import librosa
import random

# Arrays created in case enumerator solution doesn't work properly.
index = []
y_timings = []

# Random x coordinates for beat placements
x_coords = round(random.uniform(0.0, 1.0), 6)


y, sr = librosa.load("easy-song-1.wav")


BPM = input("Enter BPM: ")
offset = input("Enter offset: ")

# Beat tracker
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, start_bpm=BPM)


#Convert beattracker frames to seconds
beat_times = librosa.frames_to_time(beats, sr=sr)
beat_list = list(enumerate(beat_times))

# for count, item in beat_list:
#     print(count, round(item, 6))


with open("testfile.txt", "w+") as file:
    file.write("VERSION 2\n")
    file.write("BPM " + str(tempo * 2) + '\n')
    file.write("PAGE_SHIFT " + offset/1000 + '\n')
    file.write("PAGE_SIZE " + 240/float(offset) + '\n')
    for count, item in beat_list:
        file.write("NOTE\t" + str(count) + '\t' + str(round(item, 6)) + '\t' + str(x_coords) + '\t' + "0.000000" + '\n')

    file.close()
