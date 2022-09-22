import random
my = float(input('enter you digit:  '))
ra  = random.randint(10, 100)
if my >= ra:
    result = 'TRUE'
else: 
    result = 'FALSE'

print(result)