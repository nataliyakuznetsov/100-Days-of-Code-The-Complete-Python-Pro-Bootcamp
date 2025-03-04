import random
from art import logo

def deal_cards():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    """Take a list of cards and return the score calculated the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😏"
    elif c_score > 21:
        return "Opponent went over. You win 😊"
    elif u_score > c_score:
        return "You win 😊"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    comp_cards = []
    comp_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    while not is_game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())

            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_cards())
        comp_score = calc_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score,comp_score))

while  input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 30)
    play_game()
