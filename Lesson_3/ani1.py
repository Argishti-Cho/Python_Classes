'''Ani 1'''
# Grel cragir vory kunena 3 input ev cuyc kta businessi ekamuty,
#  ekamuti u nerdrman(caxseri) tarberutyuny, ekamti, nerdramn,
#  ev harki tarberutyuny.

a = int(input('the profit:  '))
b = int(input('investment:  '))
c = int(input('taxes:  '))

pi = a - b
t = b - c
t2 = a - c

print('եկամուտի և ներդրման տարբերությունը։ ', pi, '\n' 
      'եկամտի և հարկերի տարբերությունը։ ', t, '\n'
      'հարկերի և ներդրման տարբերությունը։  ', t2)
