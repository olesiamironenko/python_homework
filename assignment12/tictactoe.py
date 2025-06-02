import time

# Task 6: More on Classes
# 6.2: Declare a class called TictactoeException
# This should inherit from the Exception class.
class TictactoeException(Exception):
    # Add an __init__ method that stores an instance variable called message
    def __init__(self, message):
        self.message = message
        # Call the __init__ method of the superclass
        super().__init__(message)

# 6.3: Declare a class called Board
class Board:
    
    valid_moves=["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

    move_to_coords = {
        "upper left": (0, 0), "upper center": (0, 1), "upper right": (0, 2),
        "middle left": (1, 0), "center": (1, 1), "middle right": (1, 2),
        "lower left": (2, 0), "lower center": (2, 1), "lower right": (2, 2),
    }

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    # 6.4: Add a __str__() method
    def __str__(self):
        lines = []
        for line in self.board_array:
            lines.append(" | ".join(line))
        return "\n---------\n".join(lines)
    
    # 6.5: Add a move() method
    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    # 6.6: Add a whats_next() method
    def whats_next(self):
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] == self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            for i in range(3):
                for j in range(3):
                    if self.board_array[i][j] == " ":
                        cat = False
                    else:
                        cat = True
                    break
            if (cat):
                return (True, "Cat's Game.")

        if not win and not cat:
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")
            
# 6.7: Implement the game within the mainline code of tictactoe.py
if __name__ == "__main__":
    board = Board()
    print("Let's play Tic Tac Toe!")
    time.sleep(1)

    while True:
        print("\nCurrent board:")
        print(board)
        print("\n")
        time.sleep(1)

        game_over, message = board.whats_next()
        if game_over:
            print(message)
            break

        move = input(f"{board.turn}'s move (e.g. 'upper left', 'upper center', 'upper right', 'middle left', 'center', 'middle right', lower left', 'lower center', 'lower right'): ")
        try:
            board.move(move)
        except TictactoeException as e:
            print(f"Error: {e.message}")
        time.sleep(1)
