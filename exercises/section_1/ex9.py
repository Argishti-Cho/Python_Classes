from operator import indexOf


account = int(input('add your balance:  '))
interest = (account * 4) / 100
f_y = account + interest
s_y = account + (interest * 2)
t_y = account + (interest * 3)
print(f'first year: {f_y}\nsecond year: {s_y}\nthird year: {t_y}')