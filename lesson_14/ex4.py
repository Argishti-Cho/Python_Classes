from operator import truediv


fruits = ['banana', 'apple', 'orange', 'grape', 'grasshophers']
numbers = [2, 85, 78, 'apple', 'snoopdog']
# for each in fruits:
#     if each == numbers[0] or each == numbers[1] or each == numbers[2] or each == numbers[3]:
#         print('True')
#     else:
#         print('hay')
# print(list(set(fruits).intersection(numbers)))
# print(fruits[0: -1] == numbers[0: -1])

for i in fruits:
    if i in numbers:
        print(list(''.join(i)))
        print(list(i))