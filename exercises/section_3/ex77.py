
print(f"{' ': >3}",end="")
for i in range(1,11):
    print (f"{i: >5}",end="   |")
print("\n", '-'*92)
for i in range(1,11):
    print(f"{i:>2}",end="|")
    for j in range(1,11):
        print(f"{i*j: >5}",end="   |")
    print("\n", '-'*92)