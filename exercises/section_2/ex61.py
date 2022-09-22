from multiprocessing.sharedctypes import Value
import random

value = random.randint(0, 37)
# value = 00

print(f'the number is: {value}')
if value == 37:
    print('pay is 00')
elif value == 0:
    print(f'pay is {value}')
if value % 2 == 1 and value >= 1 and value <= 9 or\
     value % 2 == 0 and value >= 12 and value <= 18 or\
     value % 2 == 1 and value >= 19 and value <= 27 or\
     value % 2 == 0 and value >= 30 and value <= 36:
     print('red pay')
elif value == 0 or value == 37:
    pass
else:
    print('black')
if value >= 1 and value % 2 == 0 and value <= 36:
    print('even')
elif value == 0 or value == 37:
    pass
else:
    print('odd')
if value >= 1 and value <= 18:
    print(f'the wining number is: 1 - 18')
elif value >= 19 and value <= 36:
    print(f'the wining number is: 19 - 36')
 

