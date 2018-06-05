import math
import numpy as np
from ChordNaming import name
from ProcessWav import processwav
from Goertzel import goertzel
from AudioInput import record_wav 

SAMPLE_RATE = 48000
WINDOW_SIZE = 16384
DEVICE_INDEX = 0
LOOP = 1
HEADER = "\n***CHORD***           ***BASS***          ***NOTES***        \n- - - - - -          - - - - - -          - - - - - -"

def menu():
    while(1):
        userInput = input("\n0: Exit\n1: Transcribe a Chord\n-> ")
        if userInput == 0 or userInput == 1:
            break
        else:
            continue
    return userInput

record_wav.device_menu()
DEVICE_INDEX = input('-> ')
while(1):
    LOOP = menu()
    if LOOP == 0:
        quit() 
    wav = record_wav.capture(DEVICE_INDEX)
    data = processwav.process_wav()
    data = data * np.blackman(WINDOW_SIZE) # Exact Blackman instead of Hamming taper function -- offers more precision

    octave0 = [130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94]
    octave1 = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.3, 440.00, 466.16, 493.88]
    octave2 = [523.25, 554.37, 587.33, 622.25, 659.25, 698.46, 739.99, 783.99, 830.61, 880.00, 932.33, 987.77]
    octave3 = [1046.5, 1108.73, 1174.66, 1244.51, 1318.51, 1396.91, 1479.98, 1567.98, 1661.22, 1760.00, 1864.66, 1975.53]
    freqs = octave0 + octave1 + octave2 + octave3
    #freqs = octave1 + octave2

    mags = goertzel.goertzel_mag(WINDOW_SIZE, freqs, SAMPLE_RATE, data)

    mags.sort(key=lambda x : x[1], reverse=True)

    chord = [] 
    magMin = min(mags, key=lambda x: x[1])[1]
    magMax = max(mags, key=lambda x: x[1])[1]
    magRange = magMax - magMin
    for note, mag in mags:
        if mag > magMax * 0.1:
            chord.append(note)

    notes = [name.noteLetters[name.compute_note(x)] for x in chord]
    #for i in range(len(mags)):
    #    print(notes[i], mags[i])
#    print('\n')
    #print(set([name.noteLetters[name.compute_note(x)] for x in chord]))
    chord, bass = name.process(chord)
    print(HEADER)
    print('{}          {}          {}'.format(chord.ljust(11), bass.ljust(11), notes[:4]))
