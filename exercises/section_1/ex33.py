a = int(input('enter n1:  '))
b = int(input('enter n2:  '))
c = int(input('enter n3:  '))
print(f'''{min(a, b, c)}, {(a+b+c) - (min(a, b, c) + max(a, b, c))}, {max(a, b, c)}''')