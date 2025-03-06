from game_data import data
import random
from art import vs, logo
import os

# get the random element from the list
def random_account():
    return random.choice(data)

# format the string
def format_account_string(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_guess(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


def game_start():
    account_a = random_account()
    account_b = random_account()
    continue_game: bool = True
    score: int = 0
    
    print(logo)
    while continue_game:
        account_a = account_b
        while account_a == account_b:
            account_b = random_account()


        print(f"Compare A: {format_account_string(account_a)}")
        print(vs)
        print(f"Against B: {format_account_string(account_b)}")
        follower_count_A = account_a["follower_count"]
        follerwer_count_B = account_b["follower_count"]

        player_guessed = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
        
        if check_guess(player_guessed, follower_count_A, follerwer_count_B):
            score += 1
            print(f"You're right! Your score: {score}")
            # os.system("cls")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final Score: {score}")
            # os.system("cls")

# account = data[0]
# print(format_account_string(account))

if __name__ == "__main__":
    game_start()