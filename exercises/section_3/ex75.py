x = input('enter your word:  ')
while x == x[::-1]:
    print(f'{x} is a palidrome')
    break
else:
    print(f'{x} is not a palindrome')


