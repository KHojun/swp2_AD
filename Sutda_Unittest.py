import unittest
import game
from card import getCard
from sutda import Sutda
import data

class test_unittest(unittest.TestCase):
    def getCard_test(self):
        self.card = getCard()
        self.val1 = self.card.get('cpu')
        self.val2 = self.card.get('player')
        self.assertIn(self.val1[0], data.cards.keys())#data 카드는 카드 이름의 집합
        self.assertIn(self.val1[1], data.cards.keys())
        self.assertIn(self.val2[0], data.cards.keys())
        self.assertIn(self.val2[1], data.cards.keys())
    def sutda_test(self):
        s = Sutda()
        self.assertEqual(s.checkWin(['구사', '땡잡이']), 'draw')
        self.assertEqual(s.checkWin(['8끗','갑오']), 'win')
        self.assertEqual(s.checkWin(['땡잡이', '8땡']), 'lose')
        self.assertEqual(s.checkWin(['땡잡이', '장땡']), 'win')


        self.assertEqual(s.checkDeck(['3@','8@']),'38광땡')
        self.assertEqual(s.checkDeck(['1@','4']),'독사')
        self.assertEqual(s.checkDeck(['10','1']),'장삥')



if __name__ == '__main__':
    ts = test_unittest()
    ts.getCard_test()
    ts.sutda_test()
