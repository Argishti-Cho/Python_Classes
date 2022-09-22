
# x = input()
# a = []
# while x:
#     x != ''
#     y = round(float(x))
#     a.append(y)
#     x = input()
# print(a)
# print(f'sum is: {sum(a)}')

# sum = 0
# roundedSum = 0
# while True:
#     price = input('Enter the price:  ')
#     if price != '':
#         price = float(price)
#     else:
#         break
#     sum += price
#     pennies = price*100
#     reminder = pennies%5
#     if reminder > 2.5:
#         pennies += 5 - reminder
#     else:
#         pennies -= reminder

#     roundedPrice = pennies * 0.01
#     roundedSum += roundedPrice
# print(f'{round(sum, 2)}')
# print(f'{round(roundedSum, 2)}')

import math
sum = 0
while True:
    price = input('Enter the Price:  ')
    if price == '':
        break
    sum += float(price)

x = round(sum)
y = round(sum, 2)
z = math.floor(sum)
rest = y - z
if 0.75 > rest > 0.25:
    y = z + 0.5
elif rest <= 0.25:
    y = z
else:
    y = x
print(y)