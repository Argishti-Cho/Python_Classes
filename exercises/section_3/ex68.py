# A = 4.0
# A_MINUS = 3.7
# B_PLUS = 3.3
# B = 3.0
# B_MINUS = 2.7
# C_PLUS = 2.3
# C = 2.0
# C_MINUS = 1.7
# D_PLUS = 1.3
# D = 1.0
# F = 0
# INVALID = -1
grades = []

#.upper()
while True:
    letter = input('enter a Letter grade separated by spaces: ').upper()
    gp = 0

    if letter == '':
        break
    elif letter == "A+" or letter == "A":
        gp = 4.0
    elif letter == "A-":
        gp = 3.7
    elif letter == "B+":
        gp = 3.3
    elif letter == "B":
        gp = 3
    elif letter == "B-":
        gp = 2.7
    elif letter == "C+":
        gp = 2.3
    elif letter == "C":
        gp = 2
    elif letter == "C-":
        gp = 1.7
    elif letter == "D+":
        gp = 1.3
    elif letter == "D":
        gp = 1.0
    elif letter == "F":
        gp = 0
    else:
        print("That wasn\'t a valid letter grade.")
    grades.append(gp)
print(grades)
print(round(sum(grades)/len(grades), 3))

        # print(f'average is: {sum(gp)/len(gp)}')

# numbers = [float(num) for num in numbers_str.split()]
# print("Average of ", numbers, " is ", round(sum(numbers) / len(numbers), 3))