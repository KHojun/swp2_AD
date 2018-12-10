import random
from data import cards

def getCard():
    cardlist = list(cards.keys())
    random.shuffle(cardlist)
    return {'cpu' : [cardlist[0], cardlist[1]],
            'player' : [cardlist[2], cardlist[3]]}
