import math as m
# a = float(input('enter number a: '))
# b = float(input('enter number b: '))
# r = m.sqrt((b**2)-4*a*b)
# a = float(input('enter number a: '))

# print(round(m.sqrt(a), 4))
a = 6
b = 10 
c = -1
x1 = (-b - m.sqrt((b**2 - (4*a*c)))) / (2*a)
x2 = (-b + m.sqrt((b**2 - (4*a*c)))) / (2*a)
print(round(x1, 3), round(x2, 3))