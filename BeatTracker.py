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


# Load the file and separate into harmonics
y, sr = librosa.load(r"S:/Charts/Rigid/Song files/easy/MP3 files/SS2.mp3")
y_harmonic = librosa.effects.harmonic(y)


BPM = input("Enter BPM: ")


# Beat tracker
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, start_bpm=int(BPM))

#Onset tracker
onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
onset_times = librosa.frames_to_time(onset_frames, sr=sr)

#Convert beattracker frames to seconds
beat_times = librosa.frames_to_time(beats, sr=sr)
beat_list = list(enumerate(beat_times))

#Convert beattracker harmonic
beat_frames_harmonic = librosa.beat.beat_track(y=y_harmonic, sr=sr)
beat_times_harmonic = librosa.frames_to_time(beat_frames_harmonic, sr=sr)

# for count, item in beat_list:
#     print(count, round(item, 6))


def CalculateBPM():
    return round((tempo * 2), 6)


def CalculateShift():
    return round(beat_times[0], 6)


def RandomXGenerator():
    return round(random.uniform(0.1, 0.9), 6)


def CalculatePageSize():
    return 240 / float(BPM)

# def DetermineHolds():


with open("testfile.txt", "w+") as file:
    file.write("VERSION 2\n")
    file.write("BPM " + str(CalculateBPM()) + '\n')
    file.write("PAGE_SHIFT " + str(CalculateShift()) + '\n')
    file.write("PAGE_SIZE " + str(CalculatePageSize()) + '\n')
    for count, item in beat_list:
        file.write("NOTE\t" + str(count) + '\t' + str(round(item, 6)) + '\t' + str(
            RandomXGenerator()) + '\t' + "0.000000" + '\n')

    file.close()

