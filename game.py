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
        self.board = self.game_board() # potentially move to new class?
        self.rolls = self.dice_roll() # Potentially move to new class? 

    def create_players(self):
        p1 = Player("Peter")
        p2 = Player("Billy")
        p3 = Player("Charlotte")
        p4 = Player("Sweedal")
        self.players.extend([p1, p2, p3, p4]) # Store the players in a list.

    def get_current_player(self):
        return self.players[self.current_turn]

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players) # uses modulo 4 ie. len of players in game

    def get_current_property(self): # returns the property the current player is on
        current_player = self.get_current_player()
        for property_index, property in enumerate(self.board):
           if current_player.current_position == property_index:
               print(f"current property: {property['name']}")
               return property
           
    def get_current_roll(self):
        for roll_index, roll in enumerate(self.rolls):  # i is the roll index, roll is the value
            return roll
    

    def pass_go():
        return None

    def check_winner():
        return None
    
    
    # player logic possibly move to player class

    def player_movement(self): # may need to rename / split up this function into smaller parts.
        current_player = self.get_current_player()
        current_player.current_position += self.get_current_roll() # Moves the current player by the roll value

    
    # property logic

    def buy_property(self): # maybe move to player class
        current_player = self.get_current_player()
        current_property = self.get_current_property()

        ## May need an owner == variable?
        # owner = None

        for player in self.players:
            if current_property['name'] in player.property_owned: # checks if someone owns the property
                print(f"{player.first_name} owns {current_property['name']}")
                
                ## Make current player pay rent to this player

            else:
                print(f"{player.first_name} does not own {current_property['name']}")

                # Make current player buy the property

                print(f"{current_player.first_name} has {current_player.money}")
                current_player.money -= current_property['price'] 
                current_player.property_owned.append(current_property['name'])
                print(f"{current_player.first_name} has {current_player.money}")
                break # this is a cheat way out of the loop test this



    def pay_rent(self):
        current_player = self.get_current_player()
        current_player.money -= 1
    

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


    my_game.get_current_property()
    my_game.get_current_roll()
    my_game.player_movement()
    my_game.buy_property()
    my_game.next_turn()

    print(" ")

    my_game.get_current_property()
    my_game.get_current_roll()
    my_game.player_movement()
    my_game.buy_property()
    my_game.next_turn()
    
    print(" ")

    my_game.get_current_property()
    my_game.get_current_roll()
    my_game.player_movement()
    my_game.buy_property()
    my_game.next_turn()

    print(" ")

    my_game.get_current_property()
    my_game.get_current_roll()
    my_game.player_movement()
    my_game.buy_property()
    my_game.next_turn()
    
    print(" ")


