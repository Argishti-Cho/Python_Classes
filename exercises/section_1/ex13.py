coin_1 = 1
coin_5 = 5
coin_10 = 10
coin_25 = 25
coins = int(input('enter your coins:  '))

# 237 // 25 =10, 237 -(25*10) =12

count_25 = coins // coin_25
result_25 = coins % 25
print(result_25, count_25)
