# n = int(input('enten n:  '))

# for i in n:
#     if 

# def findStep(n):
#     if ( n == 0 ):
#         return 1
#     elif (n < 0):
#         return 0
 
#     else:
#         return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)
 
 
# # Driver code
# n = 5
# print(findStep(n))

n, n1, n2 = int(input('enter:  '))

for i in range(1, n):
    n1, n2 = n2, n1 + n2
print(n1 + n2)