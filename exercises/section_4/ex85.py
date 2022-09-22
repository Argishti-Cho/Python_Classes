import math

def hypotenuse(a, b):
    c = math.sqrt((a**2) + (b**2))
    return c

def main():
    x = float(input('Enter a:  '))
    y = float(input('Enter b:  '))
    result = hypotenuse(x, y)
    print(f'The hypotenuse of right triangle is {result} ')

if __name__ == "__main__":
    print(main())