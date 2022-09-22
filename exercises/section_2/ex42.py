
C4_f = 261.63
D4_f = 293.66
E4_f = 329.63
F4_f = 349.23
G4_f = 392.00
A4_f = 440.00
B4_f = 493.88

notes = input('Enter the note in format C4:  ')

note = notes[0]
octave = int(notes[1])

if note == 'C':
    freq = C4_f
elif note == 'D':
    freq = D4_f
else:
    print('errir')

freq = freq / 2 ** (4 - octave)
print(f'the frequanecy of {notes} is {freq}')
