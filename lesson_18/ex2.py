mydict = {
    'student1': [4, 5.5, 10, 9],
    'student2': [3, 4, 8, 10],
    'student3': [6, 10, 9, 9],
    'student4': [10, 1, 1, 8],
    'student5': [10, 10, 9, 8],
    'student6': [10, 10, 10, 10],
    'student7': [1, 6, 4, 3],
    'student8': [2, 2, 1, 1],
    'student9': [8, 7, 9, 10],
    'student10': [5, 7, 8, 6],
}

avdict = {}

for i, j in mydict.items():
    avdict[i] = sum(j)/float(len(j))
print(avdict)
    

# x = mydict.values()
# y = len(mydict)
# print(y)
# print(x)
# print(sum(x)/y)