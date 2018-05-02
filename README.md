# chord-trancriber

Chord Transcriber is a tool to transcribe musical chords from audio input. This is a work in progress. 

Simply run main.py while playing a chord. The program uses PyAudio to record audio with the built-in
microphone and tries to identify the chord. So far the program does best with sine wave or saw wave
synthesized audio. The success rate is best for fairly tight chord voicings in the octave below middle C. 
Single-note identification is quite good for the entire keyboard, and has even proven accurate for input
from a cello. 
