class TicTacToe:
    def __init__(self):
        self.board = [' ' for x in range(9)]
        self.player = 'X'
        self.winner = None

    def draw(self):
        print(f' {self.board[0]} | {self.board[1]} | {self.board[2]} ')
        print('---+---+---')
        print(f' {self.board[3]} | {self.board[4]} | {self.board[5]} ')
        print('---+---+---')
        print(f' {self.board[6]} | {self.board[7]} | {self.board[8]} ')

    def player_move(self):
        print(f"{self.player}'s turn. Move to which place?")
        move = int(input("Enter the number (1-9): "))
        if self.board[move-1] == ' ':
            self.board[move-1] = self.player
            if self.player == 'X':
                self.player = 'O'
            else:
                self.player = 'X'
        else:
            print("That place is already filled.\nMove to which place?")
            self.player_move()

    def is_victory(self, char):
        if (self.board[0] == char and self.board[1] == char and self.board[2] == char) or \
           (self.board[3] == char and self.board[4] == char and self.board[5] == char) or \
           (self.board[6] == char and self.board[7] == char and self.board[8] == char) or \
           (self.board[0] == char and self.board[3] == char and self.board[6] == char) or \
           (self.board[1] == char and self.board[4] == char and self.board[7] == char) or \
           (self.board[2] == char and self.board[5] == char and self.board[8] == char) or \
           (self.board[0] == char and self.board[4] == char and self.board[8] == char) or \
           (self.board[2] == char and self.board[4] == char and self.board[6] == char):
            return True
        else:
            return False

    def is_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False

    def play(self):
        while not self.is_draw() and not self.winner:
            self.draw()
            self.player_move()
            if self.is_victory(self.player):
                self.winner = self.player
        self.draw()
        if self.winner:
            print(f"{self.winner} won the game!")
        else:
            print("It's a draw.")

game = TicTacToe()
game.play()
