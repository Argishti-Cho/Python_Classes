# def drawBox(width, height, outline, fill):
#     if width < 2 and height < 2:
#         print('Too small try again!!! ')
#         quit()
   
#     print(outline * width)

#     for i in range(height - 2):
#         print(outline + (fill * (width-2)) + outline)

#     print(outline * width)

# drawBox(30, 5, '@', '.')

# --------------------------------------------------------------------

def sumGeometric(a, r, n):
    if r == 1:
        return a * n
    s = a * (1 - r**n) / (1-r)
    return s

def main():
    init = float(input('Enter the value a(0 to quit):  '))

    while init != 0:
        ratio = int(input("Enter the ratio, r:  "))
        num = float(input('Enter the number of items, n:  '))
        total = sumGeometric(init, ratio, num)
        print(f'The sum of the first item {num} terms is {total}')

        init = float(input('Enter the value (0 to quit):  '))

main()
