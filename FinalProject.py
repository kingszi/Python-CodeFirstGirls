import random
import requests

# Random character is chosen by computer
def random_character():
    character = {
        "name": "",
        "height": "",
        "mass": "unknown",
    }

    while character["mass"] == "unknown" or character["mass"] == "1,358":
        character_number = random.randint(1, 83)
        url = "https://swapi.dev/api/people/{}/".format(character_number)
        response = requests.get(url)
        character = response.json()

    return character


def run():

    player_1 = 0
    player_2 = 0
    while (player_1 or player_2) < 3:
        # Computer gets two characters to choose from
        character1 = random_character()
        character2 = random_character()

        # Computer asks for input from user to choose a character
        print("Choose between {} and {}".format(character1['name'], character2['name']))
        character_choice = input("Type your choice (character1/character2): ")

        def chosen_character():
            if character_choice == "character1":
                return character1
            else:
                return character2

        # User input for specific stat for comparison
        my_character = chosen_character()
        stat_choice = input("Which stat do you want to use? (height, mass) ")

        # Computer gets two characters to choose from for opponent
        opponent1 = random_character()
        opponent2 = random_character()
        print("The opponent\'s choices are: {} or {}".format(opponent1['name'], opponent2['name']))

        # Random choice for computer between the two characters
        opponent_choice = random.randint(1, 2)
        if opponent_choice == 1:
            opponent_character = opponent1
        else:
            opponent_character = opponent2

        print("The opponent chose {}".format(opponent_character['name']))

        # The stats of the characters chosen by the user and the opponent/computer
        my_stat = float(my_character[stat_choice])
        opponent_stat = float(opponent_character[stat_choice])

        # Comparison of the stats
        if my_stat >= opponent_stat:
            player_1 = player_1 + 1
            print("Good choice, you won this round!")
        elif my_stat < opponent_stat:
            player_2 = player_2 + 1
            print("Choose better next time, you lost this round!")

        # Comparison of the stats for the winner of 3 rounds
        if player_1 == 3:
            print("Good game, you won {} - {} ". format(player_1, player_2))
        elif player_2 == 3:
            print("Try again, you lost {} - {} ". format(player_2, player_1))


run()