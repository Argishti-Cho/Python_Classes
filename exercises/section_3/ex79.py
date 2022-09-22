n = int(input('Enter 1st positive number:  '))
m = int(input('Enter 2nd positive number:  '))
print(n%m)
d = min(n, m)
while d > 0:
    if n % d == 0 and m % d == 0:
        print(f'{d} is Greatest Common Divisor!')
        break
    else:
        d -= 1
