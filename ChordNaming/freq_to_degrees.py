from math import log10
import sys
import name_chord

A440 = 9

def compute_note(f_n):
    f_0 = 440.0
    a = 1.059463094359
    half_steps_away = log10(f_n/f_0) / log10(a)
    return int(round((A440 + half_steps_away) % 12)) % 12

#C = 130.81
#Gsharp = 103.83
#D = 293.66
#B = 123.47
#Bb = 58.27
#Fsharp = 92.5
#G = 3135.96
#F = 349.23
#A = 7040
#Csharp = 1108.73
#Eb = 155.56

#print('C: ', compute_note(C))
#print('G#: ', compute_note(Gsharp))
#print('D: ', compute_note(D))
#print('B: ', compute_note(B))
#print('Bb: ', compute_note(Bb))
#print('F#: ', compute_note(Fsharp))
#print('G: ', compute_note(G))
#print('F: ', compute_note(F))
#print('A: ', compute_note(A))
#print('C#: ', compute_note(Csharp))
#print('Eb: ', compute_note(Eb))

if __name__ == "__main__":
    notes = []
    for i in range(1, len(sys.argv)):
        notes.append(compute_note(float(sys.argv[i])))
    chord = name_chord.name_chord(notes) 
    print(chord)
