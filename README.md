This repository contains an implementation of the classic 2048 game using Python's Tkinter library. The game is a sliding block puzzle where the objective is to combine tiles with the same number to create a tile with the number 2048.
Features

Smooth Animations: The game updates in real-time with smooth animations for tile movement and merging.
Scoring System: Tracks the player's score and displays it on the game window.
Game Over and Win Conditions: Displays messages for game over and winning the game.
Random Tile Generation: Adds new tiles at random positions after each move.
How to Play

Move Tiles: Use the arrow keys on your keyboard to move the tiles up, down, left, or right.
Combine Tiles: When two tiles with the same number collide, they merge into one tile with the sum of the two numbers.
Win the Game: Create a tile with the number 2048 to win the game.
Game Over: The game ends when there are no empty spaces and no adjacent tiles with the same number.

Code Structure

GameBoard Class
Handles the graphical representation of the game grid and updates the tiles.

Attributes:

tile_bg_colors: Background colors for tiles.
tile_text_colors: Text colors for tiles.
size: Size of the game grid.
window: Tkinter window for the game.
game_area: Frame containing the game grid.
board: List of labels representing the grid cells.
cells: 2D list representing the tile values.
compressed, merged, moved: Flags for tracking game state.
score: Current score of the game.
Methods:

reverse_grid(): Reverses the order of cells in each row.
transpose_grid(): Transposes the grid.
compress_grid(): Compresses the grid by moving non-zero tiles to the left.
merge_grid(): Merges adjacent tiles with the same value.
add_random_tile(): Adds a new tile with value 2 at a random empty position.
can_merge(): Checks if any adjacent tiles can be merged.
update_grid(): Updates the graphical representation of the grid.

GameController Class
Manages the game logic, processes user input, and handles game state transitions.

Attributes:

board: Instance of the GameBoard class.
game_over, game_won: Flags for tracking game state.
Methods:

start(board): Initializes the game, adds the initial tiles, and starts the main event loop.
process_key_press(event): Processes key presses and updates the game state accordingly.
