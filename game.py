import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QGraphicsScene
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPixmap, QImage
from card import getCard
from sutda import Sutda
import time
import datetime
from data import cards

class Ranking(QWidget):
    def __init__(self, parent=None):
        super(Ranking, self).__init__(parent)
        self.aa = QLabel()
        lay = QGridLayout()
        self.setLayout(lay)


class SutdaGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user_info = []


        self.log = ""

        self.get_paeButton = QToolButton()
        self.get_paeButton.setText("패 받기")
        self.get_paeButton.clicked.connect(self.Get_card)
        self.get_paeButton.setFixedSize(105,50)

        left_Layout = QGridLayout()
        left_Layout.addWidget(self.get_paeButton, 2, 0)
        cpuDeck = QGridLayout()
        self.computer_pae1 = QLabel(self)
        self.computer_pae2 = QLabel(self)
        self.default = QPixmap('IMG/back.png')
        self.computer_pae1.setPixmap(self.default)
        self.computer_pae2.setPixmap(self.default)
        cpuDeck.addWidget(self.computer_pae1, 0, 0)
        cpuDeck.addWidget(self.computer_pae2, 0, 1)
        left_Layout.addLayout(cpuDeck,1,0)

        cpu = QGridLayout()
        self.cpuLabel = QLabel("CPU")
        font = self.cpuLabel.font()
        font.setPointSize(font.pointSize()+8)
        font.setBold(True)
        font.setFamily('Courier New')
        self.cpuLabel.setAlignment(Qt.AlignTop)
        self.cpuLabel.setFont(font)
        self.cpuResult = QLineEdit()
        self.cpuResult.setReadOnly(True)
        self.cpuResult.setFixedWidth(100)
        self.cpuResult.setAlignment(Qt.AlignCenter)
        cpu.addWidget(self.cpuLabel, 0,0)
        cpu.addWidget(self.cpuResult,1,0)
        left_Layout.addLayout(cpu,1,2)

        userDeck = QGridLayout()
        self.user_pae1 = QLabel(self)
        self.user_pae2 = QLabel(self)
        self.user_pae1.setPixmap(self.default)
        self.user_pae2.setPixmap(self.default)
        userDeck.addWidget(self.user_pae1, 0, 0)
        userDeck.addWidget(self.user_pae2, 0, 1)
        left_Layout.addLayout(userDeck, 3, 0)

        user = QGridLayout()
        self.userLabel = QLabel("Player")
        font = self.userLabel.font()
        font.setPointSize(font.pointSize()+8)
        font.setBold(True)
        font.setFamily('Courier New')
        self.userLabel.setAlignment(Qt.AlignTop)
        self.userLabel.setFont(font)
        self.userResult = QLineEdit()
        self.userResult.setReadOnly(True)
        self.userResult.setFixedWidth(100)
        self.userResult.setAlignment(Qt.AlignCenter)
        user.addWidget(self.userLabel, 0,0)
        user.addWidget(self.userResult,1,0)
        left_Layout.addLayout(user,3,2)

        # left_money
        self.lbLefted = QLabel("보유 금액 :")
        self.lbLefted.setAlignment(Qt.AlignRight)
        self.left_money = QLineEdit()
        self.left_money.setReadOnly(True)
        self.left_money.setAlignment(Qt.AlignRight)
        self.lefted_money = 1000000
        self.left_money.setText(str(self.lefted_money) + '원')
        self.left_money.setFixedWidth(105)

        self.name_edit = QLineEdit()
        self.name_edit.setAlignment(Qt.AlignRight)


        left_Layout.addWidget(self.left_money, 0,2)
        left_Layout.addWidget(self.lbLefted, 0, 0)



        betLayout = QGridLayout()
        self.btn_Betting = QToolButton()
        self.btn_Betting.setText("BETTING")
        self.btn_Betting.setEnabled(False)


        # self.start_btn.clicked.connect()

        self.btn_Die = QToolButton()
        self.btn_Die.setText("DIE")
        self.btn_Die.setEnabled(False)

        # self.btn_Die.clicked.connect()
        betLayout.addWidget(self.btn_Betting, 0, 0)
        betLayout.addWidget(self.btn_Die, 1, 0)
        left_Layout.addLayout(betLayout, 2, 2)

        self.btn_Save = QToolButton()
        self.btn_Save.setText("SAVE")
        self.btn_Save.clicked.connect(self.save)

        self.btn_Login = QToolButton()
        self.btn_Login.setText("Login")
        self.btn_Login.clicked.connect(self.start_game)

        self.btn_Ranking = QToolButton()
        self.btn_Ranking.setText("Rank")
        self.btn_Ranking.clicked.connect(self.ranking)

        self.logBox = QTextEdit()
        self.logBox.setReadOnly(True)
        self.lblog = QLabel("--log--")
        self.lblog.setAlignment(Qt.AlignCenter)
        right_layout = QGridLayout()

        right_layout.addWidget(self.name_edit, 0, 0)
        right_layout.addWidget(self.btn_Save, 0, 2)
        right_layout.addWidget(self.btn_Login, 0, 1)
        right_layout.addWidget(self.btn_Ranking, 0, 3)
        right_layout.addWidget(self.lblog,1,0,1,4)
        right_layout.addWidget(self.logBox, 2, 0, 3, 4)
        # Layout placement
        mainLayout = QGridLayout()
        self.setWindowTitle("Sutda")
        # mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(left_Layout, 0, 0)
        mainLayout.addLayout(right_layout, 0, 1)
        self.setLayout(mainLayout)
        self.btn_Die.clicked.connect(self.dieClicked)
        self.btn_Betting.clicked.connect(self.bettingClicked)

        self.start_game()

    def Get_card(self):

        self.user_pae1.setPixmap(self.default)
        self.user_pae2.setPixmap(self.default)
        time.sleep(0.5)
        self.computer_pae1.setPixmap(self.default)
        self.computer_pae2.setPixmap(self.default)
        self.userResult.clear()
        self.cpuResult.clear()

        self.get_paeButton.setEnabled(False)
        self.btn_Betting.setEnabled(True)
        self.btn_Die.setEnabled(True)
        self.cardMap = getCard()
        upae1 = QPixmap(cards[self.cardMap["player"][0]]['img'])
        upae2 = QPixmap(cards[self.cardMap["player"][1]]['img'])
        self.user_pae1.setPixmap(upae1)
        self.user_pae2.setPixmap(upae2)
        self.uR = self.sutda.checkDeck(self.cardMap["player"])
        self.cR = self.sutda.checkDeck(self.cardMap["cpu"])
        self.userResult.setText(self.uR)



    def dieClicked(self):
        now = datetime.datetime.now()
        nowtime = now.strftime('[%H:%M:%S]')
        self.log = nowtime + "다이!    내 패: " + self.uR +"\n              잃은 금액:" + str(
            int(self.lefted_money * 0.1)) + "원\n" + self.log
        self.lefted_money = int(self.lefted_money - self.lefted_money * 0.1)
        if self.lefted_money < 100000:
            self.lefted_money += 300000
            self.log = nowtime + "보유 금액이 10만원 미만이 되어 지원금\n              30만원을 지급합니다! " + "\n              얻은 금액: 300000원" + "\n" + self.log
        self.left_money.setText(str(self.lefted_money) + '원')
        self.logBox.setText(self.log)
        self.btn_Die.setEnabled(False)
        self.btn_Betting.setEnabled(False)
        self.get_paeButton.setEnabled(True)

    def bettingClicked(self):
        now = datetime.datetime.now()
        nowtime = now.strftime('[%H:%M:%S]')
        cpae1 = QPixmap(cards[self.cardMap["cpu"][0]]['img'])
        cpae2 = QPixmap(cards[self.cardMap["cpu"][1]]['img'])
        self.computer_pae1.setPixmap(cpae1)
        self.computer_pae2.setPixmap(cpae2)

        result = self.sutda.checkWin([self.cR, self.uR])
        self.cpuResult.setText(self.cR)
        time.sleep(0.5)
        if result == 'win':
            self.log = nowtime + "승리!    내 패: " + self.uR + ", 상대 패: " + self.cR + "\n              얻은 금액:" + str(int(self.lefted_money * 0.2)) + "원\n" + self.log
            self.lefted_money += int(self.lefted_money * 0.2)
        elif result == 'draw':
            self.log = nowtime + "재경기! 내 패: " + self.uR + ", 상대 패: " + self.cR + "\n" + self.log
        elif result == 'lose':
            self.log = nowtime + "패배!    내 패: " + self.uR + ", 상대 패: " + self.cR + "\n              잃은 금액:" + str(
                int(self.lefted_money * 0.2)) + "원\n" + self.log
            self.lefted_money -= int(self.lefted_money * 0.2)

        if self.lefted_money < 100000:
            self.lefted_money += 300000
            self.log = nowtime + "보유 금액이 10만원 미만이 되어 지원금\n              30만원을 지급합니다! " + "\n              얻은 금액: 300000원" + "\n" + self.log
        self.left_money.setText(str(self.lefted_money) + "원")
        self.btn_Die.setEnabled(False)
        self.btn_Betting.setEnabled(False)
        self.get_paeButton.setEnabled(True)
        self.logBox.setText(self.log)



    def start_game(self):
        self.name_edit.setReadOnly(True)
        self.sutda = Sutda()

    def save(self):
        f = open('user_info.txt', 'r')
        lines = f.readlines()
        f.close()
        self.count = 0
        for line in lines:
            information = line.rstrip()
            self.user_info.append(information)
        self.user_info.append(self.left_money.text() + " " + self.name_edit.text())
        f = open('user_info.txt', 'w')

        for info in self.user_info:
            f.write(info + "\n")

    def ranking(self):
        rank = Ranking(self)
        rank.show()

        # 타임아웃 이벤트가 발생하면 호출되는 메서드
        # 어떤 타이머에 의해서 호출되었는지 확인


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = SutdaGame()
    game.show()
    sys.exit(app.exec_())

