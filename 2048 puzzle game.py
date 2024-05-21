from tkinter import *
from tkinter import messagebox
import random

class GameBoard:
    tile_bg_colors = {
        '2': '#eee4da', '4': '#ede0c8', '8': '#edc850', '16': '#edc53f',
        '32': '#f67c5f', '64': '#f65e3b', '128': '#edcf72', '256': '#edcc61',
        '512': '#f2b179', '1024': '#f59563', '2048': '#edc22e'
    }
    tile_text_colors = {
        '2': '#776e65', '4': '#f9f6f2', '8': '#f9f6f2', '16': '#f9f6f2',
        '32': '#f9f6f2', '64': '#f9f6f2', '128': '#f9f6f2', '256': '#f9f6f2',
        '512': '#776e65', '1024': '#f9f6f2', '2048': '#f9f6f2'
    }

    def __init__(self):
        self.size = 4
        self.window = Tk()
        self.window.title('2048 Game')
        self.game_area = Frame(self.window, bg='azure3')
        self.board = []
        self.cells = [[0]*4 for _ in range(4)]
        self.compressed = False
        self.merged = False
        self.moved = False
        self.score = 0

        for i in range(4):
            row = []
            for j in range(4):
                label = Label(self.game_area, text='', bg='azure4', font=('arial', 22, 'bold'), width=4, height=2)
                label.grid(row=i, column=j, padx=7, pady=7)
                row.append(label)
            self.board.append(row)
        self.game_area.grid()
#manya
    def reverse_grid(self):
        for idx in range(4):
            self.cells[idx] = self.cells[idx][::-1]

    def transpose_grid(self):
        self.cells = [list(row) for row in zip(*self.cells)]

    def compress_grid(self):
        self.compressed = False
        new_grid = [[0]*4 for _ in range(4)]
        for i in range(4):
            pos = 0
            for j in range(4):
                if self.cells[i][j] != 0:
                    new_grid[i][pos] = self.cells[i][j]
                    if pos != j:
                        self.compressed = True
                    pos += 1
        self.cells = new_grid

    def merge_grid(self):
        self.merged = False
        for i in range(4):
            for j in range(3):
                if self.cells[i][j] == self.cells[i][j + 1] and self.cells[i][j] != 0:
                    self.cells[i][j] *= 2
                    self.cells[i][j + 1] = 0
                    self.score += self.cells[i][j]
                    self.merged = True

    def add_random_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.cells[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.cells[i][j] = 2

    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.cells[i][j] == self.cells[i][j + 1]:
                    return True
        for i in range(3):
            for j in range(4):
                if self.cells[i + 1][j] == self.cells[i][j]:
                    return True
        return False
#------
    def update_grid(self):
        for i in range(4):
            for j in range(4):
                value = self.cells[i][j]
                if value == 0:
                    self.board[i][j].config(text='', bg='azure4')
                else:
                    self.board[i][j].config(text=str(value),
                                            bg=self.tile_bg_colors.get(str(value), 'black'),
                                            fg=self.tile_text_colors.get(str(value), 'white'))


class GameController:
    def __init__(self):
        self.board = None
        self.game_over = False
        self.game_won = False

    def start(self, board):
        self.board = board
        self.board.add_random_tile()
        self.board.add_random_tile()
        self.board.update_grid()
        self.board.window.bind('<Key>', self.process_key_press)
        self.board.window.mainloop()

    def process_key_press(self, event):
        if self.game_over or self.game_won:
            return

        self.board.compressed = False
        self.board.merged = False
        self.board.moved = False

        key = event.keysym

        if key == 'Up':
            self.board.transpose_grid()
            self.board.compress_grid()
            self.board.merge_grid()
            self.board.moved = self.board.compressed or self.board.merged
            self.board.compress_grid()
            self.board.transpose_grid()

        elif key == 'Down':
            self.board.transpose_grid()
            self.board.reverse_grid()
            self.board.compress_grid()
            self.board.merge_grid()
            self.board.moved = self.board.compressed or self.board.merged
            self.board.compress_grid()
            self.board.reverse_grid()
            self.board.transpose_grid()

        elif key == 'Left':
            self.board.compress_grid()
            self.board.merge_grid()
            self.board.moved = self.board.compressed or self.board.merged
            self.board.compress_grid()

        elif key == 'Right':
            self.board.reverse_grid()
            self.board.compress_grid()
            self.board.merge_grid()
            self.board.moved = self.board.compressed or self.board.merged
            self.board.compress_grid()
            self.board.reverse_grid()

        self.board.update_grid()
        print(self.board.score)

        if any(2048 in row for row in self.board.cells):
            self.game_won = True
            messagebox.showinfo('2048', 'You Won!!')
            print("won")
            return

        if not any(0 in row for row in self.board.cells) and not self.board.can_merge():
            self.game_over = True
            messagebox.showinfo('2048', 'Game Over!!!')
            print("Over")

        if self.board.moved:
            self.board.add_random_tile()

        self.board.update_grid()


if __name__ == "__main__":
    game_board = GameBoard()
    game_controller = GameController()
    game_controller.start(game_board)
