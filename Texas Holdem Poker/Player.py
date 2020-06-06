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

    def value(self):
        sum = 0
        for i in range(self.N):
            if self.cards[i].getValue() == 1:
                sum += 11
                if sum > 21:
                    sum -= 10
            else:
                sum += self.cards[i].getValue()

        return sum

    def show(self):
        for i in range(self.N):
            print(self.cards[i].getValue())


