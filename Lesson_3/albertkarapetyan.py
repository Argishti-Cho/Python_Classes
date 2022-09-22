'''1'''
# couldn't round at all
# seconds = int(input('add seconds:  '))
# minutes = seconds / 60
# hour = minutes / 60
# day = hour / 24
# print(day, 'days', hour, 'hours', minutes, 'minutes')

second = int(input('Enter:  '))
day = second // 86400
time = second % 86400 // 3600
minutes = (second - (day * 86400) + (time * 3600)) // 60
print(f'{second}(second) = {day}(day) and {time}(hours) and {minutes}(minutes)')
# print(86400 + 21600 + 1980 + 20)

