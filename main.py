from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_TITLE_ICON
from main_window import MainWindow
from display import Display
from info import Info
# from buttons import Button, ButtonsGrid
from buttons import ButtonsGrid
from styles import SetupTheme

if (__name__ == "__main__"):
    app = QApplication()
    SetupTheme(app)
    window = MainWindow()

    icon = QIcon(str(WINDOW_TITLE_ICON))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.addWidget(Info("30 x 10 = 300"))
    
    pDisplay = Display()
    window.addWidget(pDisplay)    

    buttonsGrid = ButtonsGrid()

    window.vLayout.addLayout(buttonsGrid)

    # btn1 = Button("1")
    # buttonsGrid.addWidget(btn1)

    window.adjustFixedSize()

    window.show()
    app.exec()