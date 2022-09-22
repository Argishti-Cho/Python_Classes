# Taking user input
binary_num = input("Enter the Binary Number: ")
dec_num = 0
m = 1

# Converting binary into decimal
for digit in binary_num:
    digit= int(digit)
    dec_num = dec_num + (digit * m)
    m = m * 2
print(dec_num)