from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Deck import *
import random

class Ddang:
    def __init__(self):
        self.window = Tk()
        self.window.title("Black Jack")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.fontstyle3 = font.Font(self.window, size=14, weight='bold',family='Consolas')
        self.fontstyle4 = font.Font(self.window, size=12, weight='bold', family='Consolas')

        self.players = [Deck(),Deck(),Deck()]
        self.dealer = Deck()

        self.playersBetsMoney = [0,0,0]
        self.playerMoney = 1000

        self.setupButton()
        self.setupLabel()

        self.pressedDealcount = 0
        self.playerWin = False

        self.LcardsPlayers = [[],[],[]]
        self.LcardsPlayersNums = [[],[],[]]
        self.LcardsDealer = []
        self.LcardsDealerNum = []
        self.LcardsPlayersNames = []
        self.LcardsPlayersresult = []

        self.deckN = 0
        self.window.mainloop()


    def setupButton(self):
        self.fB5 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.pressedfB5)
        self.fB5.place(x=40, y=500)
        self.fB1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.pressedfB1)
        self.fB1.place(x=120, y=500)

        self.sB5 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.pressedsB5)
        self.sB5.place(x=240, y=500)
        self.sB1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.pressedsB1)
        self.sB1.place(x=320, y=500)

        self.tB5 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.pressedtB5)
        self.tB5.place(x=440, y=500)
        self.tB1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.pressedtB1)
        self.tB1.place(x=520, y=500)

        self.Deal = Button(self.window, text="Deal", width=5, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=620, y=500)
        self.Again = Button(self.window, text="Again", width=5, height=1, font=self.fontstyle2, command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.fB5['state'] = 'disabled'
        self.fB5['bg'] = 'gray'
        self.fB1['state'] = 'disabled'
        self.fB1['bg'] = 'gray'

        self.sB5['state'] = 'disabled'
        self.sB5['bg'] = 'gray'
        self.sB1['state'] = 'disabled'
        self.sB1['bg'] = 'gray'

        self.tB5['state'] = 'disabled'
        self.tB5['bg'] = 'gray'
        self.tB1['state'] = 'disabled'
        self.tB1['bg'] = 'gray'

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LfbetMoney = Label(text=str(self.playersBetsMoney[0])+"만", width=5, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LfbetMoney.place(x=60, y=450)

        self.LsbetMoney = Label(text=str(self.playersBetsMoney[1]) + "만", width=5, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LsbetMoney.place(x=260, y=450)

        self.LtbetMoney = Label(text=str(self.playersBetsMoney[2]) + "만", width=5, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LtbetMoney.place(x=460, y=450)

        self.LplayerMoney = Label(text=str(self.playerMoney)+"만", width=5, height=1, font=self.fontstyle, bg="green", fg="blue")
        self.LplayerMoney.place(x=650, y=400)



    def pressedfB5(self):
        self.playersBetsMoney[0] += 5
        self.playerMoney -= 5
        PlaySound('sounds/chip.wav',SND_FILENAME)
        self.LfbetMoney.configure(text=str(self.playersBetsMoney[0])+"만")
        self.LplayerMoney.configure(text=str(self.playerMoney)+"만")
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressedfB1(self):
        self.playersBetsMoney[0] += 1
        self.playerMoney -= 1
        PlaySound('sounds/chip.wav', SND_FILENAME)
        self.LfbetMoney.configure(text=str(self.playersBetsMoney[0])+"만")
        self.LplayerMoney.configure(text=str(self.playerMoney)+"만")
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressedsB5(self):
        self.playersBetsMoney[1] += 5
        self.playerMoney -= 5
        PlaySound('sounds/chip.wav', SND_FILENAME)
        self.LsbetMoney.configure(text=str(self.playersBetsMoney[1])+"만")
        self.LplayerMoney.configure(text=str(self.playerMoney)+"만")
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressedsB1(self):
        self.playersBetsMoney[1] += 1
        self.playerMoney -= 1
        PlaySound('sounds/chip.wav', SND_FILENAME)
        self.LsbetMoney.configure(text=str(self.playersBetsMoney[1]) + "만")
        self.LplayerMoney.configure(text=str(self.playerMoney) + "만")
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressedtB5(self):
        self.playersBetsMoney[2] += 5
        self.playerMoney -= 5
        PlaySound('sounds/chip.wav', SND_FILENAME)
        self.LtbetMoney.configure(text=str(self.playersBetsMoney[2]) + "만")
        self.LplayerMoney.configure(text=str(self.playerMoney) + "만")
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressedtB1(self):
        self.playersBetsMoney[2] += 1
        self.playerMoney -= 1
        PlaySound('sounds/chip.wav', SND_FILENAME)
        self.LtbetMoney.configure(text=str(self.playersBetsMoney[2]) + "만")
        self.LplayerMoney.configure(text=str(self.playerMoney) + "만")
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressedDeal(self):
        PlaySound('sounds/chip.wav', SND_FILENAME)
        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"
        self.deal()
        self.pressedDealcount +=1


    def pressedAgain(self):
        self.playerWin = False
        self.pressedDealcount = 0
        self.deckN = 0
        #################
        for i in range(3):
            self.players[i].reset()
        self.dealer.reset()

        for i in range(5):
            self.LcardsDealerNum[i].destroy()
            self.LcardsDealer[i].destroy()
            for j in range(3):
                self.LcardsPlayersNums[j][i].destroy()
                self.LcardsPlayers[j][i].destroy()

        for i in range(3):
            self.LcardsPlayersNames[i].destroy()
            self.LcardsPlayersresult[i].destroy()

        self.LcardsDealerName["text"] = ""

        self.LcardsPlayers = [[], [], []]
        self.LcardsPlayersNums = [[], [], []]
        self.LcardsDealer = []
        self.LcardsDealerNum = []
        self.LcardsPlayersNames = []
        self.LcardsPlayersresult = []
        ############
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'
        self.setupLabel()
        PlaySound('sounds/ding.wav', SND_FILENAME)

    def deal(self):
        if self.pressedDealcount == 0:
            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
            for p in self.players:
                p.reset()
            self.dealer.reset()

            self.cardDeck = []
            for i in range(1, 11):
                for j in range(1, 5):
                    string = str(i) + "." + str(j)
                    self.cardDeck.append(float(string))
            random.shuffle(self.cardDeck)
            self.deckN = 0
            self.hit(0)

            self.fB5['state'] = 'active'
            self.fB5['bg'] = 'white'
            self.fB1['state'] = 'active'
            self.fB1['bg'] = 'white'

            self.sB5['state'] = 'active'
            self.sB5['bg'] = 'white'
            self.sB1['state'] = 'active'
            self.sB1['bg'] = 'white'

            self.tB5['state'] = 'active'
            self.tB5['bg'] = 'white'
            self.tB1['state'] = 'active'
            self.tB1['bg'] = 'white'

        elif self.pressedDealcount == 1:
            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
            self.hit(1)
            self.hit(2)
            self.hit(3)
        elif self.pressedDealcount == 2:
            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
            self.hit(4)
        elif self.pressedDealcount == 3:
            self.checkWins()

    def hit(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)

        p = PhotoImage(file = "GodoriCards/cardback.gif")
        self.LcardsDealer.append(Label(self.window,image = p))
        self.LcardsDealer[self.dealer.inDeck() - 1].image = p
        self.LcardsDealer[self.dealer.inDeck() - 1].place(x=240+n*25, y=80)
        self.LcardsDealerNum.append(Label(self.window, width=2,font=self.fontstyle3, bg="green", fg="white"))
        self.LcardsDealerNum[self.dealer.inDeck() - 1].place(x=260+n*25, y=50)
        for i in range(3):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.players[i].addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsPlayers[i].append(Label(self.window, image=p))
            self.LcardsPlayers[i][self.players[i].inDeck() - 1].image = p
            self.LcardsPlayers[i][self.players[i].inDeck() - 1].place(x=40+(i*200) + n*25, y=300)

            self.LcardsPlayersNums[i].append(Label(self.window,width=2, text=str(int(newCard.getValue())),font=self.fontstyle3, bg="green", fg="white"))
            self.LcardsPlayersNums[i][self.players[i].inDeck() - 1].place(x=60+(i*200) + n*25, y=270)


    def checkWins(self):
        for i in range(self.dealer.inDeck()):
            p = PhotoImage(file="GodoriCards/" + self.dealer.cards[i].filename())
            self.LcardsDealer[i].configure(image=p)
            self.LcardsDealer[i].image = p
            self.LcardsDealerNum[i].configure(text=int(self.dealer.cards[i].getValue()))

        self.dealer.deckRank()
        self.LcardsDealerName = Label(self.window, width=20, text=self.dealer.getDeckName(), font=self.fontstyle3, bg="green",fg="cyan")
        self.LcardsDealerName.place(x=210, y=20)

        if self.dealer.getIsThree() == True:
            for j in range(3):
                k = self.dealer.cards.index(self.dealer.getThree()[j])
                self.LcardsDealer[k].place(y=90)
                self.LcardsDealerNum[k].configure(fg="yellow")

        for i in range(3):
            self.players[i].deckRank()
            if self.players[i].getRank() > self.dealer.getRank():
                self.LcardsPlayersresult.append(Label(self.window, text="승",width=1,bg="green", fg="red",font = self.fontstyle))
                self.playerMoney += self.playersBetsMoney[i]*2
                self.playersBetsMoney[i] = 0
            else:
                self.LcardsPlayersresult.append(Label(self.window, text="패",width=1,bg="green", fg="red",font = self.fontstyle))
                self.playersBetsMoney[i] = 0


            self.LcardsPlayersresult[i].place(x=100 + (i * 200), y=200)
            self.LcardsPlayersNames.append(Label(self.window, width=20, text=self.players[i].getDeckName(), font=self.fontstyle4, bg="green", fg="cyan"))
            self.LcardsPlayersNames[i].place(x=30 + (i * 200), y=240)

        for i in range(3):
            if self.players[i].getIsThree() == True:
                for j in range(3):
                    k = self.players[i].cards.index(self.players[i].getThree()[j])
                    self.LcardsPlayers[i][k].place(y=310)
                    self.LcardsPlayersNums[i][k].configure(fg = "yellow")

        for i in range(3):
            if self.players[i].getRank() > self.dealer.getRank():
                self.playerWin = True



        self.LfbetMoney.configure(text=str(self.playersBetsMoney[0]) + "만")

        self.LsbetMoney.configure(text=str(self.playersBetsMoney[1]) + "만")

        self.LtbetMoney.configure(text=str(self.playersBetsMoney[2]) + "만")

        self.LplayerMoney.configure(text = str(self.playerMoney)+"만")

        self.fB5['state'] = 'disabled'
        self.fB5['bg'] = 'gray'
        self.fB1['state'] = 'disabled'
        self.fB1['bg'] = 'gray'
        self.sB5['state'] = 'disabled'
        self.sB5['bg'] = 'gray'
        self.sB1['state'] = 'disabled'
        self.sB1['bg'] = 'gray'
        self.tB5['state'] = 'disabled'
        self.tB5['bg'] = 'gray'
        self.tB1['state'] = 'disabled'
        self.tB1['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'
        if self.playerWin == True:
            PlaySound('sounds/win.wav', SND_FILENAME)
        else:
            PlaySound('sounds/wrong.wav', SND_FILENAME)

Ddang()
