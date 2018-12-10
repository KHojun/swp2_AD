import random
cards = {
    # 동물그림 = '&' 광 = '@'
    "1":{"month" : 1, "spc" : None, "img" : "IMG/1.png"},
    "1@":{"month" : 1, "spc" : "@", "img" : "IMG/1@.png"},
    "2":{"month" : 2, "spc" : None, "img" : "IMG/2.png"},
    "2&":{"month" : 2, "spc" : "&", "img" : "IMG/2&.png"},
    "3":{"month" : 3, "spc" : None, "img" : "IMG/3.png"},
    "3@":{"month" : 3, "spc" : "@", "img" : "IMG/3@.png"},
    "4&":{"month" : 4, "spc" : "&", "img" : "IMG/4&.png"},
    "4":{"month" : 4, "spc" : None, "img" : "IMG/4.png"},
    "5":{"month" : 5, "spc" : None, "img" : "IMG/5.png"},
    "5_":{"month" : 5, "spc" : None, "img" : "IMG/5_.png"},
    "6":{"month" : 6, "spc" : None, "img" : "IMG/6.png"},
    "6_":{"month" : 6, "spc" : None, "img" : "IMG/6_.png"},
    "7":{"month" : 7, "spc" : None, "img" : "IMG/7.png"},
    "7&":{"month" : 7, "spc" : "&", "img" : "IMG/7&.png"},
    "8":{"month" : 8, "spc" : None, "img" : "IMG/8.png"},
    "8@":{"month" : 8, "spc" : "@", "img" : "IMG/8@.png"},
    "9":{"month" : 9, "spc" : None, "img" : "IMG/9.png"},
    "9&":{"month" : 9, "spc" : "&", "img" : "IMG/9&.png"},
    "10":{"month" : 10, "spc" : None, "img" : "IMG/10.png"},
    "10_":{"month" : 10, "spc" : None, "img" : "IMG/10_.png"}}

def getCard(cpu, player):
    cardlist = random.shuffle(cards.keys())