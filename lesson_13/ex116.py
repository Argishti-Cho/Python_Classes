mylist = []
for i in range(1, 10000):
    if i % 2 == 0:
        print(i)
    for j in range(1, i):
        if j % 2 == 0:
            print(j)
            break