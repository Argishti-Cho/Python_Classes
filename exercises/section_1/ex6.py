# tips 18%  taxes 16%
# (value*%)/100 ex.= 618*18%/100 = 111
# output = 

order = float(input('add meal order sum: '))

taxes = (order * 16) / 100
tip = (order * 18 ) / 100
total = order + taxes + tip

print('taxes will be: $', taxes)
print('tip will be: $', tip)
print('total ampount: $', total)