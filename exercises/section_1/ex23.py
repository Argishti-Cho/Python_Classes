import math as m
s = int(input('lenght:  '))
n = int(input('number of sides: '))
print(f'regular polygon area is : {round((n * (s ** 2)) / (4 * m.tan(m.pi/n)), 3)}')