from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from variables import SMALL_FONT_SIZE

class Info(QLabel):
    def __init__(self, text, *args, **kwargs) -> None:
        super().__init__(text, *args, **kwargs)
        self.configLabel()
    
    def configLabel(self):
        self.setStyleSheet(f"font-size: {SMALL_FONT_SIZE}px")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)