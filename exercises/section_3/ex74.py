# I think it's wrong 

n = int(input('Enter number:   '))

guess = 0.5 * n
better = 0.5 * (guess + n/guess)

while better != guess:
    guess = better
    better = 0.5 * (guess + n/guess)
print(guess)
