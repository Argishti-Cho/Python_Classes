import random

user = int(input('enter number (0-5):  '))
pc = random.randit(0, 5)
user_points = 0
pc_points = 0
if user == pc:
    user_points += 1
    print(f'')
    