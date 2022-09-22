import random
import time


user = input('enter your bid /note. your choice should be only rock, papper or scissors:  ')
x = 'rock', 'papper', 'scissors'
pc = random.choice(x)
user_choices_1 = 'rock'
user_choices_2 = 'papper'
user_choices_3 = 'scissors'
if user == user_choices_1 and pc != user_choices_1 and pc != user_choices_2 and pc == user_choices_3:
    print(' ---- User Won ----')
