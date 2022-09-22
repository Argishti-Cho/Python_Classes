# Two Dice Simulation
# each 36th dice could be the same pair => 3.6% of 1000 drop dices ex 1:1 => sum 2 in 1000
# drop due to prabability theory will accuar 2.77% times it means 27 times 
# formula is 1000/36 = 27.77 => 2.77% of 1,000  

import random

pairs = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

for i in range(0, 1000):
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    summ = d1 + d2
    # print(summ)
    for k, v in pairs.items():
        if summ == k:
            pairs[k] += 1
# print(pairs)

for j, l in pairs.items():
    simulated = l*100/1000
    expected = (100-simulated)*100/1000
    print(f'the pair of {j} appeared {l} times, simulated % is {simulated}%, expected % is {expected}')


