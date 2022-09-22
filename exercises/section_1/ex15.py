d = float(input('add ft:  '))

# 1 ft = 12 inches. 1 inch = 2.54 cm.
inch = d * 12
yard = inch * 0.0277778
mile = yard * 0.000568182
input(f'inches: {inch}\nyards: {yard}\nmile: {mile}')