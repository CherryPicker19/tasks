from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

class TilesButton(QPushButton):
    def __init__(self, arg):
        super().__init__(arg)
        self.setCheckable(True)
        self.is_LMB: bool|None = None
        self.setFixedSize(25, 25)

    def mousePressEvent(self, e, /):
        if e.button() == Qt.MouseButton.LeftButton:
            self.is_LMB = True
        elif e.button() == Qt.MouseButton.RightButton:
            self.is_LMB = False
        self.click()
