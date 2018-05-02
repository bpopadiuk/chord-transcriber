import math
import numpy as np
from ChordNaming import name
from ProcessWav import processwav
from Goertzel import goertzel
from AudioInput import record_wav 

SAMPLE_RATE = 44800
WINDOW_SIZE = 8192 

#t = np.linspace(0, 1, SAMPLE_RATE)[:WINDOW_SIZE]
#sine_wave = np.sin(2*np.pi*440*t) + np.sin(2*np.pi*392*t) + np.sin(2*np.pi*261*t) + np.sin(2*np.pi*329*t)# should be 'F Major 7'
#sine_wave = np.sin(2*np.pi*1046*t) + np.sin(2*np.pi*1318*t) + np.sin(2*np.pi*1567*t) + np.sin(2*np.pi*1975*t)# should be 'C Major 7'
#sine_wave = np.sin(2*np.pi*233.08*t) + np.sin(2*np.pi*207.65*t) + np.sin(2*np.pi*138.59*t) + np.sin(2*np.pi*174.61*t)# should be 'Bb minor 7'
#sine_wave = sine_wave * np.hamming(WINDOW_SIZE)
wav = record_wav.capture()
data = processwav.process_wav()
data = data * np.hamming(WINDOW_SIZE)

octave0 = [1046.5, 1108.73, 1174.66, 1244.51, 1318.51, 1396.91, 1479.98, 1567.98, 1661.22, 1760.00, 1864.66, 1975.53]
octave1 = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.3, 440.00, 466.16, 493.88]
octave2 = [130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94]
freqs = octave0 + octave1 + octave2

mags = goertzel.goertzel_mag(WINDOW_SIZE, freqs, SAMPLE_RATE, data)

mags.sort(key=lambda x : x[1], reverse=True)

chord = set()
magMin = min(mags, key=lambda x: x[1])[1]
magMax = max(mags, key=lambda x: x[1])[1]
magRange = magMax - magMin
for note, mag in mags:
    if mag > magMax * 0.25:
        chord.add(note)

print('mags: \n', mags)
print('\n')
chord = list(chord)
name.process(chord)