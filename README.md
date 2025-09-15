## How to Run application

1. Run main.py
2. Input 1 for game 1 or 2 for game 2

## Scalability
1. Additional spaces on the board and players can be added to this game.

## Future improvements
1. Add ability to simulate and Play the game with inputs for each player.
2. Add ability to create new spaces and add additional players from within the game

Your task is to write an application to play the game of Woven Monopoly.

In Woven Monopoly, when the dice rolls are set ahead of time, the game is deterministic.

### Game rules
* There are four players who take turns in the following order:
  * Peter
  * Billy
  * Charlotte
  * Sweedal
* Each player starts with $16
* Everybody starts on GO
* You get $1 when you pass GO (this excludes your starting move)
* If you land on a property, you must buy it
* If you land on an owned property, you must pay rent to the owner
* If the same owner owns all property of the same colour, the rent is doubled
* Once someone is bankrupt, whoever has the most money remaining is the winner ** What happens is multiple players have the same most money? Assumed: returning multiple winners here. **
* There are no chance cards, jail or stations
* The board wraps around (i.e. you get to the last space, the next space is the first space)


### Your task
* Load in the board from board.json
* Implement game logic as per the rules
* Load in the given dice rolls files and simulate the game
  * Who would win each game?
  * How much money does everybody end up with?
  * What spaces does everybody finish on?

