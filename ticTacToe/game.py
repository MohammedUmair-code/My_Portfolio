from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time 


class TicTacToe():
    def __init__(self):
        self.board = [" " for i in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None # keep track of winner!
    
    def print_board(self):
        #this is just getting the rows
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print(" | "+ " | ".join(row)+ " | ")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]   
        for row in number_board:
            print(" | " + " | ".join(row) + " | ")

    def available_moves(self): 
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ["x", "x", "o"] ---> [(0, "x"), (1, "x"), (2, "o")] 
        #     if spot == " ":
        #         moves.append(i)
        # return moves 

        return [i for i, spot in enumerate(self.board) if spot == " "]
    
    def empty_squares(self):
        return " " in self.board #This will become a boolean. Empty_squares() will return a boolean on whether or not the board has spaces.
    
    def num_empty_squares(self):
        return self.board.count(" ") #returns the count of empty spaces in the board.
        # return len(self.available_moves())

    def make_move(self, square, letter):
        #if valid move, then make the move (assign square to letter)
        #then return true, if invalid, return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square , letter):
                self.current_winner = letter 
            return True
        return False
    
    def winner(self, square, letter):
        #winner if 3 in a row anywhere.. We have to check all of these!
        #first let's check the row
        row_ind = square //3  #// is the floor division operator
        row = self.board[row_ind*3: (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        #check column 
        col_ind = square % 3
        column = [self.board[col_ind+ i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonals 
        #but only if the square is an even number (0, 2, 4, 6, 8)
        #these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #top left to bottom right diagonal 
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #top right to bottom left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        
        #if all of these fails
        return False


            



def play(game, x_player, o_player, print_game = True):
    #returns the winner of the game!(the letter) or None for a tie
    if print_game:
        game.print_board_nums()
    
    letter = "X" #starting letter 
    #iterate while the game still has empty squares 
    #(we don't have to worry about winner because we'll just return that
    #which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + " " + f"makes a move to square {square}")
                game.print_board()
                print("") #just empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + "Wins!!")
                return letter
    

            # if letter == "X":
            #     letter = "O"
            # else:
            #     letter = "X"
            letter = "O" if letter == "X" else "X" #switches player

        #adding a tiny pause to make it more realistic and more readable for the user
        if print_game:
            time.sleep(0.8)

    if print_game:
        print("It\'s a tie!!")

# if __name__ == "__main__":

#     x_player = HumanPlayer("X")
#     o_player = GeniusComputerPlayer("O")
#     t = TicTacToe()
#     play(t, x_player, o_player, print_game = True)


if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):
        x_player = RandomComputerPlayer("X")
        o_player = GeniusComputerPlayer("O")
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game = False)

        if result == "X":
            x_wins += 1 
        elif result == "O": 
            o_wins += 1 
        else:
            ties += 1 
    
    print(f"After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins and {ties} ties")
        


            

            



        
        





