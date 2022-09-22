dogYears = float(input('enter your dog age:  '))

h_years = 10.5
a_h_years = 4

if dogYears <= 2 and dogYears > 0:
    print(f'your dog is equivalent to {h_years * dogYears} human years')
elif dogYears >= 2:
    print(f'your dog is equivalent to {((dogYears - 2) * a_h_years) + (2 * h_years)} human years')
elif (dogYears < 0):
    print(f'the {dogYears} is negative, please enter positive number')
elif dogYears == 0:
    print(f'you entered 0')
else:
    print('error')
