
password = input('Enter Valid Password Please:  ')
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['+', ',', '.', '-', '?', ':', '_', '(', ')', '*', '/', ';', '+', '!', '#', '$', '%', '&', '%', '^', '=', '~']

l, u, d, s, = 0, 0, 0, 0
if len(password) >= 8 and len(password) <= 300:
    for i in password:
        if i in lowercase:
            l += 1
        if i in uppercase:
            u += 1
        if i in digits:
            d += 1
        if i in symbols:
            s += 1
if l >= 1 and u >= 1 and d >= 1 and s >= 1 and l+u+d+s == len(password):
    print('Your Password is strong enought')
else:
    print('ivalid password ') 

# while len(password) >= 8 and len(password) <= 300:
# l, u, d, s = 0, 0, 0, 0
# if (len(password) >= 8 and len(password) <= 300):
#     for each in password:
#         if each in lowercase:
#             l += 1
#         if each in uppercase:
#             u += 1
#         if each in digits:
#             d += 1
#         if each in symbols:
#             s += 1
# else:
#     print('Add at least 8 charcters please')
# if l >= 1 and u >= 1 and d >= 1 and s >= 1 and len(password) == l + u + d + s:
#     print('your password is valid')
# else:
#     print('invalid password')