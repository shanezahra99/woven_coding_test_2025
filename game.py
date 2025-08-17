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
               return property
           
    def board_ui(self):
        current_player = self.get_current_player()
        board_visual = "" + '\n'
        for property_index, property in enumerate(self.board):
            if current_player.current_position == property_index:
                price = property.get('price', 0)
                board_visual += f"| 💎{current_player.first_name}💎 {property['name']} ${price} |"
            else:
                price = property.get('price', 0)
                board_visual += f"| {property['name']} ${price} |"
        print(board_visual + '\n' )

    def get_current_roll(self, roll_index):
        print(f"Rolled: {self.rolls[roll_index]}")
        return self.rolls[roll_index]
    
    def pass_go(self):
        current_player = self.get_current_player()
        current_player.money += 1
    
    # player logic possibly move to player class

    def player_movement(self, roll):
        current_player = self.get_current_player()

        if current_player.current_position + roll >= len(self.board):
            print(f'{current_player.first_name} passed go and gets 1$')
            self.pass_go()

        current_player.current_position = (current_player.current_position + roll) % len(self.board) # Moves the current player by the roll value and loops past go

    def check_winner(self):
        # check all players balance, if its <=0 whoever has the most money wins

        game_over = False

        for player in self.players:
            if player.money <= 0:
                print(f'{player.first_name} is Bankrupt!')
                player.is_bankrupt = True
                game_over = True

        winners = []

        if game_over:
            most_money = -1
            for player in self.players:
                if player.money > most_money:
                    most_money = player.money
                    winners = [player]
                elif player.money == most_money:
                    winners.append(player)
        return winners

    # property logic

    def buy_property(self): # maybe move to player class
        current_player = self.get_current_player()
        current_property = self.get_current_property()
        owner = None
        print(f"{current_player.first_name} currently has ${current_player.money}")
        print(f'{current_player.first_name} landed on property {current_property['name']}')
        colour = current_property.get('colour')
        

        for player in self.players:
            if current_property in player.property_owned: # checks if someone owns the property
                print(f"{player.first_name} owns {current_property['name']}")
                owner = player
                break

        if not owner:

            if current_property['name'] == 'GO':
                pass
            else:

                print(f"There is no owner {current_player.first_name} must buy the property")
                # purchase property
                current_player.money -= current_property.get('price', 0)
                if current_property.get('type') == 'property':
                    current_player.property_owned.append(current_property)
    
        elif owner == current_player:
            print(f"{current_player.first_name} already owns {current_property['name']}")

        elif colour: # Colour checking for rent multiplier
            owner_colours = [property.get('colour') for property in owner.property_owned if property.get('type') == 'property']
            total_colour_count = sum(1 for property in self.board if property.get('colour') == colour)

            if owner_colours.count(colour) == total_colour_count:
                print(f"{owner.first_name} owns all {colour} properties! Rent is doubled.")
                self.pay_rent(rent_multiplier=2)

            else: # pay normal rent
                print(f"{current_player.first_name} must pay rent for {current_property['name']} to {owner.first_name}")
                self.pay_rent()

        print(f"{current_player.first_name} has ${current_player.money} left")

    def pay_rent(self, rent_multiplier=1):
        current_player = self.get_current_player()
        current_property = self.get_current_property()
        print(f"{current_player.first_name} Pays Rent of ${current_property.get('price', 0) * rent_multiplier}")
        current_player.money -= current_property.get('price', 0) * rent_multiplier


    # world Logic

    def game_loop(self):

        print("-------------")
        print("Starting Game")
        print("-------------")
        print("players:")
        print("-------------")
        for p in my_game.players:
            print(p.first_name)
        print("-------------")

        for roll_index, roll in enumerate(self.rolls):
            current_roll = self.get_current_roll(roll_index) 
            my_game.player_movement(current_roll)
            my_game.board_ui()
            my_game.buy_property()

            if len(my_game.check_winner()) > 0:
                print("Game Over")
                exit()

            my_game.next_turn()
            print("----------------------------------------------------")
    
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


# === Main ===
if __name__ == "__main__":
    my_game = Game()
    my_game.game_loop()

