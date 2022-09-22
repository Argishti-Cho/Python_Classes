import re

p = input('Enter any word:  ').replace(' ', '')
p = re.sub(r'[^\w\s]', '', p)
p = p.lower()
if p == p[::-1]:
    print('Open')
else:
    print('Trash')