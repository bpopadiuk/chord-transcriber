import sys
import name_chord

def process(freqs):
    notes = []
    bass = float(freqs[0])
    for i in range(len(freqs)):
        frequency = float(freqs[i])
        notes.append(compute_note(frequency))
        if frequency < bass:
            bass = frequency
    chord = name_chord.name_chord(notes) 
    bass = name_chord.noteLetters[compute_note(bass)]
    print('Chord: ', chord)
    print('Bass: ', bass)

def compute_note(f_n):
    """Convert f_n (frequency in Hz) to an int 0-11 corresponding 
       to each musical note in the western chromatic scale"""
    A440 = 9 
    f_0 = 440.0
    a = 1.059463094359
    half_steps_away = log10(f_n/f_0) / log10(a)
    return int(round((A440 + half_steps_away) % 12)) % 12

if __name__ == "__main__":
    notes = []
    bass = float(sys.argv[1])
    for i in range(1, len(sys.argv)):
        frequency = float(sys.argv[i])
        notes.append(freq_to_degrees.compute_note(frequency))
        if frequency < bass:
            bass = frequency
    chord = name_chord.name_chord(notes) 
    bass = name_chord.noteLetters[freq_to_degrees.compute_note(bass)]
    print('Chord: ', chord)
    print('Bass: ', bass)
