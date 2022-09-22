# odd or even
# Read the limit from the user
# limit = int(input("Enter an integer: "))
# # Display the positive multiples of 3 up to the limit
# print("The multiples of 3 up to and including", limit, "are:")
# for i in range(3, limit + 1, 3):
#  print(i)
kent = 0
zuyg = 0
# x = range(1, 100)
for i in range(1, 100):
    if i % 2 == 0:
        zuyg += 1
    else:
        kent += 1
print(f'zuyf: {zuyg}\nkent: {kent}')