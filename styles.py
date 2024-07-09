import qdarkstyle
from PySide6.QtWidgets import QApplication
from variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

class SetupTheme():
    def __init__(self, app: QApplication):
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        app.setStyleSheet(app.styleSheet() + qss)