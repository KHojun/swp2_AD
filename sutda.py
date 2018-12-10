from data import cards, jokbo
import card
class Sutda:
    def __init__(self):
        pass
    def checkDeck(self, cardlist):
        if "3@" in cardlist and "8@" in cardlist:
            return "38광땡"

        elif "1@" in cardlist and "8@" in cardlist:
            return "18광땡"

        elif "3@" in cardlist and "8@" in cardlist:
            return "38광땡"

        elif cards[cardlist[0]]["month"] == cards[cardlist[1]]["month"]:
            if cards[cardlist[0]]["month"] == 10:
                return "장땡"
            else :
                return str(cards[cardlist[0]]["month"]) + "땡"

        elif cards[cardlist[0]]["month"] + cards[cardlist[1]]["month"] == 3:
            return "알리"

        elif ("1@" in cardlist or "1" in cardlist) and ("4" in cardlist or "4&" in cardlist):
            return "독사"

        elif ("9" in cardlist or "9&" in cardlist) and ("1" in cardlist or "1@" in cardlist):
            return "구삥"

        elif ("10" in cardlist or "10_" in cardlist) and ("1" in cardlist or "1@" in cardlist):
            return "장삥"

        elif ("10" in cardlist or "10_" in cardlist) and ("4" in cardlist or "4&" in cardlist):
            return "장사"

        elif ("6" in cardlist or  "6_" in cardlist) and ("4" in cardlist or "4&" in cardlist):
            return "세륙"

        elif "9&" in cardlist and "4&" in cardlist:
            return "멍텅구리 구사"

        elif ("9" in cardlist or "9&" in cardlist) and ("4" in cardlist or "4&" in cardlist):
            return "구사"

        elif "3@" in cardlist and "7&" in cardlist:
            return "땡잡이"

        else:
            tmp = (cards[cardlist[0]]['month'] + cards[cardlist[1]]['month']) % 10
            if tmp == 9:
                return "갑오"
            elif tmp == 0:
                return "망통"
            else:
                return str(tmp) + "끗"

    def checkWin(self, Result):
        if "땡잡이" in Result:
            tmp = Result.index("땡잡이")
            if tmp == 0:
                if 4 <= jokbo[Result[1]] <= 12:
                    return "lose"
            elif tmp == 1:
                if 4 <= jokbo[Result[0]] <= 12:
                    return "win"

        if "멍텅구리 구사" in Result:
            tmp = Result.index("멍텅구리 구사")
            if tmp == 0:
                if 3 <= jokbo[Result[1]] <= 28:
                    return "draw"
            elif tmp == 1:
                if 3 <= jokbo[Result[0]] <= 28:
                    return "draw"

        if "구사" in Result:
            tmp = Result.index("구사")
            if tmp == 0:
                if 13 <= jokbo[Result[1]] <= 28:
                    return "draw"
            elif tmp == 1:
                if 13 <= jokbo[Result[0]] <= 28:
                    return "draw"

        if jokbo[Result[0]] > jokbo[Result[1]]:
            return "win"
        elif jokbo[Result[0]] < jokbo[Result[1]]:
            return "lose"
        else:
            return "draw"

if __name__ == "__main__":
    a = card.getCard()
    s = Sutda()
    print(s.checkDeck(a["cpu"]), s.checkDeck(a['player']))
    print(s.checkWin(["땡잡이", "7땡"]))