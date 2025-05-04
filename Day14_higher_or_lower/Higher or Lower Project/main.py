from random import randint
from game_data import data
import art

#Return a random number but not the same as an already selected one.
def select_random(a_choice):
    rand_num = randint(0,len(data)-1)
    while rand_num == a_choice:
        rand_num = randint(0,len(data)-1)
    return rand_num

def loser(final_score):
    print("\n" * 20)
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {final_score}")

def compare_a_b(a_num, b_num, selection):
    if selection == 'a':
        if int(data[a_num]["follower_count"]) >= int(data[b_num]["follower_count"]):
            return True
        else:
            return False
    if selection == 'b':
        if int(data[a_num]["follower_count"]) <= int(data[b_num]["follower_count"]):
            return True
        else:
            return False

def game_play():
    playing_game = True
    player_score = 0
    a_selection_num = select_random(-1)

    while playing_game:
        b_selection_num = select_random(a_selection_num)

        print(art.logo)
        if player_score > 0:
            print(f"You're right! Current score: {player_score}.")
        print(f"Compare A: {data[a_selection_num]['name']}, a {data[a_selection_num]['description']}, from {data[a_selection_num]['country']}.")
        print(art.vs)
        print(f"Against B: {data[b_selection_num]['name']}, a {data[b_selection_num]['description']}, from {data[b_selection_num]['country']}.")
        player_selection = input("Who has more follower? Type 'A' or 'B':").lower()

        if compare_a_b(a_selection_num, b_selection_num, player_selection):
            player_score += 1
            if player_selection == 'a':
                a_selection_num = a_selection_num
            else:
                a_selection_num = b_selection_num
            print("\n" * 20)

        else:
            loser(player_score)
            playing_game = False

game_play()