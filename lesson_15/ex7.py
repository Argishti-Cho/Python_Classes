# x = '7, 8, 89, 10, -41, -10, 0'
x = input('Enter number separated with spaces:  ').replace(' ', ', ')
xl = x.split(', ')
for number in xl:
    if int(number) % 2 == 0:
        print(number, end=', ')
