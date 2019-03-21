# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:08:30 2019
@author: Sam Tyson Gasper
"""


import librosa
import random
import Barebonestest

# Load the file and separate into harmonics
y, sr = librosa.load(r"S:/Charts/Rigid/Song files/easy/MP3 files/SS2.mp3")
y_harmonic = librosa.effects.harmonic(y)
y_percussive = librosa.effects.percussive(y)

estimated_bpm = input("Enter BPM: ")


# Beat tracker
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, start_bpm=int(estimated_bpm))

#Onset tracker
onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
onset_times = librosa.frames_to_time(onset_frames, sr=sr)

#Convert percussive beat frames to seconds
tempo, beat_frames_percussive = librosa.beat.beat_track(y=y_percussive, sr=sr)
beat_times_percussive = librosa.frames_to_time(beat_frames_percussive, sr=sr)
percussive_list = list(enumerate(beat_times_percussive))

#Convert beattracker frames to seconds
beat_times = librosa.frames_to_time(beats, sr=sr)
beat_list = list(enumerate(beat_times))

#Convert beattracker harmonic
tempo, beat_frames_harmonic = librosa.beat.beat_track(y=y_harmonic, sr=sr)
beat_times_harmonic = librosa.frames_to_time(beat_frames_harmonic, sr=sr)

# for count, item in beat_list:
#     print(count, round(item, 6))


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


with open("ss2chart.txt", "w+") as file:
    file.write("VERSION 2\n")
    file.write("BPM " + str(calculate_bpm()) + '\n')
    file.write("PAGE_SHIFT " + str(calculate_shift()) + '\n')
    file.write("PAGE_SIZE " + str(calculate_page_size()) + '\n')
    for count, item in beat_list:
        file.write("NOTE\t" + str(count) + '\t' + str(round(item, 6)) + '\t' + str(
            random_x_generator()) + '\t' + str(determine_holds(item)) + '\n')

    file.close()
