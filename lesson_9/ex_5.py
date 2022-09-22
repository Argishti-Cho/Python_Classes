import random
you = int(input('enter your followers: '))
pc = random.randint(1, 5000)
if you >= pc + pc*20/100:
    print('you are a blogger ')
else:
    print('pc is blogger')
