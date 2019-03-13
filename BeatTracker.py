import librosa
import random

# Arrays created in case enumerator solution doesn't work properly.
index = []
y_timings = []

# Random x coordinates for beat placements
x_coords = round(random.uniform(0.0, 1.0), 6)


y, sr = librosa.load("easy-song-1.wav")

# Beat tracker
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
print(tempo)
print(beats[:5])

#Convert beattracker frames to seconds
beat_times = librosa.frames_to_time(beats, sr = sr)
beat_list = list(enumerate(beat_times))

# for count, item in beat_list:
#     print(count, round(item, 6))

with open("testfile.txt", "w+") as file:
    file.write("VERSION 2\n")
    file.write("BPM " + str(tempo) + '\n')
    file.write("PAGE_SHIFT " + "12.5\n")
    file.write("PAGE_SIZE " + "12.5\n")
    for count, item in beat_list:
        file.write("NOTE\t" + str(count) + '\t' + str(round(item, 6)) + '\t' + str(x_coords) + '\t' + "0.000000" + '\n')

    file.close()
