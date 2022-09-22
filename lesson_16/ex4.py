# def merge(dict1, dict2):
#     return(dict2.update(dict1))

# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}

# print(dict2)

def merge(dict1, dict2):
    merged = {**dict1, **dict2}
    return merged

dict1 = {'a': 50, 'b': 700}
dict2 = {'c': 400, 'd': 600}
dict3 = merge(dict1, dict2)
print(dict3)

