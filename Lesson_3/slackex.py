'''Erik's 2nd exercise'''
# ինչպես գրել որևե բառ input -ից հետո
# 1st car's speed input
# 2nd car's speed is input
# the distance between them input


car1 = int(input('input 1st car speed:  '))
car2 = int(input('input 2nd car speed:  '))
distance = int(input('distance between them:  '))
# time = 60 #minutes 
# speed = (distance / time)
speed = car1 - car2
time = distance / speed
# distance = speed * time
# d1_2 = distance
# result = ((d1_2)+distance)

print(time, 'hour')