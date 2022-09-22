# totally copied from the net, could do by myself(())
import math as m

mass = float(input('enter the mass of the water:  '))
tempChange = float(input("Enter the temperature change in degrees Celsius: "))
# the amount of energy = q
# celsius = 4.186
q = mass * 4.186 * tempChange
print(q)
costPerKiloWattHour = 8.9 # Taken from the question
kiloWattHours = q * 2.7778e-7 # Converts from Joules to kilowatt-hours

cost = kiloWattHours * costPerKiloWattHour

print(f'The total cost of this is ${cost}.')