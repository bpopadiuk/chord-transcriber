"""
Implementation of the Goertzel Algorithm, used here to compute the relative 
magnitude of each frequency on the keyboard

Source for algorithm: Kevin Banks
https://www.embedded.com/design/configurable-systems/4024443/The-Goertzel-Algorithm

SAMPLE_RATE and WINDOW_SIZE are still works in progress. More research needs to
be done to identify optimal values. For now they're more or less voodoo constants
that seem to work the best for me thusfar. 
"""

import math
import numpy as np
from ChordNaming import name
from ProcessWav import processwav

# SAMPLE_RATE = 44800
# WINDOW_SIZE = 8192 

def goertzel_mag(numSamples, targetFreqs, sampleRate, data):
    scalingFactor = numSamples / 2.0
    numSamples = float(numSamples)
    magnitudes = []

    for freq in targetFreqs:
        k = int((0.5 + ((numSamples * freq) / sampleRate)))
        w = (2.0 * math.pi * k) / numSamples
        sine = math.sin(w)
        cosine = math.cos(w)
        coeff = 2.0 * cosine
        q0 = 0
        q1 = 0
        q2 = 0

        for i in range(int(numSamples)):
            q0 = coeff * q1 - q2 + data[i]
            q2 = q1
            q1 = q0

        real = (q1 - q2 * cosine) / scalingFactor
        imag = (q2 * sine) / scalingFactor
        freqMag = math.sqrt(real**2 + imag**2)

        magnitudes.append((freq, freqMag))
    return magnitudes 

#t = np.linspace(0, 1, SAMPLE_RATE)[:WINDOW_SIZE]
#sine_wave = np.sin(2*np.pi*440*t) + np.sin(2*np.pi*392*t) + np.sin(2*np.pi*261*t) + np.sin(2*np.pi*329*t)# should be 'F Major 7'
#sine_wave = np.sin(2*np.pi*1046*t) + np.sin(2*np.pi*1318*t) + np.sin(2*np.pi*1567*t) + np.sin(2*np.pi*1975*t)# should be 'C Major 7'
#sine_wave = np.sin(2*np.pi*233.08*t) + np.sin(2*np.pi*207.65*t) + np.sin(2*np.pi*138.59*t) + np.sin(2*np.pi*174.61*t)# should be 'Bb minor 7'
#sine_wave = sine_wave * np.hamming(WINDOW_SIZE)
#audio = processwav.process_wav()
#audio = audio * np.hamming(WINDOW_SIZE)

#freqs0 = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.3, 440.00, 466.16, 493.88]
#freqs1 = [1046.5, 1108.73, 1174.66, 1244.51, 1318.51, 1396.91, 1479.98, 1567.98, 1661.22, 1760.00, 1864.66, 1975.53]
#freqs2 = [130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94]
#freqs = freqs0 + freqs1 + freqs2

#mags = goertzel_mag(WINDOW_SIZE, freqs, SAMPLE_RATE, audio)

#mags.sort(key=lambda x : x[1], reverse=True)

#chord = set()
#magMin = min(mags, key=lambda x: x[1])[1]
#magMax = max(mags, key=lambda x: x[1])[1]
#magRange = magMax - magMin 
#for note, mag in mags:
#    if mag > magMax * 0.8:
#        chord.add(note)

#print('mags: \n', mags)
#chord = list(chord)
#name.process(chord)
