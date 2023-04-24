from random import randint
import pygame
from ImageModifier import ImageModifier
from GameWindows import gameWindows
class Player:
    def __init__(self, playerName, turnOrder):
        self.playerName = playerName
        self.money = 1500
        self.properties = []
        self.hasGetOutOfJailFree = False
        self.inJail = False
        self.turnsInJail = 0
        self.isBankrupt = False
        self.turnOrder = turnOrder
        self.rolledDoubles = False
        self.consecutiveDoubles = 0
        self.currentSpace = None
        self.spaces = None
        self.p1Img = pygame.image.load('1Num.png').convert()
        self.p1Img = pygame.transform.scale(self.p1Img, (20, 20))
        self.p2Img = pygame.image.load('2Num.png').convert()
        self.p2Img = pygame.transform.scale(self.p2Img, (20, 20))
        self.p3Img = pygame.image.load('3Num.png').convert()
        self.p3Img = pygame.transform.scale(self.p3Img, (20, 20))
        self.p4Img = pygame.image.load('4Num.png').convert()
        self.p4Img = pygame.transform.scale(self.p4Img, (20, 20))
        
    def findSpace(self, spaceName):
        for space in self.spaces:
            if spaceName == space.spaceName:
                print("First: " + space.spaceName)
                return space
    
    def newLocation(self, roll):
        if self.consecutiveDoubles == 3 or ((roll[0] + roll[1]) == 0):
            self.inJail = True
            return "Jail"
        match (roll[0]+roll[1]):
            case 2:
                print(self.currentSpace.move2)
                return self.currentSpace.move2
            case 3:
                print(self.currentSpace.move3)
                return self.currentSpace.move3
            case 4:
                print(self.currentSpace.move4)
                return self.currentSpace.move4
            case 5:
                print(self.currentSpace.move5)
                return self.currentSpace.move5
            case 6:
                print(self.currentSpace.move6)
                return self.currentSpace.move6
            case 7:
                print(self.currentSpace.move7)
                return self.currentSpace.move7
            case 8:
                print(self.currentSpace.move8)
                return self.currentSpace.move8
            case 9:
                print(self.currentSpace.move9)
                return self.currentSpace.move9
            case 10:
                print(self.currentSpace.move10)
                return self.currentSpace.move10
            case 11:
                print(self.currentSpace.move11)
                return self.currentSpace.move11
            case 12:
                print(self.currentSpace.move12)
                return self.currentSpace.move12
            
    def rollDice(self, board):
        imgMod = ImageModifier()
        if ((self.inJail == True) & (self.hasGetOutOfJailFree == True)):
            self.inJail = False
            self.hasGetOutOfJailFree = False
        dice1Roll = randint(1,6)
        board.blit(imgMod.space_modifier("roll" +str(dice1Roll)+ ".jpg", 60, 60, 0), (400, 300))            
        dice2Roll = randint(1,6)
        board.blit(imgMod.space_modifier("roll" +str(dice2Roll)+ ".jpg", 60, 60, 0), (500, 300)) 
        
        
        if dice1Roll == dice2Roll:
            self.rolledDoubles = True
            self.consecutiveDoubles += 1
            self.inJail = False
            self.turnsInJail = 0
        else:
            self.rolledDoubles = False
            self.consecutiveDoubles = 0
        totalRoll = (dice1Roll,dice2Roll)
        if self.inJail:
            self.turnsInJail += 1
            if self.turnsInJail >= 3:
                self.turnsInJail = 0
                self.inJail = False
            else:
                totalRoll = (0,0)
                print("You're still in jail!")
        print(str(totalRoll[0]) + " " + str(totalRoll[1]))
        origPos = self.spaces.index(self.currentSpace)
        self.currentSpace = self.findSpace(self.newLocation(totalRoll))
        newPos = self.spaces.index(self.currentSpace)
        if origPos > newPos:
            self.money += 200
        if self.currentSpace.spaceName == 'Go To Jail':
            self.currentSpace = self.findSpace('Jail')
            self.inJail = True
            self.turnsInJail = 0
        print("Current space is: " + self.currentSpace.spaceName)
        return totalRoll
        
    def getNewBoardPos(self, board, thisPlayer, index, players, drawPiles, activePlayer, roll):
        if thisPlayer.currentSpace.spaceName == "Go":
            self.setPlayerPos(board, index, 880, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Ganondorf":
            self.setPlayerPos(board, index, 790, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "PokeBall1":
            self.setPlayerPos(board, index, 710, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Little Mac":
            self.setPlayerPos(board, index, 630, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Low Tier Tax":
            self.setPlayerPos(board, index, 550, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Marth":
            self.setPlayerPos(board, index, 470, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "King Dedede":
            self.setPlayerPos(board, index, 390, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "AssistTrophy1":
            self.setPlayerPos(board, index, 310, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Kirby":
            self.setPlayerPos(board, index, 230, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Meta Knight":
            self.setPlayerPos(board, index, 150, 900, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Jail" or thisPlayer.currentSpace.spaceName == "Go To Jail":
            if thisPlayer.inJail == False:
                self.setPlayerPos(board, index, 10, 880, thisPlayer, activePlayer, drawPiles, players, roll)
            else:
                self.setPlayerPos(board, index, 50, 880, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Jigglypuff":
            self.setPlayerPos(board, index, 40, 800, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Pac Man":
            self.setPlayerPos(board, index, 40, 720, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Mewtwo":
            self.setPlayerPos(board, index, 40, 640, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Incineroar":
            self.setPlayerPos(board, index, 40, 560, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Ike":
            self.setPlayerPos(board, index, 40, 480, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Young Link":
            self.setPlayerPos(board, index, 40, 400, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "PokeBall2":
            self.setPlayerPos(board, index, 40, 320, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Toon Link":
            self.setPlayerPos(board, index, 40, 240, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Link":
            self.setPlayerPos(board, index, 40, 160, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Free Parking":
            self.setPlayerPos(board, index, 40, 70, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Falco":
            self.setPlayerPos(board, index, 160, 60, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "AssistTrophy2":
            self.setPlayerPos(board, index, 240, 60, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Wolf":
            self.setPlayerPos(board, index, 320, 60, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Fox":
            self.setPlayerPos(board, index, 400, 60, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Roy":
            self.setPlayerPos(board, index, 480, 60, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Samus":
            self.setPlayerPos(board, index, 560, 60, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Dark Samus":
            self.setPlayerPos(board, index, 640, 60, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Mr Game & Watch":
            self.setPlayerPos(board, index, 720, 60, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Zero Suit Samus":
            self.setPlayerPos(board, index, 800, 60, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Ryu":
            self.setPlayerPos(board, index, 900, 150, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Terry":
            self.setPlayerPos(board, index, 900, 230, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "PokeBall3":
            self.setPlayerPos(board, index, 900, 310, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Kazuya":
            self.setPlayerPos(board, index, 900, 390, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Byleth":
            self.setPlayerPos(board, index, 900, 470, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "AssistTrophy3":
            self.setPlayerPos(board, index, 900, 550, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Pyra":
            self.setPlayerPos(board, index, 900, 630, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "DLC Tax":
            self.setPlayerPos(board, index, 900, 710, thisPlayer, activePlayer, drawPiles, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Mythra":
            self.setPlayerPos(board, index, 900, 790, thisPlayer, activePlayer, drawPiles, players, roll)
    def calcNetWorth(self):
        total = 0
        total += self.money
        for property in self.properties:
            if property.isMortgaged:
                total += property.mortgageValue
            else:
                total += property.buyCost
            total += (property.numHouses * property.houseCost)
        return total
    
    def calcNumUtils(self):
        total = 0
        for property in self.properties:
            if ((property.spaceName == "Mr Game & Watch") or (property.spaceName == "Pac Man")):
                total += 1
        return total
    
    def calcNumFEs(self):
        total = 0
        for property in self.properties:
            if ((property.spaceName == "Marth") or (property.spaceName == "Ike") or (property.spaceName == "Roy") or (property.spaceName == "Byleth")):
                total += 1
        return total
    def setPlayerPos(self, board, index, xCoord, yCoord, thisPlayer, activePlayer, drawPiles, players, roll):
        gw = gameWindows(board)
        imgMod = ImageModifier()
        smallFont = pygame.font.SysFont(None, 16)
        if ((self.inJail == False) & (self.currentSpace.spaceName == "Jail" or self.currentSpace.spaceName == "Go To Jail")):
            if index == 0:
                board.blit(self.p1Img, (xCoord, yCoord))
            elif index == 1:
                board.blit(self.p2Img, (xCoord, yCoord+20))
            elif index == 2:
                board.blit(self.p3Img, (xCoord, yCoord+40))
            else:
                board.blit(self.p4Img, (xCoord, yCoord+60))
        else:           
            if index == 0:
                board.blit(self.p1Img, (xCoord, yCoord))
            elif index == 1:
                board.blit(self.p2Img, (xCoord, yCoord+30))
            elif index == 2:
                board.blit(self.p3Img, (xCoord+30, yCoord))
            else:
                board.blit(self.p4Img, (xCoord+30, yCoord+30))
        if ((thisPlayer == activePlayer) & (roll != (0,0))) :
            roll1 = "roll" +str(roll[0])+ ".jpg"
            roll2 = "roll" +str(roll[1])+ ".jpg"
            BLACK = (0,0,0)
            if (thisPlayer.currentSpace.spaceName in ["AssistTrophy1", "AssistTrophy2", "AssistTrophy3"]):
                drawPiles.drawAssistTrophy(thisPlayer, players, roll)
            elif (thisPlayer.currentSpace.spaceName in ["PokeBall1", "PokeBall2", "PokeBall3"]):
                drawPiles.drawPokeBall(thisPlayer, players, roll)
            elif (thisPlayer.currentSpace.spaceName in ["Free Parking", "Jail", "Go to Jail", "Go"]):
                if thisPlayer.currentSpace.spaceName == "Free Parking":
                    messageText = smallFont.render(activePlayer.playerName + " landed on Free Parking.", True, BLACK)
                elif thisPlayer.currentSpace.spaceName == "Jail":
                    messageText = smallFont.render(activePlayer.playerName + " is in jail!", True, BLACK)
                elif thisPlayer.currentSpace.spaceName == "Go To Jail":
                    messageText = smallFont.render(activePlayer.playerName + " went to jail!", True, BLACK)
                else:
                    messageText = smallFont.render(activePlayer.playerName + " landed on Go!", True, BLACK)
                gw.createBoard(smallFont, players, drawPiles, None)
                if roll != (0,0):
                    board.blit(imgMod.space_modifier(roll1, 60, 60, 0), (400, 300))            
                    board.blit(imgMod.space_modifier(roll2, 60, 60, 0), (500, 300)) 
                textRect = messageText.get_rect()
                textRect.center = (350, 750)
                board.blit(messageText, textRect)
                pygame.display.update() 
            elif (thisPlayer.currentSpace.spaceName == "DLC Tax"):
                thisPlayer.money -= 100
                gw.createBoard(smallFont, players, drawPiles, None)
                board.blit(imgMod.space_modifier(roll1, 60, 60, 0), (400, 300))            
                board.blit(imgMod.space_modifier(roll2, 60, 60, 0), (500, 300))
                messageText = smallFont.render(activePlayer.playerName + " paid the DLC Tax!", True, BLACK)
                textRect = messageText.get_rect()
                textRect.center = (350, 750)
                board.blit(messageText, textRect)
                pygame.display.update() 
            elif (thisPlayer.currentSpace.spaceName == "Low Tier Tax"):
                thisPlayer.money -= 200
                gw.createBoard(smallFont, players, drawPiles, None)
                board.blit(imgMod.space_modifier(roll1, 60, 60, 0), (400, 300))            
                board.blit(imgMod.space_modifier(roll2, 60, 60, 0), (500, 300))
                messageText = smallFont.render(activePlayer.playerName + " paid the Low Tier Tax!", True, BLACK)
                textRect = messageText.get_rect()
                textRect.center = (350, 750)
                board.blit(messageText, textRect)
                pygame.display.update() 
            else:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll, players, drawPiles)