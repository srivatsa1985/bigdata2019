
import random
from random import randint
from time import sleep
whoStarts=0
card = []
card.append(["superman",100,200,300,400])
card.append(["batman",108,400,305,100])
card.append(["antman",150,200,250,300])
card.append(["spiderman",220,350,230,220])
card.append(["Aquaman",100,120,210,80])
card.append(["GhostRider",400,200,500,450]) 
card.append(["HellBoy",450,250,100,300])
card.append(["Hulk",500,150,100,500])


class Cards:
    def __init__(self,name,power,jump,defense,attack):
        self.name=name
        self.power=power
        self.jump=jump
        self.defense=defense
        self.attack=attack

class Game:
    def __init__(self,NameOfGame):
        self.name = NameOfGame

class Player:
    def __init__(self,ID,Card):
        self.PlayerID = ID
        self.CardForPlayer = Card

        
class CardGame(Game):

    def __init__(self,NumberOfPlayers):
        self.NumberOfPlayers = NumberOfPlayers
        self.PlayerList = []
        print("NumberOfPlayers ", NumberOfPlayers)
        for Players in range(NumberOfPlayers):
            NewPlayer = Player(Players,[]) #Save Player ID and Card
            self.PlayerList.append(NewPlayer)
        
    def shuffle(self):  
                
        shuffleCards = list(range(len(card))) 
        
        random.shuffle(shuffleCards)
        playerIDInc = 0
        print("shuffleCards ",shuffleCards)
        
        
        playerID = self.NumberOfPlayers
        
        for assignCard in range(len(shuffleCards)):
            #print(assignCard,card[shuffleCards[assignCard]])
            #print(self.PlayerList[playerIDInc%self.NumberOfPlayers].PlayerID,self.PlayerList[playerIDInc%self.NumberOfPlayers].CardForPlayer)
            self.PlayerList[playerIDInc%self.NumberOfPlayers].CardForPlayer.append(card[shuffleCards[assignCard]])
            playerIDInc+=1
           
        for Players in range(self.NumberOfPlayers):
            print("\n Player Id " ,self.PlayerList[Players].PlayerID)
            print("Cards",self.PlayerList[Players].CardForPlayer)
            
        # 
        #print("\n \n len ",len(self.PlayerList[0].CardForPlayer)) 
        #print("\n \n ",self.PlayerList[0].CardForPlayer[0]) 
        #print("\n \n ",self.PlayerList[0].CardForPlayer[0][1]) 
         #   NewPlayer = Player(playerIDInc%playerID,card[assignCard]) #Save Player ID and Card
          # 
           # self.PlayerList.append(NewPlayer)
           # print(NewPlayer.PlayerID)
           # print(NewPlayer.CardForPlayer)

    def roll(self):
        print("\n\nPlayer 1 it's your turn. Type 'r' to roll the dice or 'quit' to forfeit. ")
        userOneInput = input(">>>")
        if userOneInput == "r":
            valueOne = randint(1,6)
            print("Player 1 rolled ", valueOne)
            print(" Player 2 it's your turn. Type 'r' to roll the dice or 'quit' to forfeit. ")
            userTwoInput = input(">>>")
            if userTwoInput == "r":
                valueTwo = randint(1,6)
                print("Player 2 rolled ",  valueTwo)
            if valueOne > valueTwo:
                print("Player 1 wins dice! and Can start the Game")
                whoStarts=0
            else:
                print("Player 2 wins dice! and Can start the Game")
                whoStarts=1
                
    #def godspell(self)
        #If firstPlayerIdx = 1
            #print("Player1 to pick card from deck")
        #elif secondPlayerindx = 2
            #print("Player2 to pick card from deck")
    #def resurrecctspell(self)
        #If firstPlayerIdx = 1
            #print("Player1 to pick card from outdated deck")
        #elif secondPlayerindx = 2
            #print("Player2 to pick card from outdated deck")
            
    def StartGame(self):
        #print("whoStarts",whoStarts)
        firstPlayerIdx=whoStarts
        secondPlayerindx = 1 if whoStarts == 0 else 0
        
        #print("player", firstPlayerIdx,secondPlayerindx)
        numberOfRounds = len(self.PlayerList[whoStarts].CardForPlayer)
        #print(numberOfRounds)
        
        self.playerOneWins = 0
        self.playerTwoWins = 0
        for n in range(numberOfRounds):
            cardValueIdx=0
            print("Type P for Power;J for Jump;D for Defense;A for Attack ")
            userOneInput = input(">>>")
            if userOneInput == "p":
                cardValueIdx=1
            elif userOneInput == "j":
                cardValueIdx=2
            elif userOneInput == "d":
                cardValueIdx=3
            elif userOneInput == "a":
                cardValueIdx=4
            else:
                print("In valid input")
                break
                sleep(2)
            
            #print("cardValueIdx ",cardValueIdx)
            
            firstPlayerVal = self.PlayerList[firstPlayerIdx].CardForPlayer[n][cardValueIdx]
            secondPlayerVal = self.PlayerList[secondPlayerindx].CardForPlayer[n][cardValueIdx]
            
            if firstPlayerVal > secondPlayerVal:
                print("Player 1 wins this round! ")
                self.playerOneWins += 1
            elif firstPlayerVal == secondPlayerVal:
                print("It's a draw! ")
            else:
                print("Player 2 wins this round;")
                self.playerTwoWins += 1
                
    def Results(self):
            print("\n\n playerOneWins",self.playerOneWins)
            print("playerTwoWins",self.playerTwoWins)
            if self.playerOneWins > self.playerTwoWins:
                print(" Final Winner is Player 1")
            elif self.playerOneWins < self.playerTwoWins:
                print(" Final Winner is Player 2") 
            else: 
                print(" It's a draw! ")
            
        
if __name__=="__main__":
    NewGame = CardGame(2)
    NewGame.shuffle()
    NewGame.roll()
    NewGame.StartGame()
    NewGame.Results()

