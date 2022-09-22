# x = 0
# for i in str(x):
#     if x % 12 == 0 and x % 15 == 0:
#         print(x)
#     else:
#         print('eror')

a = int(input('num1:  '))
b = int(input(' num2:  '))
for i in range(max(a, b), a * b + 1, max(a, b)):
    if i % min(a, b) == 0:
        print(i)
        break