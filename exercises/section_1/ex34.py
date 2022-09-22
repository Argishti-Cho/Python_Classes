# (deposit * 4 / 100)

o_l_q = int(input('add number of loaves in off:  '))
n_l_q = int(input('number of todays loaves:  '))
loaves = 3.49
old_loaves = loaves - (3.49 * 60) /100
o_l_q_t = (old_loaves * o_l_q)
n_l_q_t = (n_l_q * loaves)

print(f'''discounted loaves {round(o_l_q_t, 2)} \ntoday's loaves {n_l_q_t}''')