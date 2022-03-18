import sys

from PySide6 import QtCore
from PySide6.QtGui import QColor
from PySide6.QtWidgets import *

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen


# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui.setupUi(self)

        # MAIN WINDOW LABEL


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)


        ## Удаление системного окна
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        self.show()

if __name__ == "__main__":
    app = QApplication()
    window = SplashScreen()
    sys.exit(app.exec())