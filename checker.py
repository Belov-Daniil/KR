class Checker:

    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.is_queen = False

    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col
