import random

draw_list = random.sample(range(1, 76), 75)
card = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
minimum = 1
maximum = 15    

for letter in card:
    card[letter] = random.sample(range(minimum, maximum), 5)
    minimum += 15
    maximum += 15
# print(card)
# for letter in card:
    print(letter, end='\t')
    for number in card[letter]:
        print(number, end='\t')
    print('\n')
# print('\n')