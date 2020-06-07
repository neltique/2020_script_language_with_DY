class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0
        self.myDeck = []
        self.price = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self):
        sum = 0
        for i in range(self.N):
            if self.cards[i].getValue() == 1:
                sum += 11
            else:
                sum += self.cards[i].getValue()
        return sum

    def getRank(self):
        # 플레이어가 가진 패 순서대로 정렬
        RankName =""
        suitDict = {"Clubs":[],"Spades":[],"Hearts":[],"Diamonds":[]}

        shape = ""

        for i in range(self.N):
                suitDict[self.cards[i].getSuit()].append(self.cards[i].getValue())

        for value in suitDict.values():
            value.sort()

        # 플러쉬 되는 경우
        for key,value in suitDict.items():
            if len(value)>=5:
                if 1 in value and 10 in value and 11 in value and 12 in value and 13 in value:
                    RankName = "Royal\nStraight\nFlush\n"
                    shape = key
                    self.price = 1
                elif 1 in value and 2 in value and 3 in value and 4 in value and 5 in value:
                    RankName = "Back\nStraight\nFlush\n"
                    shape = key
                    self.price = 2
                else:
                    for i in range(2,10):
                        if i in value and i+1 in value and i+2 in value and i+3 in value and i+4 in value:
                            RankName = "\nStraight\nFlush\n"
                            shape = key
                            self.price = 3
                            self.myDeck =[i, i+1, i+2, i+3, i+4]
                            break
                        else:
                            RankName = "\n\nFlush"
                            shape = key
                            self.price = 6
                            self.myDeck = suitDict[key][len(suitDict[key]):len(suitDict[key])-6:-1]

        #플러쉬 안되는 경우
        if RankName == "":
            numDict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: []}
            for i in range(self.N):
                numDict[self.cards[i].getValue()].append(self.cards[i].getSuit())


            pair = 0
            triple = 0
            for key,value in numDict.items():
                if len(value) == 2:
                    pair += 1
                elif len(value) == 3:
                    triple += 1
                elif len(value) == 4:
                    RankName = "\nFour\nCards"
                    self.myDeck = [key]
                    self.price = 4

            if triple > 0 and pair > 0:
                RankName = "\nFull\nHouse"
                self.price = 5

            if len(numDict[1]) > 0 and len(numDict[10]) > 0 and len(numDict[11]) > 0 and len(
                    numDict[12]) > 0 and len(numDict[13]) > 0:
                RankName = "\n\nMountain"
                self.price = 6
            elif len(numDict[1]) > 0 and len(numDict[2]) > 0 and len(numDict[3]) > 0 and len(
                    numDict[4]) > 0 and len(numDict[5]) > 0:
                RankName = "\nBack\nStraight"
                self.price = 7
            else:
                for i in range(2, 10):
                    if len(numDict[i]) > 0 and len(numDict[i + 1]) > 0 and len(numDict[i + 2]) > 0 and len(
                            numDict[i + 3]) and len(numDict[i + 4]):
                        RankName = "\n\nStraight"
                        self.price = 8
                        self.myDeck = [i, i+1, i+2, i+3, i+4]
                        break

            if RankName == "":
                if triple == 0:
                    if pair ==1:
                        RankName = "\nOne\nPair"
                        self.price = 11
                    elif pair > 1:
                        RankName = "\nTwo\npair"
                        self.price = 10
                    else:
                        RankName = "\nNo\npair"
                        self.price = 12
                else:
                    RankName = "\n\nTriple"
                    self.price = 9


            if RankName == "\nNo\npair":
                for i in range(13,0,-1):
                    if len(self.myDeck)<5:
                        if len(numDict[i]) > 0:
                            self.myDeck.append(i)

            elif RankName == "\nOne\nPair" or RankName == "\nTwo\npair":
                for i in range(13,0,-1):
                    if len(self.myDeck)<5:
                        if len(numDict[i]) > 1:
                            self.myDeck.append(i)

            elif RankName == "\n\nTriple":
                for i in range(13,0,-1):
                    if len(self.myDeck)<5:
                        if len(numDict[i])>2:
                            self.myDeck.append(i)

            elif RankName == "\nFour\nCards":
                for i in range(13,0,-1):
                    if len(self.myDeck)<5:
                        if len(numDict[i])>3:
                            self.myDeck.append(i)

            elif RankName == "\nFull\nHouse":
                for i in range(13,0,-1):
                    if len(self.myDeck)<5:
                        if len(numDict[i])>2:
                            self.myDeck.append(i)

                for i in range(13,0,-1):
                    if len(self.myDeck)<5:
                        if len(numDict[i])>1:
                            self.myDeck.append(i)





        print (self.myDeck)
        return RankName

    def getMyDeck(self):
        for i in self.myDeck:
            if i == 1:
                i=14
        return self.myDeck

    def getPrice(self):
        return self.price