summ = 0

while True:
    age = input('age:  ')
    if age == '':
        print(summ)
        break
    else:
        if 3 <= int(age) <= 12:
            summ += 14
        elif int(age) >= 65:
            summ += 18
        else:
            summ += 23