def multiply(mylist):
    summ = 1
    for i in mylist:
        summ *= i
    return summ
print(multiply([4, 5, 6]))