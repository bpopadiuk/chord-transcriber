from math import log10
import name_chord

def compute_note(f_n):
    """Convert f_n (frequency in Hz) to an int 0-11 corresponding 
       to each musical note in the western chromatic scale"""
    A440 = 9
    f_0 = 440.0
    a = 1.059463094359
    half_steps_away = log10(f_n/f_0) / log10(a)
    return int(round((A440 + half_steps_away) % 12)) % 12
