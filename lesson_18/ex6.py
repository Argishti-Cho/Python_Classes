#  the shitie shit can't resolve the shit

mydict = {
    'Dave': [4, 5.5, 1.5, 3],
    'Andrey': [3, 4, 8, 10],
    'Abbey': [6, 2, 9, 1.5],
    'Danna': [10, 1, 1, 8],
    'Mark': [10, 10, 9, 8],
    'Ruby': [2, 2, 1, 3],
    'Benedict': [1, 6, 4, 3],
    'Argi': [10, 10, 9.5, 10],
    'Methew': [8, 7, 9, 10],
    'Galagher': [5, 7, 8, 6],
}
the_dict = {}
for i, j in mydict.items():
    the_dict[i] = sum(j) / float(len(j))
for i in mydict.keys():
    if i == 'Argi':
        print(f'{i} is: {the_dict[i]}')


