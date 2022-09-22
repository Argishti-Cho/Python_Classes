'''Albert'''

# rd = str(input('add random digits:  '))

# reverse = rd[:: -1]

# print(reverse)

# number = int(input('input 4 digits:  '))
# print(number % 10), (number // 10 % 10), (number // 100 % 10), (number // 1000 % 10)
# print(number // 10 % 10) 
# print(number // 100 % 10) 
# print(number // 1000 % 10) 

# n = int(input('input:  '))
# print(f'{n % 10}')

# text = 'hello python team'
# print(text[])
# res = 'hello'
# print(res.index('o'))
# text = 'hello |python| team'
# text = text.replace('|', '.', 1)
# text = text.replace('|', ',', 1)

# print(text.index(','))
# print(text[12::-1])

text = 'hello |python| team'
x1 = text.index('|')
text = text.replace('|', '.', 1)
x2 = text.index('|')
print(text[x2 - 1:x1:-1])