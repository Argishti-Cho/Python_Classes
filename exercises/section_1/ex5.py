# a bottle <= 1 litter = 0.10, a bottle >= 1 litter = 0.25 
# input each bottle, then colculate all

b_1 = float(input('bottles holding a litter or less:  '))
b_2 = float(input('bottles more then 1 litters:  '))

r_1 = b_1 * 0.10
r_2 = b_2 * 0.25
tr = r_1 + r_2

print('refund $', tr)