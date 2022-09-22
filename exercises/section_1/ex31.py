kpa = float(input('enter the pressure in kilopascals:  '))
psi = kpa * 0.145038
mm = kpa * 7.50062
sa = kpa / 101.3
print(f'{kpa} kpa is {round(psi, 3)} psi, {round(mm, 3)} mm and {round(sa, 6)} sa')