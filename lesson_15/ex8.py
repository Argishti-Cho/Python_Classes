x = input('Enter number separated with space:  ')
xl = x.split(' ')
for i in xl[::]:
    if int(i) % 2 == 0:
        xl.remove(i)
print(xl)
