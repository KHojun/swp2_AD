#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel, QComboBox, QSizePolicy

class SutdaGame(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("섯다")
        self.mainLayout = QGridLayout();
        


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = SutdaGame()
    game.show()
    sys.exit(app.exec_())
