# ===============================================
# File: player.py
# Description: Holds the player class
# Author: Shane Zahra
# Date: 2025-08-13
# ===============================================


class Player:
  def __init__(self, first_name, money=16, property_owned=None, current_position=0, is_bankrupt=False):
    self.first_name = first_name
    self.money = money
    self.property_owned = property_owned
    self.current_position = current_position
    self.is_bankrupt = is_bankrupt

# p1 = Player("Peter", 16, None, 0, False) Example