from art import logo
print(logo)

bid_dictionary={}
should_continue = True

def find_highest_bidder(bidding_dictionary):
    highest_amount = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bid_dictionary[bidder]
        if highest_amount < bid_amount:
            highest_amount = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_amount}")


while should_continue:
    name = input("What is your name? ")
    price = int(input("What is your bid?: $ "))

   # bid_dictionary = {name: price}
    # if name not in bid_dictionary:
    bid_dictionary[name] = price

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if other_bidders == "no":
        should_continue = False
        find_highest_bidder(bid_dictionary)
    elif other_bidders == "yes":
        print("\n" * 50)
