from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from variables import BIG_FONT_SIZE, TEXT_MARGIN

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configDisplay()

    def configDisplay(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setTextMargins(*margins)

