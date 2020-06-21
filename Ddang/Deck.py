from itertools import combinations

DD_name_table = {
    1:"삥",
    2:"이",
    3:"삼",
    4:"사",
    5:"오",
    6:"육",
    7:"칠",
    8:"팔",
    9:"구",
    10:"장"
}
KK_name_table = {
    1:"한",
    2:"두",
    3:"세",
    4:"네",
    5:"다섯",
    6:"여섯",
    7:"일곱",
    8:"여덟",
    9:"아홉",
}

made_name_table = {
    (1,1,8):"콩콩팔(1,1,8)",
    (1,2,7):"삐리칠(1,2,7)",
    (1,3,6):"물삼육(1,3,6)",
    (1,4,5):"빽새오(1,4,5)",
    (1,9,10):"삥구장(1,9,10)",
    (2,2,6):"니니육(2,2,6)",
    (2,3,5):"이삼오(2,3,5)",
    (2,8,10):"이판장(2,8,10)",
    (3,3,4):"심심새(3,3,4)",
    (3,7,10):"삼칠장(3,7,10)",
    (3,8,9):"삼빡구(3,8,9)",
    (4,4,2):"살살이(4,4,2)",
    (4,6,10):"사륙장(4,6,10)",
    (4,7,9):"사칠구(4,7,9)",
    (5,5,10):"꼬꼬장(5,5,10)",
    (5,6,9):"오륙구(5,6,9)",
    (5,7,8):"오리발(5,7,8)",
    (6,6,8):"쭉쭉팔(6,6,8)",
    (6,7,7):"철철육(7,7,6)",
    (4,8,8):"팍팍싸(8,8,4)",
    (2,9,9):"구구리(9,9,2)"
}



class Deck:
    def __init__(self):
        self.cards = []
        self.N = 0
        self.isMade = False
        self.madename = "노 메이드"
        self.rankname = ""
        self.rank = 0
        self.madeList = []
        self.isThree = False

    def inDeck(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.isMade = False
        self.madename = "노 메이드"
        self.rankname = ""
        self.rank = 0
        self.madeList.clear()
        self.isThree = False
        self.cards.clear()


    def deckRank(self):
        threeLists = list(combinations(self.cards,3))
        for threeList in threeLists:
            twoList = set(self.cards) - set(threeList)
            twoList = list(twoList)

            self.checkMade(threeList)

            if self.rank < self.checkRank(twoList)[0] and self.isMade == True:
                self.rank,self.rankname = self.checkRank(twoList)
                self.madename = made_name_table[tuple(sorted([int(i.getValue()) for i in threeList]))]
                self.threeList = threeList
                self.isThree = True

    def getIsThree(self):
        return self.isThree

    def getThree(self):
        return self.threeList

    def getRank(self):
        return self.rank

    def getRankName(self):
        return self.rankname

    def getIsMade(self):
        return self.isMade

    def getDeckName(self):
        return self.madename+" "+self.rankname


    def checkRank(self, lst):
        lst = sorted(lst, key = lambda x: x.getValue())
        if lst[0].getValue() == 3.1 and lst[1].getValue() == 8.1:
            rank = 40
            rankname = DD_name_table[int(lst[0].getValue())] + DD_name_table[int(lst[1].getValue())] + "광땡"
            return rank, rankname

        if lst[0].getValue() == 1.1 and (lst[1].getValue() == 3.1 or lst[1].getValue()==8.1):
            rank = 30
            rankname = "일"+DD_name_table[int(lst[1].getValue())] + "광땡"
            return rank, rankname

        if int(lst[0].getValue())==int(lst[1].getValue()):
            rank = 20 + int(lst[0].getValue())-1
            rankname = DD_name_table[int(lst[0].getValue())] + "땡"
            return rank, rankname
        else:
            if int(lst[0].getValue())+int(lst[1].getValue())==10:
                rank = 0
                rankname = "망통"
                return rank, rankname
            else:
                rank = (int(lst[0].getValue()) + int(lst[1].getValue()))%10
                rankname = KK_name_table[((int(lst[0].getValue())+int(lst[1].getValue()))%10)] + " 끗"
                return rank, rankname


    def checkMade(self,lst):
        self.isMade = False

        l = []
        for i in lst:
            l.append(int(i.getValue()))
        l.sort()

        if tuple(l) in made_name_table.keys():
            self.isMade = True
        else:
            self.isMade = False


