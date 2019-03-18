# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:08:30 2019

@author: Sam Tyson Gasper
"""


import librosa
import random

# Arrays created in case enumerator solution doesn't work properly.
index = []
y_timings = []

# Random x coordinates for beat placements
x_coords = round(random.uniform(0.0, 1.0), 6)


y, sr = librosa.load(r"S:/Charts/Rigid/Song files/easy/MP3 files/SS2.mp3")


BPM = input("Enter BPM: ")


# Beat tracker
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, start_bpm=int(BPM))


#Convert beattracker frames to seconds
beat_times = librosa.frames_to_time(beats, sr=sr)
beat_list = list(enumerate(beat_times))

# for count, item in beat_list:
#     print(count, round(item, 6))


with open("testfile.txt", "w+") as file:
    file.write("VERSION 2\n")
    file.write("BPM " + str(round((tempo * 2), 6)) + '\n')
    file.write("PAGE_SHIFT " + str(round(beat_times[0], 6)) + '\n')
    file.write("PAGE_SIZE " + str(240/float(BPM)) + '\n')
    for count, item in beat_list:
        file.write("NOTE\t" + str(count) + '\t' + str(round(item, 6)) + '\t' + str(round(random.uniform(0.0, 1.0), 6)) + '\t' + "0.000000" + '\n')

    file.close()