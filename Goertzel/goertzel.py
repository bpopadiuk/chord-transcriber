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

def goertzel_mag(numSamples, targetFreqs, sampleRate, data):
    scalingFactor = numSamples / 2.0
    numSamples = float(numSamples)
    magnitudes = []

    for freq in targetFreqs:
        k = int((0.5 + ((numSamples * freq) / sampleRate)))
        w = (2.0 * math.pi / numSamples) * k
        cosine = math.cos(w)
        sine = math.sin(w)
        coeff = 2.0 * cosine
        Q1 = 0
        Q2 = 0

        for i in range(int(numSamples)):
            Q0 = coeff * Q1 - Q2 + data[i]
            Q2 = Q1
            Q1 = Q0

        real = (Q1 - Q2 * cosine) / scalingFactor
        imag = (Q2 * sine) / scalingFactor
        freqMagnitude = math.sqrt(real**2 + imag**2)
        # "optimized" version:
        # freqMagnitude = math.sqrt(Q1**2 + Q2**2 - Q1 * Q2 * coeff)

        magnitudes.append((freq, freqMagnitude))
    return magnitudes 
