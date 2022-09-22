import random
summ = 0
for x in range(10):
    s = ''
    count = 0
    while True:
        x = random.choice(["HEADS", "TAILS"])
        for i in x:
            if x == "HEADS":
                print('HEADS')
                s += x
                count += 1
                summ += 1

# import random
# # flips = 'heads', 'tails'
# summ = 0
# for i in range(10):
#     count = 0
#     s = ''
#     while True:
#         x = random.choice('ft')
#         s += f'{x} '
#         count += 1
#         summ += 1
#         if len(s) < 6:
#             continue
#         else:
#             if s[-2] == s[-4] == s[-6]:
#                 print(f'{s} (count: {count})')
#                 break
# print(f'Mean: {summ / 10}')

# import random
# def coin_flip():
#     """Randomly return 'heads' or 'tails'."""
#     if random.randint(0, 1) == 0:
#         return "heads"
#     else:
#         return "tails"


# flips = 0
# num_trials = 10_000

# for trial in range(num_trials):
#     # Flip the coin once and increment the flips tally by 1
#     first_flip = coin_flip()
#     flips = flips + 1
#     # Continue flipping the coin and updating the tally until
#     # a different result is returned by coin_flips()
#     while coin_flip() == first_flip:
#         flips += 1
#     # Increment the flip tally once more to account for the
#     # final flip with a different result
#     flips += 1

# avg_flips_per_trial = flips / num_trials
# print(f"The average number of flips per trial is {avg_flips_per_trial}.")