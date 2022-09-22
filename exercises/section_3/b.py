from math import floor
t = [15,73,-4,8,52,10,23]
x = t[0]
for i in range(len(t)):
    for j in range(i,len(t)):
        if t[i]>t[j]:
            t[i],t[j] = t[j],t[i]
print(t)
y = int(input())
l = 0
h = len(t)-1
mid = (l + h)//2
while y != t[mid]:
    mid = (l + h)//2
    if y > t[mid]:
        l = mid+1
    elif y < t[mid]:
        h = mid-1
print(mid)