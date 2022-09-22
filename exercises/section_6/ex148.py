# import random

# card = {k: random.sample(range(1, 15), 5) for k in 'BINGO'}
# print(card)

import random

random_draw_list = random.sample(range(1, 76), 75)

def generate_card():
    card = {"B": [], "I": [], "N": [], "G": [], "O": [],}
    min_ = 1
    max_ = 15
    for letter in card:
        card[letter] = random.sample(range(min_, max_), 5)
        min_ += 15
        max_ += 15

    return card

def print_card(card):

    for letter in card:
        print(letter, end="\t")
        for number in card[letter]:
            print(number, end="\t")
        print("\n")
    print("\n")

def draw(card, list):

    number_drawn = random_draw_list.pop()
    for letter in card:
        i = 0
        for number in card[letter]:
            if number == number_drawn:
                card[letter][i] = "X"
            i += 1
    return number_drawn

def check_win(card):

    win = False
    if card["B"][0] == "X" and card["I"][1] == "X" and card["N"][2] == "X" and card["G"][3] == "X" and card["O"][4] == "X":
        win = True
    elif card["O"][0] == "X" and card["G"][1] == "X" and card["N"][2] == "X" and card["I"][3] == "X" and card["B"][4] == "X":
        win = True
    elif card["B"][0] == "X" and card["O"][4] == "X" and card["B"][4] == "X" and card["O"][0] == "X":
        win = True
    for letter in card:
        if(len(set(card[letter]))==1):
            win = True
    for i in range(5):
        cnt = 0
        for letter in card:
            if card[letter][i] == "X":
                cnt += 1
        print(cnt)
        if cnt == 5:
            win = True
            break
    return win

def main():

    print("Let's play bingo!")
    card = generate_card()

    print("\nHere is your card:\n")
    print_card(card)

    print("\nKeep pressing enter to continue or type quit to exit.\n")
    user_input = input()
    win = check_win(card)
    balls_till_win = 0

    while win == False and user_input != "quit":
        number_drawn = draw(card, random_draw_list)
        balls_till_win += 1

        print(f"\nNumber drawn: {number_drawn}.")
        print(f"Total balls drawn: {balls_till_win}.\n")
        print_card(card)

        win = check_win(card)

        user_input = input()
    if win == True:
        print(f"\nBingo! Total balls to win: {balls_till_win}.")
    else:
        print("Goodbye! Thanks for playing!")

main()