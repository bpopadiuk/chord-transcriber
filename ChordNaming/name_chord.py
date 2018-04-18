def closed_voicing(notes):
    notes.sort()
    bass = 0
    minGap = (notes[-1] - notes[0]) % 12 
    for i in range(1, len(notes)):
        gap = (notes[i-1] - notes[i]) % 12
        if gap < minGap:
            bass = i
            minGap = gap
        else:
            continue

    return notes[bass:] + notes[:bass]

def interval_sequence(chord):
    intervals = []
    for i in range(len(chord) - 1): 
        intervals.append((chord[i+1] - chord[i]) % 12) 
    return int(''.join(str(x) for x in intervals))

def name_chord(notes):
    voicing = closed_voicing(notes) # convert original voicing to closed voicing
    sequence = interval_sequence(voicing) # calculate interval sequence and save as int
    if sequence in chordQualities.keys():
        root_degree = voicing[chordQualities[sequence][1]] # find degree of root note
    else:   
        return 'CHORD UKNOWN'
    note_letter = noteLetters[root_degree] # fetch letter name of root
    chord_quality = chordQualities[sequence][0] # fetch chord quality
    return note_letter + ' ' + chord_quality
    

chordQualities = {34:('minor', 0), 43:('Major', 0), 44:('augmented', 0), 233:('half diminished', 1), 333:('fully diminished', 0), 332:('dominant 7', 3), 341:('Major 7', 3), 143:('Major 7', 1), 323:('minor 7', 2), 422:('augmented-7', 3), 224:('augmented-7', 2)}

noteLetters = {0:'C', 1:'D flat', 2:'D', 3:'E flat', 4:'E', 5:'F', 6:'F sharp', 7:'G', 8:'A flat', 9:'A', 10:'B flat', 11:'B'}

#bMinor = [2,11,6]
#cMajor = [7,0,4]
#cHalfdim = [10,6,3,0]
#cFulldim = [0,3,6,9]
#cDom7 = [4,0,10,7]
#cMajor7 = [0,4,7,11]
#cMinor7 = [0,3,7,10]

#bMinor = closed_voicing(bMinor)
#cMajor = closed_voicing(cMajor)
#cHalfdim = closed_voicing(cHalfdim)
#cFulldim = closed_voicing(cFulldim)
#cDom7 = closed_voicing(cDom7)
#cMajor7 = closed_voicing(cMajor7)
#cMinor7 = closed_voicing(cMinor7)

#bMinorints = interval_sequence(bMinor)
#cMajorints = interval_sequence(cMajor)
#cHalfdimints = interval_sequence(cHalfdim)
#cFulldimints = interval_sequence(cFulldim)
#cDom7ints = interval_sequence(cDom7)
#cMajor7ints = interval_sequence(cMajor7)
#cMinor7ints = interval_sequence(cMinor7)

#misteryChord = [7,3,2,10]
#print('mistery chord ' , misteryChord, ': ')
#print(name_chord(misteryChord))
#chord1 = [7, 4, 0, 9]
#print(chord1, name_chord(chord1))
#chord2 = [5, 7, 2, 11]
#print(chord2, name_chord(chord2))
#chord3 = [6, 9, 3, 0]
#print(chord3, name_chord(chord3))
#chord4 = [8, 0, 5]
#print(chord4, name_chord(chord4))
#chord5 = [10, 5, 2]
#print(chord5, name_chord(chord5))
#chord6 = [6,10,1]
#print(chord6, name_chord(chord6))
#chord7 = [4,8,11,2]
#print(chord7, name_chord(chord7))
#chord8 = [1, 5, 8, 0]
#print(chord8, name_chord(chord8))
#chord9 = [0, 4, 8]
#print(chord9, name_chord(chord9))
#chord10 = [9, 1, 5, 7]
#print(chord10, name_chord(chord10))

#print('C minor 7: ', name_chord(cMinor7))
#print('C Dom: ', name_chord(cDom7))

#print('Voicings: \n')
#print('B minor: ', bMinor)
#print('C Major: ', cMajor)
#print('C Half dim: ', cHalfdim)
#print('C Full dim: ', cFulldim)
#print('C7: ', cDom7)
#print('C Maj 7: ', cMajor7)
#print('C min 7: ', cMinor7)

#print('Interval codes: \n')
#print('B minor: ', bMinorints)
#print('C Major: ', cMajorints)
#print('C Half dim: ', cHalfdimints)
#print('C Full dim: ', cFulldimints)
#print('C7: ', cDom7ints)
#print('C Maj 7: ', cMajor7ints)
#print('C min 7: ', cMinor7ints)
