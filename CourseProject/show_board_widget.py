from PySide6.QtWidgets import QPushButton, QDialog, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QRunnable, QThreadPool, Slot
from chess import ChessSolver
from tiles_button import TilesButton

class ShowBoardWidget(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Show Board")
        self.parent = parent
        self.chess = ChessSolver(parent.board_size)
        self.amount = parent.amount
        self.placed_pieces = self.parent.placed_pieces.copy()
        #print("Placed Pieces: ", self.placed_pieces)
        self.tiles_under_attack = self.parent.tiles_under_attack.copy()

        layout_grid = QGridLayout()
        self.tiles = [[TilesButton("0") for i in range(0, parent.board_size + 1)] for j in range(0, parent.board_size + 1)]
        for i in range(0, len(self.tiles) - 1):
            for j in range(0, len(self.tiles) - 1):
                layout_grid.addWidget(self.tiles[i][j], i, j)
                self.tiles[i][j].setCheckable(False)

        for i in self.placed_pieces:
            self.tiles[i[0]][i[1]].setText("-1")
            self.chess.place_piece(i[0], i[1])

        for i in self.tiles_under_attack:
            self.tiles[i[0]][i[1]].setText("*")

        solution = self.chess.compute(self.amount, 1)
        c1 = ChessSolver(self.parent.board_size)
        if solution is None:
            #print("no solution found")
            dlg = QDialog()
            dlg.setFixedSize(200, 70)
            lb = QLabel("No solution found")
            lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
            b1 = QPushButton("Ok")
            b1.clicked.connect(dlg.close)
            layout = QVBoxLayout()
            layout.addWidget(lb)
            layout.addWidget(b1)
            dlg.setLayout(layout)
            dlg.exec()
        else:
            for i in solution:
                self.tiles[i[0]][i[1]].setChecked(True)
                self.tiles[i[0]][i[1]].setText("-1")
                moves = c1.place_piece(i[0], i[1])
                c1.remove_piece(i[0], i[1])
                for j in moves:
                    self.tiles[j[0]][j[1]].setDisabled(True)
                    self.tiles[j[0]][j[1]].setText("*")

        #print(solution)
        # compute and write to file button
        self.write_bt = QPushButton("Write to File")
        self.write_bt.clicked.connect(self.write_bt_clicked)

        # close button
        self.close_bt = QPushButton("Close")
        self.close_bt.clicked.connect(self.close)

        layout_bts = QHBoxLayout()
        layout_bts.addWidget(self.write_bt)
        layout_bts.addWidget(self.close_bt)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_grid)
        layout_main.addLayout(layout_bts)
        self.setLayout(layout_main)

        self.threadpool = QThreadPool()

    def write_bt_clicked(self):
        worker = ChessWorker(self.parent.board_size, self.placed_pieces, self.amount)
        self.threadpool.start(worker)

class ChessWorker(QRunnable):
    def __init__(self, dimensions, placed_pieces, amount):
        super().__init__()
        self.chess = ChessSolver(dimensions)
        for i in placed_pieces:
            self.chess.place_piece(i[0], i[1])
        self.amount = amount

    @Slot()
    def run(self):
        print("Thread Starts")
        self.chess.compute(self.amount)
        print("Thread Stops")
        dlg = QDialog()
        dlg.setFixedSize(300, 70)
        lb = QLabel("Writing to the file is done")
        lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bt1 = QPushButton("Ok")
        bt1.clicked.connect(dlg.close)
        layout = QVBoxLayout()
        layout.addWidget(lb)
        layout.addWidget(bt1)
        dlg.setLayout(layout)
        dlg.exec()

