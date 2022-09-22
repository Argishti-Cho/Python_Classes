mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}

print({i:mydict[i] for i in sorted(mydict, key=mydict.get)[3:]})

# s = sorted(mydict, key=mydict.get, reverse=True)[:3]
# j = mydict.values()
# for i in j:
#     if s == j[i]:
#         print(s, j)

# print(j)


# s = sorted(mydict, key=mydict.get, reverse=True)[:3]
