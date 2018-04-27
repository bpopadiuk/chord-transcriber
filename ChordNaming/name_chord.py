def closed_voicing(notes):
    """Rearrange notes to a 'closed voicing', i.e. in ascending order as close together
       as possible"""

    notes.sort() # sort notes in ascending order
    bass = 0 
    minGap = (notes[-1] - notes[0]) % 12 
    for i in range(1, len(notes)):          # for every note, check gap between note and previous note (outter voices)
        gap = (notes[i-1] - notes[i]) % 12
        if gap < minGap:                    # set current note as minGap, meaning this is the tightest voicing so far
            bass = i
            minGap = gap
        else:
            continue

    return notes[bass:] + notes[:bass]      # return notes in ascending order starting from the selected bass note

def interval_sequence(chord):
    """Build an ordered list of the intervals between each note of the closed voicing --
       Return as int"""

    intervals = []
    for i in range(len(chord) - 1): 
        intervals.append((chord[i+1] - chord[i]) % 12) 
    return int(''.join(str(x) for x in intervals))  # return list as an integer (used as key to chordQualities dict())

def name_chord(notes):
    """Take list of notes represented as ints 0-11, calculate closed voicing and 
       interval sequence. Query chordQualities and noteLetters to name the chord"""

    voicing = closed_voicing(notes) # convert original voicing to closed voicing
    sequence = interval_sequence(voicing) # calculate interval sequence and save as int
    if sequence in chordQualities.keys():
        root_degree = voicing[chordQualities[sequence][1]] # find degree of root note
    else:   
        return 'CHORD UKNOWN'
    note_letter = noteLetters[root_degree] # fetch letter name of root
    chord_quality = chordQualities[sequence][0] # fetch chord quality
    return note_letter + ' ' + chord_quality
    

chordQualities = {33:('diminished', 0), 34:('minor', 0), 43:('Major', 0), 44:('augmented', 0), 
233:('half diminished', 1), 333:('fully diminished', 0), 332:('dominant 7', 3), 341:('Major 7', 3), 
143:('Major 7', 1), 323:('minor 7', 2), 422:('augmented-7', 3), 224:('augmented-7', 2)}

noteLetters = {0:'C', 1:'D flat', 2:'D', 3:'E flat', 4:'E', 5:'F', 6:'F sharp', 7:'G', 
8:'A flat', 9:'A', 10:'B flat', 11:'B'}
