sound = float(input('Enter sound level in decibels: '))

# jackhammer = 130 
# gas_Lawnmower = 106 
# alarm_Clock = 70 
# quiet_Room = 40 

if sound == 130:
    print('Jackhammer')
elif sound == 106:
    print('Gas Lawnmower')
elif sound == 70:
    print('Alarm Clock')
elif sound == 40:
    print('Quiet Room')
elif sound > 40 and sound < 70:
    print('between alarm and room')
elif sound > 70 and sound < 106:
    print('sound between alarm and gas lawnmover')
elif sound > 106 and sound < 130:
    print('sound is between Gas Lawnmover and Jackhammer')
elif sound > 40 or sound > 130:
    print('out of range')
else:
    print('Error')
