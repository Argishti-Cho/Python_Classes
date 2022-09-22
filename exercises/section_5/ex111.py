
numbers = []
while True:
    x = int(input(' Enter number:  '))
    if x != 0:
        numbers.append(x)
    else:
        break        
numbers.reverse()
for i in numbers:
    print(i, end=', ')