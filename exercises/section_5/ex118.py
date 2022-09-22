import re
x = input('Enter your sentece:  ').lower()
x = re.sub(r'[^\w\s]','', x)
xl = x.split(' ')
for each in xl:
    if each[0] == each[::-1]:
        continue

    print('asd')
