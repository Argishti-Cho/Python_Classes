x = int(input('enter num:  '))

for number in range(2, x+1):
        for i in range(2, number):
            if number % i == 0:
                break
            else:
                print(number)
                break
# print(number)