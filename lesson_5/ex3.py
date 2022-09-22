import calendar
y = int(input('Enter your birth year:  '))
m = int(input('Enter your month:  '))
d = int(input('Enter your day:  '))
print(calendar.month(y, m, d))