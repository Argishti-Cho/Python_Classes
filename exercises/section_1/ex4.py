# Hint: There are 43,560 square feet in an acre.

lenght = float(input('add lenght in ft:  '))
width = float(input('add width in ft:  '))
area_in_ft = lenght * width
acres = 43560
area = area_in_ft / acres

print(area, 'acres')