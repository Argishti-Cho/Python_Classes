'''Test 1 (2 points) '''

# import math

# class Corona:

#     def __init__(self, temp:float=float(input('Enter your body tempreture with floating numbers:  '))) -> None:
#         self.temp = temp

#     def coronaCheck(self) -> str:

#         temp_x = round(self.temp * math.pi)
#         # print(f'{temp_x} is your temreture')

#         if 120 <= temp_x <= 128:
#             return f'You have coronavirus'
#         else:
#             return f'Everythong is ok'

# aC = Corona()
# print(aC.coronaCheck())

'''Test 2 (3 points)'''
# import math

# class CorrespondingNumber:

#     def __init__(self, name:str=input('Enter your name:  ').lower()) -> None:
#         self.name = name

#     def checkWidespread(self) -> str:
#         res = 0
#         for letter in self.name:
#             if letter == 'a' or letter == 'j' or letter == 's':
#                 res += 1
#             if letter == 'b' or letter == 'k' or letter == 't':
#                 res += 2
#             if letter == 'c' or letter == 'l' or letter == 'u':
#                 res += 3
#             if letter == 'd' or letter == 'm' or letter == 'v':
#                 res += 4
#             if letter == 'e' or letter == 'n' or letter == 'w':
#                 res += 5
#             if letter == 'f' or letter == 'o' or letter == 'x':
#                 res += 6
#             if letter == 'g' or letter == 'p' or letter == 'y':
#                 res += 7
#             if letter == 'h' or letter == 'q' or letter == 'z':
#                 res += 8
#             if letter == 'i' or letter == 'r':
#                 res += 9

#         if math.sqrt(res) <= 5:
#             return f'{res}, root is {math.sqrt(res)}, Yes'
#         else:
#             return f'{res}, root is {math.sqrt(res)}, No'

# aC = CorrespondingNumber()
# print(aC.checkWidespread())

'''Test 3 (5 points)'''
# import random as r

# class HarryPotter:

#     # def __init__(self, user:str) -> None:
#     #     self.user = user

#     def checkMagicWord(user) -> str:

#         lord = ['Avada Kedavra', 'Crucio', 'Imperio']
#         lordChoice = r.choices(lord, k=3)

#         userChoice = []
#         for i in range(3):
#             user = input('Enter your magic word 3 times Avada Kedavra, Crucio or Imperio: ')
#             print()
#             userChoice.append(user)

#         res = 0
#         resString = ', \n'
#         if userChoice[0] == lordChoice[0]:
#             res += 1
#         if userChoice[0] != lordChoice[0]:
#             res -= 1
#         if userChoice[1] == lordChoice[1]:
#             res += 1
#         if userChoice[1] != lordChoice[1]:
#             res -= 1
#         if userChoice[2] == lordChoice[2]:
#             res += 1
#         if userChoice[2] != lordChoice[2]:
#             res -= 1

#         if res >= 2:
#             return f'{resString.join(lordChoice)} \n\nYou Win !!!'
#         else:
#             return f'{resString.join(lordChoice)} \n\nYou Lose !!!'

# aC = HarryPotter()
# print(aC.checkMagicWord())