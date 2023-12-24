import tkinter as tk
from board import CheckersBoard


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        # Создание и настройка окна
        self.title('Евразийские шашки')
        self.geometry('700x700')
        self.resizable(False, False)
        self.board = CheckersBoard(self)
        self.start_the_game()

    def mainloop(self, n=0):
        super().mainloop()
        self.start_the_game()

    def start_the_game(self):
        self.board.start_game()


