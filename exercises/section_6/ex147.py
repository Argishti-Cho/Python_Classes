import random
print('\n')
print('     WHAT IS YOURT NAME ???  ')
print('\n')
user_name = input('Enter your name here:  ')
print('\n')
print(f'     Hello {user_name} !!!')
print('\n')


card_1 = {'B': 2, 'I': 23, 'N': 44, 'G': 46, 'O': 67}
card_12 = {'I': 11, 'N': 24, 'G': 39, 'O': 52, 'B': 75}
card_13 = {'N': 8, 'G': 26, 'O': 40, 'B': 48, 'I': 64}
card_14 = {'G': 5, 'O': 29, 'B': 41, 'I': 54, 'N': 70}
card_15 = {'O': 14, 'B': 18, 'I': 37, 'N': 51, 'G': 66}

x = random.randrange(1, 76)
print(f'the number is {x}')

for k, v in card_1.items():
    if card_1[k] == x:
        card_1[k] = 'X'
for k, v in card_12.items():
    if card_12[k] == x:
        card_12[k] = 'X'
for k, v in card_13.items():
    if card_13[k] == x:
        card_13[k] = 'X'
for k, v in card_14.items():
    if card_14[k] == x:
        card_14[k] = 'X'
for k, v in card_15.items():
    if card_15[k] == x:
        card_15[k] = 'X'

for k, v in card_1.items():
    print(card_1[k], end='   |   ')
print('\n', '-' *40)
for k, v in card_12.items():
    print(card_12[k], end='   |   ')
print('\n', '-' *40)
for k, v in card_13.items():
    print(card_13[k], end='   |   ')
print('\n', '-' *40)
for k, v in card_14.items():
    print(card_14[k], end='   |   ')
print('\n', '-' *40)
for k, v in card_15.items():
    print(card_15[k], end='   |   ')

print('\n')
     
