import json

'''exersice 1'''

# first = ['Ani', 'Jessy ', 'Ben']  
# second = [1,2,3]

# res = {second[i]: first[i] for i in range(len(second))}
# # print(res)
# with open('res.txt', 'w') as file:
#     json.dump(res, file)

'''exersice 2'''

# with open('lyrics.json', 'w') as file:
#     res = json.load(file)

# for data in res:
#     print(data)


'''3'''

# def sum_(n):
#     res = 0
#     for i in range(0, n):
#         if i % 3 == 0 or i % 5 == 0:
#             res += i
#     return res
# print(sum_(20))

'''4'''

# def vowels(word: str) -> str:
#     count = 0
#     for i in word:
#         if i in 'aoeuiAOEUI' and word[0] == 'y' or i in 'aoeuiAOEUI':
#             count += 1
#     count = str(count)
#     return {'Count of vowels': count}

# with open('vowels.json', 'w') as file:
#     json.dump(vowels(input('Enter a word:  ')), file)


'''5'''

# def count_the_words(n: str) -> dict:
#     count1 = 0
#     count2 = 0
#     # another = 'another'
#     and_ = 'and'
#     x = n.split()
#     for words in x:
#         if words.lower() == 'another':
#             count1 += 1
#         if words.lower() == and_:
#             count2 += 1
#     return {'another': count1, and_: count2}

# with open('text2.txt') as acMilan:
#     word = acMilan.read()

# print(word)
# print(count_the_words(word))

'''6'''

# def getNewList(n: list) -> list:
#     output = []
#     # new_string = ''
#     [output.append(i) for i in n if i not in output]
#     # for x in output:
#     #     new_string += x
#     # return new_string
#     return output

# my_list = ['a', 'b', 'a', 'c', 'b']
# print(getNewList(my_list))

'''7'''

# def calculateTheNumber(n: str) -> dict:
#     uppercase = 0
#     lowercase = 0
#     for letter in n:
#         if letter.isupper():
#             uppercase += 1
#         if letter.islower():
#             lowercase += 1
#     return {
#         'uppercase letters': uppercase,
#         'lowercase letters': lowercase
#     }

# with open('text3.txt') as acMilan:
#     miLan = acMilan.read()

# print(calculateTheNumber(miLan))




