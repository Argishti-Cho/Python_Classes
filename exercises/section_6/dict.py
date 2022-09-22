# mydict = {
#     'login': 'user',
#     'password': 'python',
#     'phone': 935546464
# }

# for i in mydict:
#     print(mydict.get(1))

# for i in mydict.items():
#     print(i)

# mydict['login'] = 'admin'
# mydict['email'] = 'abc@gmail.com'

# mydict.popitem()jnjum e verjin item-y
# print(mydict)

# mydict.pop('phone') jnjum e miayn phone number-y 
# print(mydict)

# del mydict['phone'] jnjum e amboghj phone toghy
# print(mydict)


# mydict = {
#     'D': 56,
#     'E': 12,
#     'F': 69,
#     'C': 45,
#     'B': 23,
#     'A': 67
# }

# print({i:mydict[i] for i in sorted(mydict, key=mydict.get, reverse=True)[:3]})

# s = sorted(mydict, key=mydict.get)
# print(s[-3:])


# constants = {"pi": 3.14, "e": 2.71, "root 2": 1.41}
# # for k in constants:
# #     print(f'the value associated with {k} is, {constants[k]}')
# total = 0
# for v in constants.values():
#     total += v
# print(total)

# counts = {}
# while len(counts) < 5:
#     s = input()
#     if s in counts:
#         counts[s] += 1
#     else:
#         counts[s] = 1
# for k in counts:
#     print(f'{k} occured {counts[k]} times')

# import random

# pairs = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

# for i in range(0, 1001):

#     d1 = random.randint(1, 6)
#     d2 = random.randint(1, 6)
#     summ = d1 + d2
#     pairs[summ] += 1

# print(pairs)
