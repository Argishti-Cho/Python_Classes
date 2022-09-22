# calculator

def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def divide(x, y):
    return x/y
def multiply(x, y):
    return x*y
# x = % / 100 * n
def percent(x, y):
    return y/100*x

num1 = float(input('enter first number:  '))
operator_ = (input('enter operator:  '))
num2 = float(input('enter second number:  '))

if operator_ == '+':
    print(f'= {add(num1, num2)}')
elif operator_ == '-':
    print(f'= {subtract(num1, num2)}')
elif operator_ == '*':
    print(f'= {multiply(num1, num2)}')
elif operator_ == '/':
    print(f'= {divide(num1, num2)}')
elif operator_ == '%':
    print(f'the {num2}% of {num1} = {percent(num1, num2)}')

else:
    print('invalid input')