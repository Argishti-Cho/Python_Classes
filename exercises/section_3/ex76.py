import re, timeit

x = input('enter you sentence here:  ').replace(' ', '')
x = re.sub(r'[^\w\s]','', x)
x = x.lower()
# print(x)
while x == x[::-1]:
    print(f'{x} is a palidrome')
    break
else:
    print(f'{x} is not a palindrome')
print(round(timeit.timeit(), 4))