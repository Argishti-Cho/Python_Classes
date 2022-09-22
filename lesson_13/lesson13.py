# tup1 = ('physics', 'chemistry', 1997, 2000)
# print(tup1.__sizeof__())
# output 56
thistuple = ("apple", 'banana', "cherry", 'kiwi', 'melon', 'mango')
# print(len(thistuple)) 
# print(thistuple.count('banana')) # qani hat nshvats baric ka 
# if 'banana' in thistuple:
#     print('yes')
# else:
#     print('no')
# for x in thistuple:
#     print(x, end=' ')
# print(thistuple[1:3])
x = (5, 65, 78, 45, 2)
# y = reversed(thistuple)
# y = tuple(y)
# print(tuple(y))
# print(thistuple[-4:-1]) # verjin indexic 4 index het e gnum 
# # tuple -nery miacvum en + operatorov
# y = thistuple + x
# print(y)
num = [10, 20, 30, (10, 20), 40]
c = 0
for n in num:
    if isinstance(n, int):
        break
c += 1
print(c)