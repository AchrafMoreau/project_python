import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [' ' for x in range(9)]
        self.player = 'X'
        self.winner = None
        self.buttons = []

        for i in range(9):
            button = tk.Button(self.master, text=" ", font=('Helvetica', '20'), height=2, width=4,
                               command=lambda i=i: self.move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def move(self, position):
        if self.winner or self.board[position] != ' ':
            return

        self.board[position] = self.player
        self.buttons[position].config(text=self.player)

        if self.is_victory(self.player):
            self.winner = self.player
            print(f"the {self.winner} player Win!")
            self.master.destroy()

        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

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

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
