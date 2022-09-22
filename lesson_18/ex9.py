old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]

seen = set()
new_l = []
for d in old_list:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_l.append(d)
print(new_l)
# print(seen)

old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
for i in old_list[::]:
    if old_list.count(i) > 1:
        old_list.remove(i)
print(old_list)