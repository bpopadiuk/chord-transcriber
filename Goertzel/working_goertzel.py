import math
import numpy as np
from ChordNaming import name

SAMPLE_RATE = 44100
WINDOW_SIZE = 1024

def goertzel_mag(numSamples, targetFreq, sampRate, data):
    scalingFactor = numSamples / 2.0

    floatnumSamples = float(numSamples)
    k = int((0.5 + ((floatnumSamples * targetFreq) / sampRate)))
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

    magnitude = math.sqrt(real**2 + imag**2)
    return targetFreq, magnitude 

t = np.linspace(0, 1, SAMPLE_RATE)[:WINDOW_SIZE]
sine_wave = np.sin(2*np.pi*1318*t) + np.sin(2*np.pi*1396*t) + np.sin(2*np.pi*1760*t) + np.sin(2*np.pi*1046*t)# should be 'A Major
sine_wave = sine_wave * np.hamming(WINDOW_SIZE)

C = 1046.5 
Db = 1108.73
D = 1174.66
Eb = 1244.51
E = 1318.51
F = 1396.91
Fsharp = 1479.98
G = 1567.98
Ab = 1661.22
A = 1760.00
Bb = 1864.66
B = 1975.53

mags = []
mags.append(goertzel_mag(WINDOW_SIZE, C, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, Db, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, D, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, Eb, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, E, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, F, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, Fsharp, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, G, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, Ab, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, A, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, Bb, SAMPLE_RATE, sine_wave))
mags.append(goertzel_mag(WINDOW_SIZE, B, SAMPLE_RATE, sine_wave))


mags.sort(key=lambda x : x[1], reverse=True)

chord = set()
magRange = max(mags, key=lambda x: x[1])[1] - min(mags, key=lambda x: x[1])[1]
for note in mags:
    if note[1] > magRange / 2:
        chord.add(note[0])

chord = list(chord)
name.process(chord)
