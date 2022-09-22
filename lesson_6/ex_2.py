fruits = input('enter fuits: ')
a = 'bananas'
b = 'oranges'
c = 'apples'

if fruits == a and b and c:
    print('there is 3 of them')  
elif fruits == a and b:
    print('there are 2 of thems')
elif fruits == a and c:
    print('there are 2 of thems')
elif fruits == a:
    print('1 of')
elif fruits == b:
    print('1 of')
elif fruits == c:
    print(' 1 of')
elif fruits == '':
    print('not supported ')
else:
    print('non of them')