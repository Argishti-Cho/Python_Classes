import math as m
days = int(input('enter days:  '))
hours = int(input('enter hours:  '))
minutes = int(input('enter minutes:  '))
seconds = int(input('enter seconds:  '))

ts = seconds
ts += minutes * 60
ts += hours * 60 * 60
ts += days * 60 * 60 *24
print(ts)
