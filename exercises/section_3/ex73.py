
a = 'XYZABCDEFGHIJKLMNOPQRSTXYZ'
text = input('enter: ').upper()
s = ''
for i in text:
    if i in text:
        s += a[a.index(i) + 3]
    else:
        print('none')
print(s)


