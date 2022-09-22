
dict = {}
# word = 'exercises'
word = input('Enter any word without spaces:  ')
for letter in word:
    dict[letter] = word.count(letter)
print(dict)
