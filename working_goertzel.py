import math
import numpy as np
from ChordNaming import name

SAMPLE_RATE = 44100
WINDOW_SIZE = 1024

def goertzel_mag(numSamples, targetFreqs, sampRate, data):
    scalingFactor = numSamples / 2.0
    floatnumSamples = float(numSamples)
    magnitudes = []

    for freq in targetFreqs:
        k = int((0.5 + ((floatnumSamples * freq) / sampRate)))
        omega = (2.0 * math.pi * k) / floatnumSamples
        sine = math.sin(omega)
        cosine = math.cos(omega)
        coeff = 2.0 * cosine
        q0 = 0
        q1 = 0
        q2 = 0

        for i in range(numSamples):
            q0 = coeff * q1 - q2 + data[i]
            q2 = q1
            q1 = q0

        real = (q1 - q2 * cosine) / scalingFactor
        imag = (q2 * sine) / scalingFactor
        freqMag = math.sqrt(real**2 + imag**2)

        magnitudes.append((freq, freqMag))
    return magnitudes 

t = np.linspace(0, 1, SAMPLE_RATE)[:WINDOW_SIZE]
sine_wave = np.sin(2*np.pi*1318*t) + np.sin(2*np.pi*1396*t) + np.sin(2*np.pi*1760*t) + np.sin(2*np.pi*1046*t)# should be 'F Major 7'
sine_wave = sine_wave * np.hamming(WINDOW_SIZE)

freqs = [1046.5, 1108.73, 1174.66, 1244.51, 1318.51, 1396.91, 1479.98, 1567.98, 1661.22, 1760.00, 1864.66, 1975.53]
mags = goertzel_mag(WINDOW_SIZE, freqs, SAMPLE_RATE, sine_wave)

#mags.sort(key=lambda x : x[1], reverse=True)

chord = set()
magRange = max(mags, key=lambda x: x[1])[1] - min(mags, key=lambda x: x[1])[1]
for note, mag in mags:
    if mag > magRange / 2:
        chord.add(note)

chord = list(chord)
name.process(chord)
