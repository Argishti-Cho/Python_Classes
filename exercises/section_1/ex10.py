# 10-ի քառակուսին հավասար է 100-ի հետևաբար 100-ի լօգարիթմը 2-ն է։
# օր․ լօգ2 -ի 8-ը  հավասար է 3 քանի որ 2-ը 3 անգամ բազմապատկվել է որ դառնա 8
# 8ի լոգ2 հասկանալու համար պետք է հաշվել քանի անգամ է 
# 2ը բազմապատկվել ինքն իրենով  որ դառնա 8
import math as m

a = int(input('add 1st digits: '))
b = int(input('add 2nd digits: '))

print(f'''      sum: {a + b} 
      subtract: {a - b} 
      multiply: {a * b} 
      quotient: {a // b} 
      reminder: {a % b}
      result log 10 a astijan kam a-n inchi qarakusi astijann a: {round(m.log10(a), 2)}
      result of a-i b astijan: {a ** b}''')
      