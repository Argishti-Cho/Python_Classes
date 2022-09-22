
def check(text):
    # global digits 
    digits = 0
    # global letters
    letters = 0
    for i in text:
        if i.isalpha():
            letters += 1
        elif i.isnumeric():
            digits += 1
    return digits, letters

print(check(input('Enter text:  ')))
# print(digits, letters)
