from abc import ABCMeta, abstractmethod
import random

class User(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self):
        self.hp = 10
        self.diceDeck = 15
        self.shields = 0

    @abstractmethod
    def throw(self):
        pass

class Dealer(User):
    def __init__(self):
        super().__init__()
    
    def throw(self):
        if self.diceDeck >= 5:
            dealerDice.diceResult(5)
        else:
            dealerDice.diceResult(self.diceDeck)

class Player(User):
    def __init__(self):
        super().__init__()

    def throw(self):
        if self.diceDeck >= 5:
            playerDice.diceResult(5)
        else:
            playerDice.diceResult(self.diceDeck)

class Dice(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self):
        self.dices = ['double', 'double', 'shield', 'skull', 'attack', 'attack']
        self.dicesResult = []

class PlayerDice(Dice):
    def __init__(self):
        super().__init__()

    def diceResult(self, diceNumber):
        for _ in range(diceNumber):
            self.dicesResult.append(random.choice(self.dices))
        playerDice.double(self.dicesResult.count('double'))
        playerDice.shield(self.dicesResult.count('shield'))
        playerDice.skull(self.dicesResult.count('skull'))
        playerDice.attack(self.dicesResult.count('attack'))
        if player.diceDeck >= 5:
            player.diceDeck -= 5
        else:
            player.diceDeck = self.dicesResult.count('double')

    
    def skull(self, skullNumber):
        if player.shields - skullNumber < 0:
            player.hp += player.shields - skullNumber 
            player.shields = 0
        else:
            player.shields -= skullNumber  
    
    def double(self, doubleNumber):
        if doubleNumber == 0: return
        player.diceDeck += doubleNumber
    
    def shield(self, shieldNumber):
        player.shields += shieldNumber
        if player.shields > 6:
            player.shields = 6
            
    def attack(self, attackNumber):
        if dealer.shields - attackNumber < 0:
            dealer.hp += dealer.shields - attackNumber 
            dealer.shields = 0
        else:
            dealer.shields -= attackNumber  
        
class DealerDice(Dice):
    def __init__(self):
        super().__init__()

    def diceResult(self, diceNumber):
        for _ in range(diceNumber):
            self.dicesResult.append(random.choice(self.dices))
        
        dealerDice.double(self.dicesResult.count('double'))
        dealerDice.shield(self.dicesResult.count('shield'))
        dealerDice.skull(self.dicesResult.count('skull'))
        dealerDice.attack(self.dicesResult.count('attack'))

        if dealer.diceDeck >= 5:
            dealer.diceDeck -= 5
        else:
            dealer.diceDeck = self.dicesResult.count('double')

    def skull(self, skullNumber):
        if skullNumber == 0: return
        if dealer.shields - skullNumber < 0:
            dealer.hp += dealer.shields - skullNumber 
            dealer.shields = 0
        else:
            dealer.shields -= skullNumber  
    
    def double(self, doubleNumber):
        if doubleNumber == 0: return
        dealer.diceDeck += doubleNumber

    
    def shield(self, shieldNumber):
        if shieldNumber == 0: return
        dealer.shields += shieldNumber
        if dealer.shields > 6:
            dealer.shields = 6
            
    def attack(self, attackNumber):
        if attackNumber == 0: return
        if player.shields - attackNumber < 0:
            player.hp += player.shields - attackNumber 
            player.shields = 0
        else:
            player.shields -= attackNumber  

class Table:
    game = True

    def playerTurn(self):
        print('\n------------플레이어턴------------')
        if player.diceDeck <= 0: 
            print('카드가 없으므로 턴을넘김니다') 
            return
        userInput = input('던지기\t그만  ')
        if userInput == '던지기':
            player.throw()
            print(f'플레이어주사위 결과{playerDice.dicesResult}')
            print('더블: {0} 쉴드: {1} 공격: {2} 해골: {3}'.format(playerDice.dicesResult.count('double'), playerDice.dicesResult.count('shield'), playerDice.dicesResult.count('attack'), playerDice.dicesResult.count('skull')))
            print('--------------플레이어정보-------------')
            print(f'플레이어체력{player.hp}\t플레이어쉴드{player.shields}\t플레이어주사위개수{player.diceDeck}')
            print('----------------딜러정보---------------')
            print(f'딜러체력{dealer.hp}\t딜러쉴드{dealer.shields}\t딜러주사위개수{dealer.diceDeck}')    
            playerDice.dicesResult = []
        elif userInput == '그만':
            return
        else:
            print('던지기\t그만 둘중 하나만 입력하세요!')
            return diceTable.playerTurn()
        
    def dealerTurn(self):
        print('\n-------------딜러턴----------------')
        if dealer.diceDeck <= 0: 
            print('카드가 없으므로 턴을넘김니다') 
            return
        userInput = input('던지기\t그만  ')
        if userInput == '던지기':
            dealer.throw()
            print(f'딜러주사위 결과{dealerDice.dicesResult}')
            print('더블: {0} 쉴드: {1} 공격: {2} 해골: {3}'.format(dealerDice.dicesResult.count('double'), dealerDice.dicesResult.count('shield'), dealerDice.dicesResult.count('attack'), dealerDice.dicesResult.count('skull')))
            print('--------------플레이어정보-------------')
            print(f'플레이어체력{player.hp}\t플레이어쉴드{player.shields}\t플레이어주사위개수{player.diceDeck}')
            print('----------------딜러정보---------------')
            print(f'딜러체력{dealer.hp}\t딜러쉴드{dealer.shields}\t딜러주사위개수{dealer.diceDeck}')
            dealerDice.dicesResult = []
        elif userInput == '그만':
            return
        else:
            print('던지기,  그만 둘중 하나만 입력하세요!')
            return diceTable.dealerTurn()

    @classmethod
    def gameOverCheck(cls):
        if player.hp <= 0 and dealer.hp <= 0:
            print('..........무승무...........')
            cls.game = False
        elif player.diceDeck == 0 and dealer.diceDeck == 0 :
            print('..........무승무...........')
            cls.game = False
        elif player.hp <= 0:
            print('~~~~~~~~~~딜러승~~~~~~~~~')
            cls.game = False
        elif dealer.hp <= 0:
            print('~~~~~~~~~플레이어승~~~~~~~~')
            cls.game = False
                    
player = Player()
dealer = Dealer()
playerDice = PlayerDice()
dealerDice = DealerDice()
diceTable = Table()

betAmount = input('배팅할 금액을 고르세요 350, 700, 1500')
print('---------게임시작----------\n')
while diceTable.game:
    diceTable.playerTurn()
    diceTable.gameOverCheck()
    if diceTable == False:
        break
    diceTable.dealerTurn()
    diceTable.gameOverCheck()

    


