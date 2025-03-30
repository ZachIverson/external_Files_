#-----------------------------
# file_handling_game.py
# Zach Ignacio
# Uses your own external files
#Writes to a text file - for example - high scores, level, inventory, save game data, etc.
#Read a text file - for example - load savegame data, high scores, user names, etc
#-----------------------------

import os     # Provides functions to interact with the operating system, like checking if a file exists.

player_data = {} 

def load_player_data():
    """Loads player data from a file into a dictionary."""
    player_name = input("Enter your name: ")
    filename = player_name + ".txt"
    if not os.path.exists(filename):
        print("No saved data found. Starting a new game.")
        player_data["Name"] = player_name
        player_data["Level"] = "1"
        player_data["Health"] = "100"
    else:
        try:
            with open(filename, "r") as file:
                data = file.read().split(",")
                for i in range(0, len(data), 2):
                    player_data[data[i]] = data[i + 1]
            print("Welcome back, " + player_data["Name"] + "!")
        except Exception as e:
            print(f"Error loading game data: {e}")
    return filename

def update_player_data():
    """Updates player's stats in the dictionary."""
    print(f"Current Level: {player_data['Level']}, Health: {player_data['Health']}")
    print("You won a challenge and gained experience!")
    player_data["Health"] = "50"
    player_data["Level"] = "5"
    player_data["Class"] = input("Choose your character class (Warrior, Mage, Rogue, etc.): ")
    print("Updated Stats:", player_data)

def save_player_data(filename):
    """Saves the updated player data to the file."""
    try:
        with open(filename, "w") as file:
            for key, value in player_data.items():
                file.write(f"{key},{value},")
        print("Game saved successfully.")
    except Exception as e:
        print(f"Error saving game data: {e}")

def main():
    filename = load_player_data()
    print(f"Welcome, {player_data['Name']}!")
    input("Press Enter to continue...")
    update_player_data()
    input("Press Enter to save your progress...")
    save_player_data(filename)

#-----------------------Main Code------------------------
main()
