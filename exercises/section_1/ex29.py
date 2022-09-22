# T = air temreture in degree celsius 
# V = wind speed in kilometers per hour 

T = float(input('enter air temreture in celsius:  '))
V = float(input('enter wind speed in Kph:  '))

# T <= 10
# V >= 4.8

WCI = 13.12 + (0.6215 * T) - (11.37 * V ** 0.16) + (0.3965 * T * V ** 0.16)

print(WCI)

# airTemp = float(input("Please enter an air temperature: "))
# windSpeed = float(input("Please enter the corresponding wind speed: "))

# WCI = 13.12 + (0.6215*airTemp) - (11.37*(windSpeed**0.16)) + (0.3965*airTemp*(windSpeed**0.16))

# print("The WCI (Wind Chill Index) is {}.".format(WCI))