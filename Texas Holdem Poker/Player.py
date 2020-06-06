class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def getCards(self):
        return self.cards

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
        string =""
        dict = {"Clubs":[],"Spades":[],"Hearts":[],"Diamonds":[]}
        for i in range(self.N):
                dict[self.cards[i].getSuit()].append(self.cards[i].getValue())

        for value in dict.values():
            value.sort()

        # 플러쉬 되는 경우
        for value in dict.values():
            if len(value)>=5:
                if 1 in value and 10 in value and 11 in value and 12 in value and 13 in value:
                    string = "Royal\nStraight\nFlush"
                elif 1 in value and 2 in value and 3 in value and 4 in value and 5 in value:
                    string = "Back\nStraight\nFlush"
                else:
                    for i in range(2,10):
                        if i in value and i+1 in value and i+2 in value and i+3 in value and i+4 in value:
                            string = "\nStraight\nFlush"
                            break
                        else:
                            string = "Flush"

        #플러쉬 안되는 경우
        if string == "":
            dict2 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: []}
            for i in range(self.N):
                dict2[self.cards[i].getValue()].append(self.cards[i].getSuit())


            pair = 0
            triple = 0
            for value in dict2.values():
                if len(value) == 2:
                    pair += 1
                elif len(value) == 3:
                    triple += 1
                elif len(value) == 4:
                    string = "Four Cards"

            if triple > 0 and pair > 0:
                string = "Full House"

            if len(dict2[1]) > 0 and len(dict2[10]) > 0 and len(dict2[11]) > 0 and len(
                    dict2[12]) > 0 and len(dict2[13]) > 0:
                string = "Mountain"
            elif len(dict2[1]) > 0 and len(dict2[2]) > 0 and len(dict2[3]) > 0 and len(
                    dict2[4]) > 0 and len(dict2[5]) > 0:
                string = "Back Straight"
            else:
                for i in range(2, 10):
                    if len(dict2[i]) > 0 and len(dict2[i + 1]) > 0 and len(dict2[i + 2]) > 0 and len(
                            dict2[i + 3]) and len(dict2[i + 4]):
                        string = "Straight"
                        break

            if string == "":
                if triple == 0:
                    if pair ==1:
                        string = "One Pair"
                    elif pair > 1:
                        string = "Two pair"
                    else:
                        string = "No pair"
                else:
                    string = "Triple"

            #print(dict2)

        #print(dict)

        return string