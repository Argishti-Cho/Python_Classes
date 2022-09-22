import timeit 

n = int(input('Enter any psoitive number,  0 for exit:  '))

while n != 1:
    if n % 2 == 0:
        n = n//2
        print(n)
    else:
        n = n * 3 + 1
        print(n)
    # if n >= 0:
    #     break
print(n)
print(timeit.timeit())