import math as m

s1 = float(input('side1 :  '))
s2 = float(input('side2 :  '))
s3 = float(input('side3 :  '))

s = (s1 + s2 + s3)/2
area = m.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print(round(area, 3))