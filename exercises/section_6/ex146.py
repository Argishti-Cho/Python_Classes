import random
bingo = {'B': 0, 'I': 0, 'N': 0, 'G': 0, 'O': 0}
bingo2 = {'I': 0, 'N': 0, 'G': 0, 'O': 0, 'B': 0}
bingo3 = {'N': 0, 'G': 0, 'O': 0, 'B': 0, 'I': 0}
bingo4 = {'G': 0, 'O': 0, 'B': 0, 'I': 0, 'N': 0}
bingo5 = {'O': 0, 'B': 0, 'I': 0, 'N': 0, 'G': 0}
for i in bingo.keys():
    b1 = random.randrange(1, 15)
    i1 = random.randrange(16, 30)
    n1 = random.randrange(31, 45)
    g1 = random.randrange(46, 60)
    o1 = random.randrange(61, 75)
    bingo['B'] = b1
    bingo['I'] = i1
    bingo['N'] = n1
    bingo['G'] = g1
    bingo['O'] = o1
    b2 = random.randrange(1, 15)
    i2 = random.randrange(16, 30)
    n2 = random.randrange(31, 45)
    g2 = random.randrange(46, 60)
    o2 = random.randrange(61, 75)
    bingo2['I'] = b2
    bingo2['N'] = i2
    bingo2['G'] = n2
    bingo2['O'] = g2
    bingo2['B'] = o2
    b3 = random.randrange(1, 15)
    i3 = random.randrange(16, 30)
    n3 = random.randrange(31, 45)
    g3 = random.randrange(46, 60)
    o3 = random.randrange(61, 75)
    bingo3['N'] = b3
    bingo3['G'] = i3
    bingo3['O'] = n3
    bingo3['B'] = g3
    bingo3['I'] = o3
    b4 = random.randrange(1, 15)
    i4 = random.randrange(16, 30)
    n4 = random.randrange(31, 45)
    g4 = random.randrange(46, 60)
    o4 = random.randrange(61, 75)
    bingo4['G'] = b4
    bingo4['O'] = i4
    bingo4['B'] = n4
    bingo4['I'] = g4
    bingo4['N'] = o4
    b5 = random.randrange(1, 15)
    i5 = random.randrange(16, 30)
    n5 = random.randrange(31, 45)
    g5 = random.randrange(46, 60)
    o5 = random.randrange(61, 75)
    bingo5['G'] = b5
    bingo5['O'] = i5
    bingo5['B'] = n5
    bingo5['I'] = g5
    bingo5['N'] = o5

print(' B       I        N        G        O')
for k, v in bingo.items():
    print(bingo[k], end='   |   ')
print('\n', '-' *40)
for k, v in bingo2.items():
    print(bingo2[k], end='   |   ')
print('\n', '-' *40)
for k, v in bingo3.items():
    print(bingo3[k], end='   |   ')
print('\n', '-' *40)
for k, v in bingo4.items():
    print(bingo4[k], end='   |   ')
print('\n', '-' *40)
for k, v in bingo5.items():
    print(bingo5[k], end='   |   ')
