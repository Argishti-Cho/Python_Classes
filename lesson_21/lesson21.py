# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# def converter(a):
#     cnv_dct = {a[i]: a[i+1] for i in range(0, len(a), 2)}
#     return cnv_dct  
    
# fruits = ['apple', 2, 'banana', 5, 'kiwi', 4, 'peach', 1]
# print(converter(fruits))
# import time
#  if statement
# n1 = 0
# n2 = 1
# n = int(input('Enter number:  '))
# st = time.time()
# for i in range(2, n):
#     n1, n2 = n2, n1 + n2
# print(n1+n2)
# et = time.time()
# print(et-st)

# recursion 
# st = time.time()
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(35))
# et = time.time()
# print(et-st)

#  factorial solution
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(150))

# def test_pow(n):
#     def just_decorator(x):
#         def test(mylist):
#             return [x(i[0], i[1]) ** n for i in mylist]
#         return test
#     return just_decorator

# @test_pow(3)
# def func(a, b):
#     return a + b
# print(func([(5, 9), (10, 11), (7, -4), (5, 4)]))