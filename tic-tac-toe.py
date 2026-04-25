import random

class TicTacToe:

    def __init__(self):

        """
        Initialising the board, player symbols, scores, control flags, and history tracking
        """

        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.player1_symbol = ""
        self.player2_symbol = ""
        self.current_player = ""

        self.score_player1 = 0
        self.score_player2 = 0
        self.draws = 0

        self.playing = True
        self.game_over = False

        self.player1_name = ""
        self.player2_name = ""

        self.history = []

        self.vs_computer = False

    def print_board(self, highlight=None):

        """
        this function prints Tic Tac Toe matrix, and also appends [] to the winning row/col/(anti) diagonal
        """

        print("    0   1   2")

        for i in range(3):
            row_display = []

            for j in range(3):
                cell = self.board[i][j]

                if highlight and (i, j) in highlight:
                    row_display.append("[" + cell + "]")
                else:
                    row_display.append(" " + cell + " ")

            print(f"{i}  " + "|".join(row_display))

            if i < 2:
                print("   ---+---+---")

    def reset_board(self):

        """
        this function resets the board
        """

        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.game_over = False
        self.current_player = self.player1_symbol

    def changePlayer(self):

        """
        this function switches the turn between players, based on the symbol
        """

        if self.current_player == self.player1_symbol:
            self.current_player = self.player2_symbol
        else:
            self.current_player = self.player1_symbol

    def isDraw(self):

        """
        this function checks for draw (True, if every cell is filled)
        """

        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False

        return True

    def make_move(self, row, col):

        """
        this function apends the player's choosen symbol on the matrix, if it's a legal move. False, if the move is illegal, or the cell was occupied
        """

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Out of range move!")
            return False

        if self.board[row][col] != " ":
            print("Cell is already taken!")
            return False

        self.board[row][col] = self.current_player
        return True

    def computer_move(self):

        """
        this function makes a random legal move 
        """

        empty = []

        for r in range(3):
            for c in range(3):
                if self.board[r][c] == " ":
                    empty.append((r, c))

        row, col = random.choice(empty)
        self.make_move(row, col)

    def isWin(self, player):

        """
        this function checks if a player has won (True if row, coloumn, (anti) diagonal), False otherwise
        this function also returns win status, the type of the win, as well as the positions of the winning cell
        """

        for r in range(3):
            if self.board[r][0] == player and self.board[r][1] == player and self.board[r][2] == player:
                return True, "Row", r, [(r,0), (r,1), (r,2)]

        for c in range(3):
            if self.board[0][c] == player and self.board[1][c] == player and self.board[2][c] == player:
                return True, "Column", c, [(0,c), (1,c), (2,c)]

        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True, "Diagonal", 0, [(0,0), (1,1), (2,2)]

        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True, "Anti-Diagonal", 0, [(0,2), (1,1), (2,0)]

        return False, None, None, None

    def get_current_player_name(self):

        """
        this function returns the name of the player whose turn it is currently
        """

        if self.current_player == self.player1_symbol:
            return self.player1_name
        else:
            return self.player2_name

    def print_score(self):

        """
        this function prints the current scoreboard (win(s) for the player(s), and also the draws)
        """

        print("\n===== SCOREBOARD =====")
        print(self.player1_name + " (" + self.player1_symbol + "):", self.score_player1)
        print(self.player2_name + " (" + self.player2_symbol + "):", self.score_player2)
        print("Draws   :", self.draws)
        print("======================\n")

    def print_history(self):

        """
        this function prints the history (win(s) and draw(s)) all concluded games
        """

        print("\n===== GAME HISTORY =====")
        for i in range(len(self.history)):
            print("Game", i + 1, ":", self.history[i])
        print("========================\n")  

    def play_single_game(self):

        """
        this function runs a round of the game, and switches turns between the player(s) and computer (if selected) till a win or draw
        """

        self.reset_board()

        while self.game_over == False:

            self.print_board()

            valid_move = False  

            if self.vs_computer and self.current_player == self.player2_symbol:

                self.computer_move()
                valid_move = True

            else:

                try:
                    row = int(input(self.get_current_player_name() + " row (0-2): "))
                    col = int(input(self.get_current_player_name() + " col (0-2): "))
                except ValueError:
                    print("Please enter numbers only!")
                else:
                    valid_move = self.make_move(row, col)

            if valid_move:

                win, win_type, index, highlight = self.isWin(self.current_player)

                if win:
                    self.print_board(highlight)

                    player_display = self.get_current_player_name() + " (" + self.current_player + ")"

                    if win_type == "Row":
                        print(player_display + " wins on Row " + str(index) + "!")
                        result = player_display + " - Row " + str(index)
                    elif win_type == "Column":
                        print(player_display + " wins on Column " + str(index) + "!")
                        result = player_display + " - Column " + str(index)
                    elif win_type == "Diagonal":
                        print(player_display + " wins on Main Diagonal!")
                        result = player_display + " - Main Diagonal"
                    else:
                        print(player_display + " wins on Anti-Diagonal!")
                        result = player_display + " - Anti-Diagonal"

                    self.history.append(result)

                    if self.current_player == self.player1_symbol:
                        self.score_player1 += 1
                    else:
                        self.score_player2 += 1

                    self.game_over = True

                elif self.isDraw():
                    self.print_board()
                    print("It's a draw!")
                    self.draws += 1
                    self.history.append("Draw")
                    self.game_over = True

                else:
                    self.changePlayer()

    def show_final_result(self):

        """
        this function prints the final result of all the games played, and also prints the overall winner
        this function also prints the game history 
        """

        print("\n===== FINAL RESULT =====")
        print(self.player1_name + " (" + self.player1_symbol + "):", self.score_player1)
        print(self.player2_name + " (" + self.player2_symbol + "):", self.score_player2)
        print("Draws   :", self.draws)

        if self.score_player1 > self.score_player2:
            print("Overall Winner:", self.player1_name)
        elif self.score_player2 > self.score_player1:
            print("Overall Winner:", self.player2_name)
        else:
            print("Overall Result: Tie")

        print("========================\n")

        self.print_history()

    def play_game(self):

        """
        this function control the loop of the game and handles the setup, mode (whether opponent is human or computer) selection, the symbol of the player(s), and also handles multiple games 
        """

        print("Welcome to Tic-Tac-Toe!\n")

        self.player1_name = input("Enter Player 1 name: ")
        self.player2_name = input("Enter Player 2 name (or 'Computer'): ")

        mode = input("Play against computer? (y/n): ").lower()
        self.vs_computer = (mode == "y")

        self.player1_symbol = input(self.player1_name + " choose your symbol: ")

        while self.player1_symbol == "":
            print("Symbol cannot be empty!")
            self.player1_symbol = input(self.player1_name + " choose your symbol: ")

        self.player2_symbol = input(self.player2_name + " choose your symbol: ")

        while self.player2_symbol == "" or self.player2_symbol == self.player1_symbol:
            if self.player2_symbol == "":
                print("Symbol cannot be empty!")
            else:
                print("Symbol already taken by " + self.player1_name + "! Choose a different symbol.")
            self.player2_symbol = input(self.player2_name + " choose your symbol: ")

        self.current_player = self.player1_symbol

        while self.playing == True:

            self.play_single_game()
            self.print_score()

            again = input("Play again? (y/n): ").lower()

            if again == "y":
                self.playing = True
            else:
                self.show_final_result()
                print("Thanks for playing!")
                self.playing = False


#this automatically the game when the python file is run on VSC
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

