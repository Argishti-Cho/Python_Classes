# myDict = {
#     'name': 'Dave',
#     'year': 1989,
#     'email': 'dave89@gmail.com'
# }

# otherDict = dict(brand='Ford', model='Mustang', year=1964)

# print(myDict,'\n', otherDict)

mydict = {
    'D': 56,
    'E': 12,
    'F': 69,
    'C': 45,
    'B': 23,
    'A': 67
}

print({i:mydict[i] for i in sorted(mydict, key=mydict.get)})

newmydict = {}
x = sorted(mydict, key=mydict.get)
y = sorted(mydict.values())
for i, j in zip(x, y):
    newmydict[i] = j
print(newmydict)

