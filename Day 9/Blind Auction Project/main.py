import art
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
print(art.logo)
bid_list = {}

bidding_active = True

while bidding_active:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_list[name] = bid

    another_bidder = input("Is there another bidder? (yes/no): ").lower()
    if another_bidder == "no":
        bidding_active = False
    else:
        print("\n" * 30)

winning_name = ""
winning_bid = 0
for name in bid_list:
    if bid_list[name] > winning_bid:
        winning_name = name
        winning_bid = bid_list[name]

print(f"The winner is {winning_name} with a bid of ${winning_bid}")