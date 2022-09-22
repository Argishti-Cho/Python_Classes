myList = ['apple', ' banana', 'orange', 'apple', 'kiwi']
for item in myList:
    if myList.count(item) > 1:
            myList.remove(item)
print(myList)