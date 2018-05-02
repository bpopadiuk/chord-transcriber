# chord-trancriber

Chord Transcriber is a tool to transcribe musical chords from audio input. This is a work in progress. 

Run main.py while playing a chord. The program uses PyAudio to record audio with the built-in
microphone and tries to identify the chord.

So far this thing does best with sine wave or saw wave synthesized audio. 
The success rate is best for fairly tight chord voicings in the octave below middle C. 
Single-note identification is quite good for the entire keyboard.

I've also had a fair bit of success identifying single notes from a cello, an electric bass and my voice. 
