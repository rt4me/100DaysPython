import random
import art

player_cards = []
computer_cards = []

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def current_score(card_list):
    return sum(card_list)


def replace_11_with_1(card_list):
    if 11 in card_list:
        index = card_list.index(11)
        card_list[index] = 1


def print_final_scores(players_end_cards, players_end_score, computer_end_cards, computer_end_score):
    print(f"   Your final hand: {players_end_cards}, final score: {players_end_score}")
    print(f"   Computer's final hand: {computer_end_cards}, final score: {computer_end_score}")


def blackjack_or_over_check(pl_cards, player_score, comp_cards, computer_score):
    if player_score > 21:
        print_final_scores(pl_cards, player_score, comp_cards, computer_score)
        print("You went over. You lose :^(")
        return True
    elif player_score == 21 and len(pl_cards) == 2:
        print_final_scores(pl_cards, player_score, comp_cards, computer_score)
        print("Win with a Blackjack!")
        return True
    elif computer_score > 21:
        print_final_scores(pl_cards, player_score, comp_cards, computer_score)
        print("Opponent went over. You Win :^)")
        return True
    elif computer_score == 21 and len(comp_cards) == 2:
        print_final_scores(pl_cards, player_score, comp_cards, computer_score)
        print("Lose, opponent has Blackjack 8^O")
        return True
    return False


def play_game():
    print(art.logo)
    player_cards = [draw_card()] + [draw_card()]
    computer_cards = [draw_card()] + [draw_card()]

    player_keep_playing = True

    while player_keep_playing:
        print(f"    Your cards: {player_cards}, current score: {current_score(player_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")

        new_card_ask = input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card_ask == 'y':
            player_cards.append(draw_card())
            player_score = current_score(player_cards)
            if player_score > 21 and 11 in player_cards:
                replace_11_with_1(player_cards)
                player_score = current_score(player_cards)
            if blackjack_or_over_check(player_cards, player_score, computer_cards, current_score(computer_cards)) != False:
                player_keep_playing = False
        elif new_card_ask == 'n':
            computer_path(computer_cards, player_cards)
            player_keep_playing = False


def computer_path(comp_cards, pl_cards):
    computer_keep_playing = True

    while computer_keep_playing == True:
        comp_cards.append(draw_card())
        computer_score = current_score(comp_cards)
        if computer_score > 21 and 11 in comp_cards:
            replace_11_with_1(comp_cards)
            computer_score = current_score(comp_cards)
        if computer_score > 16:
            if blackjack_or_over_check(pl_cards, current_score(pl_cards), comp_cards, computer_score) == False:
                print_final_scores(pl_cards, current_score(pl_cards), comp_cards, computer_score)
                if computer_score == current_score(pl_cards):
                    print("Draw!")
                elif computer_score > current_score(pl_cards):
                    print("You lose :^(")
                elif computer_score < current_score(pl_cards):
                    print("You win!")

            computer_keep_playing = False

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'. : ") == "y":
    print("" * 20)
    play_game()