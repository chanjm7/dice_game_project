from abc import ABCMeta, abstractmethod
import random
from typing import overload

# betAmount = input('배팅할 금액을 고르세요 350, 700, 1500')

class user(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self):
        self.hp = 10
        self.diceDeck = 15
        self.shields = 0

    @abstractmethod
    def throw(self):
        pass


class Dealer(user):
    def __init__(self):
        super().__init__()
    
    def throw(self):
        if self.diceDeck >= 5:
            dealerDice.diceResult(5)
            self.diceDeck -= 5
        else:
            dealerDice.diceResult(self.diceDeck)
            self.diceDeck = 0
        print('던짐')
    
    

class Player(user):
    def __init__(self):
        super().__init__()

    def stop():
        pass

    def throw(self):
        if self.diceDeck >= 5:
            playerDice.diceResult(5)
            self.diceDeck -= 5
        else:
            playerDice.diceResult(self.diceDeck)
            self.diceDeck = 0
        print('던짐')

class Dice(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self):
        self.dices = ['double', 'double', 'shield', 'skull', 'attack', 'attack']
        self.dicesResult = []

    @abstractmethod
    def diceResult(self, diceNumber):
        for _ in range(diceNumber):
            self.dicesResult.append(random.choice(self.dices))
        print(self.dicesResult)
        if 'double' in self.dicesResult:
            print('있음')
            print(self.dicesResult.count('double'))
            # user1Dice.double(self.dicesResult.count('double'))
    
    @abstractmethod
    def skull(self):
        pass
    
    @abstractmethod
    def double(self):
        pass
    
    @abstractmethod
    def shield(self):
        pass
    
    @abstractmethod
    def attack():
        pass

class PlayerDice(Dice):
    def __init__(self):
        super().__init__()

class DealerDice(Dice):
    def __init__(self):
        super().__init__()
        


player = Player()
dealer = Dealer()
playerDice = PlayerDice()
dealerDice = DealerDice()

game = True
print('게임시작')
while game:
    # userInput = input('던지기     그만  ')
    player.throw()
    dealer.throw()

    break


