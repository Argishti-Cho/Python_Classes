# P = presure in pascals
# V = volume in litters 
# n = is the amount of substance in moles
# R = 8.314*(j / (m/k))
# T = temperature in degrees Kelvin.
import math as m
# P * V = n*R*T
P = float(input('enter presure in pascals:  '))
V = float(input('enter volume in litters:  '))
# T = float(input('enter temreture in Kelvins:  '))
T = float(input('enter temreture in Celsius:  '))
T = T + 273.15
R = 8.314
# tankCapacity = 12
# pressureInTank = 20000000
# roomTemp = 20
n = (P * V) / (R * T)
print(round(n, 3))