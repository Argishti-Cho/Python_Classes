sides = int(input('enter side''s number: '))
if sides == 3:
    print('triangle')
elif sides == 4:
    print('squares')
elif sides == 5:
    print('5')
elif sides == 6:
    print('6')
elif sides == 7:
    print('7')
elif sides == 8:
    print('8')
elif sides == 9:
    print('9')
elif sides == 10:
    print('10')
elif sides < 3 or sides > 10:
    print('entered range should be 3-10')
else:
    print('error')