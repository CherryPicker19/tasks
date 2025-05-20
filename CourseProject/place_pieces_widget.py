from PySide6.QtWidgets import QPushButton, QDialog, QGridLayout, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from functools import partial
from chess import ChessSolver
from tiles_button import TilesButton

class PlacePiecesWidget(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Place Pieces")
        self.parent = parent
        self.chess = ChessSolver(parent.board_size)

        self.tiles = [[TilesButton(f"0") for i in range(0, parent.board_size + 1)] for j in range(0, parent.board_size + 1)]
        self.placed_pieces = self.parent.placed_pieces.copy()
        self.tiles_under_attack = self.parent.tiles_under_attack.copy()

        layout_tiles = QGridLayout()
        for i in range(0, len(self.tiles) - 1):
            for j in range(0, len(self.tiles[0]) - 1):
                func = partial(self.tile_bt_clicked, i, j)
                self.tiles[i][j].toggled.connect(func)
                layout_tiles.addWidget(self.tiles[i][j], i, j)

        for i in self.placed_pieces:
            moves = self.chess.place_piece(i[0], i[1])
            self.tiles[i[0]][i[1]].setText("-1")
            for i in moves:
                self.tiles[i[0]][i[1]].setDisabled(True)
                self.tiles[i[0]][i[1]].setText("*")

        layout_buttons = QHBoxLayout()
        self.accept_bt = QPushButton("Accept")
        self.accept_bt.clicked.connect(self.accept_bt_clicked)
        layout_buttons.addWidget(self.accept_bt)

        self.close_bt = QPushButton("Cancel")
        self.close_bt.clicked.connect(self.close_bt_clicked)
        layout_buttons.addWidget(self.close_bt)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_tiles)
        layout_main.addLayout(layout_buttons)
        self.setLayout(layout_main)

    def tile_bt_clicked(self, x: int, y: int, is_pressed: bool):
        board = self.chess.board
        if is_pressed and self.tiles[x][y].is_LMB:
            self.tiles[x][y].setText("-1")
            moves = self.chess.place_piece(x, y)
            self.tiles_under_attack.extend(moves)
            self.placed_pieces.append((x, y))
            for i in moves:
                self.tiles[i[0]][i[1]].setDisabled(True)
                self.tiles[i[0]][i[1]].setText("*")

        elif not is_pressed and not self.tiles[x][y].is_LMB:
            #self.tiles[x][y].setChecked(False)
            self.tiles[x][y].setText("0")
            moves = self.chess.remove_piece(x, y)
            if (x, y) in self.placed_pieces:
                self.placed_pieces.remove((x, y))
            for i in moves:
                if board[i[0]][i[1]] == 0:
                    self.tiles[i[0]][i[1]].setDisabled(False)
                    self.tiles[i[0]][i[1]].setText("0")
                    self.tiles_under_attack.remove((i[0], i[1]))
        else:
            self.tiles[x][y].toggle()
            #self.tiles[x][y].setFlat(True)
            return None
        #print(self.placed_pieces)
        #print(self.tiles_under_attack)
        self.chess.print_board()

    def accept_bt_clicked(self):
        self.parent.tiles_under_attack = self.tiles_under_attack
        self.parent.placed_pieces = self.placed_pieces
        self.parent.chess = self.chess
        self.close()

    def close_bt_clicked(self):
        self.close()