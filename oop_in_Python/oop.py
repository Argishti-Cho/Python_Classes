# class Car:

#     x = 45

# print(Car.x)

# class AcMilan:

#     x = 'Ac Milan'

# print(AcMilan.x)

'''------------------------------'''
# class Car:
#     def func(x: int, y: int, z: int) -> int:
#         return x + y + z

# ac = Car
# print(ac.func(7, 8, 9))

# class Car:
#     def __init__(self, x: int, y: int, z: int) -> int:
#         self.x = x
#         self.y = y
#         self.z = z

#     def test(self):
#         return self.x + self.y + self.z

# object_ = Car(7, 7, 7)
# print(object_.test())

# class calculator:

#     def __init__(self, number1: int or float, number2: int or float) -> None:
#         self.number1 = number1
#         self.number2 = number2

#     def gumarum(self):
#         return self.number1 + self.number2

# class Soda:
#     def __init__(self, just_soda: str):
#         self.just_soda = just_soda

#     def show_my_drinks(self) -> int:
#         x = int(input("Enter your choice 1 - just Soda or 2 - Soda with Lemon:  "))
#         if x == 1:
#             return self.just_soda
#         elif x == 2:
#             return f"Just Soda"

# aC = Soda
# # x = 'Soda with with Lemon'
# print(aC.show_my_drinks('Soda with Lemon'))

# class Soda:

#     def __init__(self, addition: str = None):
#         self.addition = addition

#     def show_my_drinks(self) -> int:

# aC = Soda
# x = 'Soda with with Lemon'
# print(aC.show_my_drinks(x))

# class TriangleChecker:

#     def __init__(self, x:float, y:float, z:float):
#         self.x = x
#         self.y = y
#         self.z = z

#     def is_triangle(self):
#         # juraqanchyur 2 koghmi gumar 3rd koghmic petqa mets lini
#         if self.x + self.y > self.z and self.x > 0 and self.y > 0 and self.z > 0:
#             return f"The triange is built !!!"
#         elif self.x.isalpha():
#             return f' the entered value is alpha'
#         else:
#             return f'Entered number are negative or is not digits eithet we won\'t be able to make a triangle'

# aC = TriangleChecker(5, 6, 8)
# print(aC.is_triangle())

'''4'''

# class Nikola:

#     def __init__(self, name: str = 'Nikola'):
#         self.name = name

#     def changeName(self) -> str:
        
#         x = input('Enter Your name:  ')
#         y = int(input('Enter Your age:  '))
#         if x == 'Nikola':
#             return self.name
#         else:
#             return f'your name is not {x} but {self.name} !!!'

# aC = Nikola()
# print(aC.changeName())

'''5'''

# class Anna:

#     def __init__(self, w1:str = input('Enter first word:  '), w2:str=input('Enter second word:  ')) -> None:
#         self.w1 = w1
#         self.w2 = w2

#     def ord_(self):

#         w1ord = 0
#         w2ord = 0

#         for i in self.w1:
#             w1ord += ord(i)
#         for j in self.w2:
#             w2ord += ord(j)

#         if w1ord > w2ord:
#             return f'{self.w1} is greater than {self.w2} acording to ASCII table'
#         elif w2ord > w1ord: 
#             return f'{self.w2} is greater than {self.w1} acording to ASCII table'
#         else:
#             return f'They are equal'
        
#     def RealString(self):

#         if len(self.w1) > len(self.w2):
#             return f'{self.w1} is grater than {self.w2} according to their actual lenght'

#         elif len(self.w1) < len(self.w2):
#             return f'{self.w2} is greater than {self.w1} according to their actual lenght'

#         else:
#             return f'They are equal'


# aC = Anna()
# print(aC.ord_())
# print(aC.RealString())

'''-------------'''
# class Myclass:

#     __x = 5

# print(Myclass.__x)

#  class - i mej __ (2 gtsiky) incapsualcnume is _ (mek gtsiky) deincapsulacnum e

'''---------------'''



