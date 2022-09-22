mydict = {'a': '1', 'b': '2', 'c': '2'}
l = {}
for i, j in mydict.items():
    l.setdefault(j, []).append(i)
print(l)

# ------------------ 2 diferent exercises ------------------
s = 'a,2,b,5,c,8,a,4,e,11'
mydict = {}
s = s.split(',')
for i in range(0, len(s), 2):
    if s[i] in mydict:
        mydict[s[i]] += int(s[i+1])
    else:
        mydict[s[i]] = int(s[i+1])
print(mydict)





