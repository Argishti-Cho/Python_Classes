# listA = [1, 2, 3]
# listA = list(input())

# while 6 not in listA:
#    listA.append(len(listA) + 1)

# print(listA)
# ----------------------------------------------
# count= 3


# while not (count== 6) :

#    print(count)

#    count= count+ 1
# ----------------------------------------------
# text = 'geeks5 for geeks asdk kks55'
  
# # Splits at space
# print(text.split())

# word = 'geeks, for, geeks'
  
# # Splits at ','
# print(word.split(','))
# -----------------------------------------------
# # contains indices (0, 1, 2)
# result1 = slice(3)
# print(result1)

# # contains indices (1, 3)
# result2 = slice(1, 5, 2)
# print(slice(1, 5, 2))

# def sayHello():
#     print('motafata')

# sayHello()

# def get_first(data):
#     return data[0]
    
# if __name__ == '__main__':
#     data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
#     print(get_first(data))

# def binary_search(data, value):
#     n = len(data)
#     left = 0
#     right = n - 1
#     while left <= right:
#         middle = (left + right) // 2
#         if value < data[middle]:
#             right = middle - 1
#         elif value > data[middle]:
#             left = middle + 1
#         else:
#             return middle
#     raise ValueError('Value is not in the list')
    
# if __name__ == '__main__':
#     data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(binary_search(data, 1))

# def drawBox():
#     print("**********")
#     print("*        *")
#     print("*        *")
#     print("**********")

# drawBox()