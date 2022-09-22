n = int(input('Enter the number:  '))
factor = 2 
while factor <= n:
    if n % factor == 0:
        # print(f'{factor}')
        n = n // factor
        print(f'{factor}')
        break
    else:
        factor += 1


