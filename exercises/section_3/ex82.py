# tipayin popoxutyun => tivy voxel string-i katarel popoxutyun 
# ev noric shrjel hakarak

q = int(input('enter numbers:  '))
result = ''

while q > 0:
    r = q % 2
    result = str(r) + result
    q = q // 2
print(result)