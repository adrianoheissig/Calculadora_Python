from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_TITLE_ICON
from main_window import MainWindow
from display import Display
from info import Info
from styles import SetupTheme

if (__name__ == "__main__"):
    app = QApplication()
    SetupTheme(app)
    window = MainWindow()

    icon = QIcon(str(WINDOW_TITLE_ICON))

    window.addWidget(Info("30 x 10 = 300"))
    pDisplay = Display()

    window.addWidget(pDisplay)    

    window.setWindowIcon(icon)
    window.adjustFixedSize()
    app.setWindowIcon(icon)

    window.show()
    app.exec()