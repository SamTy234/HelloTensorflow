import librosa

y, sr = librosa.load("easy-song-1.wav")

tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beats, sr=sr)

# onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
# onset_times = librosa.frames_to_time(onset_frames, sr=sr)


print(beat_times[:5])
# print(onset_times[:5])