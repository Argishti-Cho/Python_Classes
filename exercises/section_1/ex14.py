height = float(input('add your height in ft:  '))

# 1 ft = 12 inches. 1 inch = 2.54 cm.
ft = height * 12
cm = ft * 2.54
input(f'your height is=> {round(cm, 2)} cm\nand {round(ft, 2)} ft')