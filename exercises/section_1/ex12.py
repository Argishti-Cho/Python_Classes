import math

lt1 = float(input('latitude 1st:  '))
lg1 = float(input('longitude 1st:  '))
lt2 = float(input('latitude 2nd:  '))
lg2 = float(input('longitude 2nd:  '))

lt1 = math.radians(lt1)
lg1 = math.radians(lg1)
lt2 = math.radians(lt1)
lg2 = math.radians(lg2)

# dlon = lg2 - lg1
# dlat = lt2 - lt1
# a = math.sin(dlat / 2)**2 + math.cos(lt1) * math.cos(lt2) * math.sin(dlon / 2)**2
# c = 2 * math.asin(math.sqrt(a))
# r = 6371.01

a = math.acos(math.sin(lt1)*math.sin(lt2) + math.cos(lt1)*math.cos(lt2)*math.cos(lg1-lg2)) 
d = 6371.01
# arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

print(f'{round(a*d, 4)} KM')
# print(f'{c * r} KM')