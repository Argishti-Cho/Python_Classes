import numpy as np 

participants = ['Dan', 'Diana', 'Argi', 'Tom', 'Abbey',]
to_pickup = np.array([participants.index(name) for name in participants])
pickedup = np.array([])
results = ''

# np.random.seed(3960)
r = np.random.choice(to_pickup)
print(f"picked-up first:  {participants[r]} \n")
to_pickup = np.delete(to_pickup, np.where(to_pickup == r))
pickedup = np.append(pickedup, r)

for person in to_pickup:
    r = np.random.choice(to_pickup)
    pickedup = np.append(pickedup, r)
    to_pickup = np.delete(to_pickup, np.where(to_pickup == r))    
    results += participants[int(pickedup.item(-2))] + ' offers to ' + participants[r] + '\n'

results += 'And ' + participants[int(pickedup.item(-1))] + ' offers to ' + participants[int(pickedup.item(0))] + '\n'
print(results)

# import random

# participants = ['Dan', 'David', 'Ben', 'Abbey', 'Argi']
# pickedup = []
# users = []
# new_list = []

# while len(participants) > 0:
#     x = random.choice(participants)
#     pickedup.append(x)  
#     participants.remove(x)

# for item in range(0, len(pickedup) - 1):
#     users.append(f"{pickedup[item]} --- {pickedup[item+1]}")
# users.append(f"{pickedup[-1]} --- {pickedup[0]}")

# while len(users) > 0:
#     y = random.choice(users)
#     new_list.append(y)
#     users.remove(y)

# for each in new_list:
#     print(each)
