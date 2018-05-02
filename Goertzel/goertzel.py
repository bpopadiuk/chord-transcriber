"""
Implementation of the Goertzel Algorithm, used here to compute the relative 
magnitude of each frequency on the keyboard

Code based on pseudocode in this article:
https://www.embedded.com/design/configurable-systems/4024443/The-Goertzel-Algorithm

SAMPLE_RATE and WINDOW_SIZE are still works in progress. I need to do more research to
identify optimal values. For now they're more or less voodoo constants
that seem to work the best for frequency resolution thus far. 
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
