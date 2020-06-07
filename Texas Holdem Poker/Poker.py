from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *

import random

class Poker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Texas holdem Poker 이언권 , 백도열")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family = 'Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')

        self.setupButton()
        self.setupLabel()
        self.i=0
        self.pressedDealcount = 0

        self.player = Player("Player")
        self.dealer = Player("dealer")
        self.betMoney = 10
        self.playerMoney = 990
        self.nCardsDealer = 0
        self.nCardsPlayer = 0
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.deckN = 0
        self.window.mainloop()


    def setupButton(self):
        self.Check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2, command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.Bx1 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle2, command=self.pressedBx1)
        self.Bx1.place(x=150, y=500)
        self.Bx2 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle2, command=self.pressedBx2)
        self.Bx2.place(x=250, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2, command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LbetMoney = Label(text="$10", width=4, height=1, font=self.fontstyle, bg="green", fg="gold")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $990", width=15, height=1, font=self.fontstyle, bg="green", fg="gold")
        self.LplayerMoney.place(x=500, y=450)

        self.LplayerPts = Label(text="", width=11, height=3, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerPts.place(x=300, y=325)
        self.LdealerPts = Label(text="", width=11, height=3, font=self.fontstyle, bg="green", fg="cyan")
        self.LdealerPts.place(x=300, y=25)

        self.Lstatus = Label(text="", width=4, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus.place(x=600, y=300)

    def pressedCheck(self):
        self.betMoney += 0
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney -= 0
            self.LplayerMoney.configure(text = "You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav',SND_FILENAME)
        else:
            self.betMoney -= 0
        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'

    def pressedBx1(self):
        self.betMoney += 10*(2**self.i)
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney -= 10*(2**self.i)
            self.LplayerMoney.configure(text = "You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav',SND_FILENAME)

        else:
            self.betMoney -= 0
        self.i += 1
        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'

    def pressedBx2(self):
        self.betMoney += (self.betMoney*2)
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney -=  (self.betMoney*2)
            self.LplayerMoney.configure(text = "You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav',SND_FILENAME)
        else:
            self.betMoney -= 0
        self.i += 1
        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'

    def pressedDeal(self):
        PlaySound('sounds/chip.wav', SND_FILENAME)
        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

        self.deal()

        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

        self.Check['state'] = 'active'
        self.Check['bg'] = 'white'
        self.Bx1['state'] = 'active'
        self.Bx1['bg'] = 'white'
        self.Bx2['state'] = 'active'
        self.Bx2['bg'] = 'white'

    def pressedAgain(self):
        self.setupButton()
        self.deckN = 0

        for i in range(self.player.inHand()):
             self.LcardsPlayer[i].destroy()

        for i in range(self.dealer.inHand()):
             self.LcardsDealer[i].destroy()

        self.player.reset()
        self.dealer.reset()

        self.LcardsPlayer = []
        self.LcardsDealer = []

        self.Lstatus = Label(text="", width=15, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.Lstatus.place(x=500, y=300)

        self.nCardsDealer = 0
        self.nCardsPlayer = 0

    def deal(self):
        if self.pressedDealcount == 0:
            self.player.reset()
            self.dealer.reset()
            self.cardDeck = [i for i in range(52)]

            random.shuffle(self.cardDeck)
            self.deckN = 0

            self.hitPlayer(0)
            self.hitDealer(0)

            self.hitPlayer(1)
            self.hitDealer(1)

            self.nCardsPlayer = 1
            self.nCardsDealer = 0
            self.pressedDealcount += 1
        elif self.pressedDealcount == 1:
            self.centerCard(0)
            self.centerCard(1)
            self.centerCard(2)
            self.pressedDealcount += 1
        elif self.pressedDealcount == 2:
            self.centerCard(3)
            self.pressedDealcount += 1
        elif self.pressedDealcount == 3:
            self.centerCard(4)
            self.pressedDealcount += 1
        elif self.pressedDealcount == 4:
            self.checkWinner()

    def centerCard(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        self.dealer.addCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.LcardsPlayer.append(Label(self.window, image=p))
        self.LcardsDealer.append(Label(self.window, image=p))
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=250 + n * 75, y=200)
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=250 + n * 75, y=200)

    def hitPlayer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.LcardsPlayer.append(Label(self.window,image=p))


        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=50 + n * 75, y=350)
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealer(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))

        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=50 + n * 75, y=30)
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def checkWinner(self):
        p = PhotoImage(file="cards/" + self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image=p)
        self.LcardsDealer[0].image=p

        self.LplayerPts.configure(text= self.player.getRank())
        self.LdealerPts.configure(text = self.dealer.getRank())


        if self.player.getPrice() < self.dealer.getPrice():
            self.Lstatus.configure(text="Win")
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)
        elif self.player.getPrice()>self.dealer.getPrice():
            self.Lstatus.configure(text="LOSE")
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        else:
            deckP = self.player.getMyDeck()
            deckD = self.player.getMyDeck()
            for i in range(7):
                if deckP[i]>deckD[i]:
                    self.Lstatus.configure(text="Win")
                    self.playerMoney += self.betMoney * 2
                    PlaySound('sounds/win.wav', SND_FILENAME)
                elif deckP[i]<deckD[i]:
                    self.Lstatus.configure(text="LOSE")
                    PlaySound('sounds/wrong.wav', SND_FILENAME)
                else:
                    #if self.player.value()> self.dealer.value():
                    #    self.Lstatus.configure(text="Win")
                    #    self.playerMoney += self.betMoney * 2
                    #    PlaySound('sounds/win.wav', SND_FILENAME)
                    #elif self.dealer.value()>self.player.value():
                    #    self.Lstatus.configure(text="LOSE")
                    #    PlaySound('sounds/wrong.wav', SND_FILENAME)
                    #else:
                    self.Lstatus.configure(text="PUSH")


        self.betMoney = 0
        self.LplayerMoney.configure(text = "You have $"+str(self.playerMoney))
        self.LbetMoney.configure(text="$"+str(self.betMoney))

        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'


Poker()

