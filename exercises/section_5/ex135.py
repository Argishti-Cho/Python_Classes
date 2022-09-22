import time

n = int(input("Enter number:  "))
st = time.time()
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
et = time.time()
print(et -st)

# print(timeit.timeit())