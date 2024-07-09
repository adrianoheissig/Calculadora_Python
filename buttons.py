from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import MED_FONT_SIZE

class Button(QPushButton):
    def __init__(self, text: str, *args, **kwargs) -> None: 
        super().__init__(text, *args, **kwargs)
        self._configStyle()
    
    def _configStyle(self):
        font = self.font()
        font.setPixelSize(MED_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75,75)

class ButtonsGrid(QGridLayout):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent,*args, **kwargs)

        self._gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self._makeGrid()
    
    def _makeGrid(self):
        for (idr,line) in enumerate(self._gridMask):
            for (idc, cell) in enumerate(line):
                button = Button(cell)
                self.addWidget(button, idr, idc)