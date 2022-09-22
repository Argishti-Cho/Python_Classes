# how to check if there is a 2 big items
fruits = ['banana', 'apple', 'orange', 'grape', 'grasshophers']
# for each in fruits:
#     x = max(fruits, key=len)
# print(x)
count = 0
for each in fruits:
    if len(each) > count:
        count = len(each)
        word = each
print(word)