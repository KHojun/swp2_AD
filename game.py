import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap, QImage


class SutdaGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user_info = []

        self.getCardButton = QToolButton()
        self.getCardButton.setText("패 받기")
        self.getCardButton.clicked.connect(self.getCard)

        left_Layout = QGridLayout()
        left_Layout.addWidget(self.getCardButton, 1, 0)
        self.computer_pae = QLabel(self)
        pixma = QPixmap('2.png')
        self.computer_pae.setPixmap(pixma)
        left_Layout.addWidget(self.computer_pae, 0, 0)

        self.user_pae = QLabel(self)
        pixmap = QPixmap('1.png')
        self.user_pae.setPixmap(pixmap)
        left_Layout.addWidget(self.user_pae, 2, 0)

        # left_money
        self.left_money = QLineEdit()
        self.left_money.setReadOnly(True)
        self.left_money.setAlignment(Qt.AlignRight)
        self.lefted_money = 500
        self.left_money.setText(str(self.lefted_money))

        self.user_name = QLineEdit()
        self.user_name.setAlignment(Qt.AlignRight)

        centerLayout = QGridLayout()
        centerLayout.addWidget(self.left_money, 0, 0, 5, 5)
        centerLayout.addWidget(self.user_name, 1, 0, 1, 1)

        self.btn_Betting = QToolButton()
        self.btn_Betting.setText("BETTING")

        self.btn_Betting = QToolButton()
        self.btn_Betting.setText("BETTING")
        # self.start_btn.clicked.connect()

        self.btn_Die = QToolButton()
        self.btn_Die.setText("DIE")
        # self.btn_Die.clicked.connect()

        self.btn_Save = QToolButton()
        self.btn_Save.setText("SAVE")
        self.btn_Save.clicked.connect(self.save)

        right_laydout = QGridLayout()
        right_laydout.addWidget(self.btn_Betting, 0, 0)
        right_laydout.addWidget(self.btn_Die, 1, 0)
        right_laydout.addWidget(self.btn_Save, 2, 0)

        # Layout placement
        mainLayout = QGridLayout()
        self.setWindowTitle("Sutda")
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(left_Layout, 0, 0)
        mainLayout.addLayout(centerLayout, 0, 1)
        mainLayout.addLayout(right_laydout, 0, 2)
        self.setLayout(mainLayout)

    def getCard(self):
        pass

    def start_game(self):
        pass

    def save(self):
        f = open('user_info.txt', 'w')
        lines = f.readlines()
        f.close()
        self.count = 0
        for line in lines:
            information = line.rstrip()
            self.user_info.append(information)

        # 타임아웃 이벤트가 발생하면 호출되는 메서드
        # 어떤 타이머에 의해서 호출되었는지 확인


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = SutdaGame()

    game.show()

    sys.exit(app.exec_())

