The project is a console-based implementation of the classic Tic-Tac-Toe game for two players. The game allows players to take turns placing their respective marks (X or O) on a 3x3 grid. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game. If all the squares are filled and no player has won, the game is a tie.

Features:
create_board(row):

Displays the current state of the game board.
create_user():

Allows users to input their chosen marks (X or O).
is_board_full():

Checks if the game board is full, indicating a tie.
winner(i, char):

Checks if a player has won the game based on the current board state.
match_box(l):

Main game loop where players take turns entering their moves.
Verifies if a box is empty before allowing a player to mark it.
Checks for a winner or a tie after each move