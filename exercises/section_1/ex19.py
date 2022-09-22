import math
d = float(input('enter the height in  metters:  '))
initial_speed = 0
acceleration = 9.8 
# hitTheGround = (initial_speed ** 2) + 2 * acceleration * d
# hitTheGround = math.sqrt((initial_speed ** 2) + 2 * acceleration * d)
hitTheGround = math.sqrt(2 * acceleration * d) 
print(round(hitTheGround, 2))
# print(initial_speed ** 2)