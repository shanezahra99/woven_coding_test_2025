# ===============================================
# File: game.py
# Description: Holds the game logic
# Author: Shane Zahra
# Date: 2025-08-13
# ===============================================

from player import Player
import json

class Game:

    def __init__ (self): # Instantiate the player objects in the game
        self.players = []
        self.create_players()

    def create_players(self):
        p1 = Player("Peter")
        p2 = Player("Billy")
        p3 = Player("Charlotte")
        p4 = Player("Sweedal")
        self.players.extend([p1, p2, p3, p4]) # Store the players in a list.

    def current_player(self):
        return None
    
    # world Logic
    def game_board(self):
        try:
            with open('board.json', 'r') as file:
                board_data = json.load(file)
                return board_data
        except FileNotFoundError:
            print("Error: file not found.")
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from file.")

    def dice_roll(self):
        # Dice rolls 1
        try:
            with open('rolls_testing.json', 'r') as file:
                rolls1_data = json.load(file)
                return rolls1_data
        except FileNotFoundError:
            print("Error: file not found.")
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from file.")

        # # Dice rolls 2 find an way to simulate the second roll later on
        # try:
        #     with open('rolls_2.json', 'r') as file:
        #         rolls2_data = json.load(file)
        #         return rolls2_data
        # except FileNotFoundError:
        #     print("Error: file not found.")
        # except json.JSONDecodeError:
        #     print("Error: Could not decode JSON from file.")

    def next_turn(self):
        return None
    
    # player logic possibly move to player class

    def player_movement(self):
        return None

    def buy_property(self):
        return None

    def pass_go():
        return None

    def check_winner():
        return None
    
    # property logic

    def pay_rent():
        return None
    

# === Main ===
if __name__ == "__main__":
    pass