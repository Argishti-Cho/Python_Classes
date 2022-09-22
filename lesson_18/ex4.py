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

rate_dict = {}
for i, j in mydict.items():
    rate_dict[i] = sum(j) / float(len(j))
# print(rate_dict)

for k in rate_dict:
    if rate_dict[k] >= 5:
        print(f'{k} has 5 or grater rate with avarage of {rate_dict[k]} points')