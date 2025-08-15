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
        self.current_turn = 0 # Tracks the current turn in the game

    def create_players(self):
        p1 = Player("Peter")
        p2 = Player("Billy")
        p3 = Player("Charlotte")
        p4 = Player("Sweedal")
        self.players.extend([p1, p2, p3, p4]) # Store the players in a list.

    def current_player(self):
        return self.players[self.current_turn]
    
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
            with open('rolls_1.json', 'r') as file:
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
        self.current_turn = (self.current_turn + 1) % len(self.players) # uses modulo 4 ie. len of players in game

    def pass_go():
        return None

    def check_winner():
        return None
    
    # player logic possibly move to player class

    def player_movement(self): # may need to rename / split up this function into smaller parts.
        rolls = self.dice_roll()

        for roll_index, roll in enumerate(rolls):  # i is the roll index, roll is the value
            print("---------------------------------------------")
            player = self.current_player() # gets the current player
            print(self.players[self.current_turn].first_name + "'s turn")
            print("---------------------------------------------")
            player.current_position += roll # Moves the current player by the roll value
            print(f"Turn {roll_index}: {player.first_name} rolls {roll}, moves to {player.current_position}")
            self.buy_property()
            self.next_turn() # next players turn

    
    # property logic

    def buy_property(self):
        return None

    def pay_rent():
        return None
    

# === Main ===
if __name__ == "__main__":
    print("-------------")
    print("Starting Game")
    print("-------------")
    my_game = Game()
    print("players:")
    print("-------------")
    for p in my_game.players:
        print(p.first_name)
    print("-------------")
    my_game.game_board()
    my_game.current_player()
    my_game.player_movement()