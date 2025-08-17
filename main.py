# ===============================================
# File: main.py
# Description: starts the application
# Author: Shane Zahra
# Date: 2025-08-13
# ===============================================

from game import Game

def main():
    print("\n ⭐⭐ Starting Woven Monopoly ⭐⭐ \n")
    print(" Welcome! This game uses preset dice rolls, so each run is deterministic. You can choose to simulate Game 1 or Game 2 based on predefined roll sequences.")
    print("""
        Game Rules:
        - Each player starts with $16
        - All players start on GO
        - You collect $1 each time you pass GO (excluding your starting move)
        - Landing on an unowned property means you must buy it
        - Landing on an owned property means you pay rent to the owner
        - If a single owner has all properties of the same colour, rent is doubled!
        - The game ends when a player goes bankrupt; the winner is the player with the most money remaining
        - If multiple players have the same highest amount, they all share the win 
        """)
    my_game = Game()
    my_game.game_loop()

if __name__ == "__main__":
    main()