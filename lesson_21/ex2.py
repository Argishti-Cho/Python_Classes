def max_(x,y):
    if x > y:
        return f'the max nim is {x}'
    elif y > x:
        return f'the max nim is {y}'
    else:
        return 'equal'
num1 = float(input('Enter first num:  '))
num2 = float(input('Enter second num:  '))
print(f'{max_(num1, num2)}')