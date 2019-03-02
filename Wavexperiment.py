import wave
import matplotlib.pyplot as plt
from scipy.io import wavfile


samplerate, data = wavfile.read("easy-song-1.wav")
x = wave.open("easy-song-1.wav", 'rb')

allparams = x.getparams()
readframes = [x.readframes(1), x.readframes(2), x.readframes(3), x.readframes(4), x.readframes(5)]

# Stack overflow this later
bitrate = str((x.getframerate() * x.getsampwidth() * 8 * x.getnchannels()) / 1000)

print(bitrate)

plt.plot(data)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Test title")


print("All params: " + str(allparams))
print("Frames: " + str(readframes))