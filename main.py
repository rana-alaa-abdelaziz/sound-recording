import pyaudio
import wave

frames_per_buffer= 3200  # Record in buffer of 3200 samples (memory)
format= pyaudio.paInt32 #32 bit per sample
channels= 1
sample_rate= 16000

p= pyaudio.PyAudio() #pyaudio object
stream= p.open(format= format,
            channels= channels,
            rate= sample_rate,
            input= True, #to capture audio
            frames_per_buffer= frames_per_buffer)


print("Start Recording")

seconds=5
frames=[]

# Store data in buffer for 5 seconds
for i in range(0, int(sample_rate / frames_per_buffer * seconds)):
    data = stream.read(frames_per_buffer)  #read 3200 frame at each iteration
    frames.append(data)

print("Finished Recording")

stream.stop_stream()
stream.close()
p.terminate()

wf= wave.open("record.wav", "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(sample_rate)

wf.writeframes(b''.join(frames)) #############
wf.close()
#Step 2

import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from scipy.io import wavfile

sample_rate, audio_data = wavfile.read('record.wav')

lowcut = 1000
highcut = 700
order = 4
nyquist = 0.5 * sample_rate  #max frequency
low = lowcut / nyquist
high = highcut / nyquist
b, a = scipy.signal.butter(order, [low, high], btype='band') #band pass

filtered_audio = scipy.signal.lfilter(b, a, audio_data)

wavfile.write('record_filtered.wav', sample_rate, np.int16(filtered_audio/np.max(np.abs(filtered_audio))*32767))
#to ensure audio data is within range of 16 bit ,convert from float to int to store

# Plot the original and filtered signals
plt.plot(audio_data, label='Original')
plt.plot(filtered_audio, label='Filtered')
plt.legend()
plt.show()

import speech_recognition as sr
audio = sr.AudioFile("record_filtered.wav")
r = sr.Recognizer()

with audio as s:

    audio_data = r.record(s)

text = r.recognize_google(audio_data=audio_data,language='en-US')
print(text)
