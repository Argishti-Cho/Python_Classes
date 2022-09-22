# is there any way to shorten the first if statement like all vowels in 1 variable?

letter = str(input('enter the any letter of the alphabet: '))

if letter == 'a' or letter == 'e' or letter == 'u' or letter == 'i' or letter == 'o':
    print(f'{letter} is vowel')
elif letter == 'y':
    print(f'{letter} is sometimes vowel and sometimes consonant')
else:
    print(f'{letter} is consonant')