mydict = {
    'Dave': [4, 5.5, 1.5, 3],
    'Andrey': [3, 4, 8, 10],
    'Abbey': [6, 2, 9, 1.5],
    'Danna': [10, 1, 1, 8],
    'Mark': [10, 10, 9, 8],
    'Ruby': [10, 10, 10, 10],
    'Benedict': [1, 6, 4, 3],
    'Argi': [2, 2, 1, 1],
    'Methew': [8, 7, 9, 10],
    'Galagher': [5, 7, 8, 6],
}

avdict = {}
for i, j in mydict.items():
    avdict[i] = sum(j) / float(len(j))
# print(avdict)

for i in avdict:
    # print(i)
    if avdict[i] >= 5:
        print(f'{i} is a Good Student with an average of {avdict[i]} points')
    else:
        print(f'{i} is a Bad Student with an average of {avdict[i]} points')

