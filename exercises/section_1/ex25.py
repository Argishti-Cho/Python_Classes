# t_sec = int(input('add seconds:  '))

# days = t_sec / 60 / 60 / 24
# t_sec -= days * 60 * 60 * 24

# hours = t_sec / 60 /60
# t_sec -= hours * 60 * 60

# minutes = t_sec / 60
# t_sec -= minutes * 60

# seconds = t_sec

# print(f'{seconds}')  
totalSeconds = int(input("Please enter a number of seconds: "))

days = int(totalSeconds / 60 / 60 / 24)
totalSeconds -= days * 60 * 60 * 24

hours = int(totalSeconds / 60 / 60)
totalSeconds -= hours * 60 * 60

minutes = int(totalSeconds / 60)
totalSeconds -= minutes * 60

seconds = totalSeconds

# print("In the form D:H:M:S : {}:{}:{}:{}".format(days, hours, minutes, seconds))
print(f'In the form D:H:M:s :{days}:{hours}:{minutes}:{seconds}')
