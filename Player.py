from MovementFile import movementLocation
from random import randint
import pygame
from ImageModifier import ImageModifier
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
        self.currentSpace = movementLocation().spaces[0]
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
        if self.consecutiveDoubles == 3 or roll == 0:
            self.inJail = True
            return "Jail"
        match roll:
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
        totalRoll = dice1Roll + dice2Roll
        if self.inJail:
            self.turnsInJail += 1
            if self.turnsInJail >= 3:
                self.turnsInJail = 0
                self.inJail = False
            else:
                totalRoll = 0
                print("You're still in jail!")
        self.currentSpace = self.findSpace(self.newLocation(totalRoll))
        if self.currentSpace.spaceName == 'Go To Jail':
            self.currentSpace = self.findSpace('Jail')
            self.inJail = True
            self.turnsInJail = 0
        print("Current space is: " + self.currentSpace.spaceName)
        return totalRoll
        
    def getNewBoardPos(self, board, thisPlayer, index, players, drawPiles, activePlayer, roll):
        if thisPlayer.currentSpace.spaceName == "Go":
            if index == 0:
                board.blit(self.p1Img, (880, 900))
            elif index == 1:
                board.blit(self.p2Img, (920, 900))
            elif index == 2:
                board.blit(self.p3Img, (880, 940))
            else:
                board.blit(self.p4Img, (920, 940))
        elif thisPlayer.currentSpace.spaceName == "Ganondorf":
            if index == 0:
                board.blit(self.p1Img, (790, 900))
            elif index == 1:
                board.blit(self.p2Img, (830, 900))
            elif index == 2:
                board.blit(self.p3Img, (790, 940))
            else:
                board.blit(self.p4Img, (830, 940))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "PokeBall1":
            if index == 0:
                board.blit(self.p1Img, (710, 900))
            elif index == 1:
                board.blit(self.p2Img, (750, 900))
            elif index == 2:
                board.blit(self.p3Img, (710, 940))
            else:
                board.blit(self.p4Img, (750, 940))
            if thisPlayer == activePlayer:
                drawPiles.drawPokeBall(thisPlayer, players)
        elif thisPlayer.currentSpace.spaceName == "Little Mac":
            if index == 0:
                board.blit(self.p1Img, (630, 900))
            elif index == 1:
                board.blit(self.p2Img, (670, 900))
            elif index == 2:
                board.blit(self.p3Img, (630, 940))
            else:
                board.blit(self.p4Img, (670, 940))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Low Tier Tax":
            if index == 0:
                board.blit(self.p1Img, (550, 900))
            elif index == 1:
                board.blit(self.p2Img, (590, 900))
            elif index == 2:
                board.blit(self.p3Img, (550, 940))
            else:
                board.blit(self.p4Img, (590, 940))
            if thisPlayer == activePlayer:
                thisPlayer.money -= 200
        elif thisPlayer.currentSpace.spaceName == "Marth":
            if index == 0:
                board.blit(self.p1Img, (470, 900))
            elif index == 1:
                board.blit(self.p2Img, (510, 900))
            elif index == 2:
                board.blit(self.p3Img, (470, 940))
            else:
                board.blit(self.p4Img, (510, 940))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "King Dedede":
            if index == 0:
                board.blit(self.p1Img, (390, 900))
            elif index == 1:
                board.blit(self.p2Img, (430, 900))
            elif index == 2:
                board.blit(self.p3Img, (390, 940))
            else:
                board.blit(self.p4Img, (430, 940))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "AssistTrophy1":
            if index == 0:
                board.blit(self.p1Img, (310, 900))
            elif index == 1:
                board.blit(self.p2Img, (350, 900))
            elif index == 2:
                board.blit(self.p3Img, (310, 940))
            else:
                board.blit(self.p4Img, (350, 940))
            if thisPlayer == activePlayer:
                drawPiles.drawAssistTrophy(thisPlayer, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Kirby":
            if index == 0:
                board.blit(self.p1Img, (230, 900))
            elif index == 1:
                board.blit(self.p2Img, (270, 900))
            elif index == 2:
                board.blit(self.p3Img, (230, 940))
            else:
                board.blit(self.p4Img, (270, 940))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Meta Knight":
            if index == 0:
                board.blit(self.p1Img, (150, 900))
            elif index == 1:
                board.blit(self.p2Img, (190, 900))
            elif index == 2:
                board.blit(self.p3Img, (150, 940))
            else:
                board.blit(self.p4Img, (190, 940))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Jail" or thisPlayer.currentSpace.spaceName == "Go To Jail":
            if thisPlayer.inJail == False:
                if index == 0:
                    board.blit(self.p1Img, (10, 880))
                elif index == 1:
                    board.blit(self.p2Img, (10, 910))
                elif index == 2:
                    board.blit(self.p3Img, (10, 940))
                else:
                    board.blit(self.p4Img, (10, 970))
            else:
                if index == 0:
                    board.blit(self.p1Img, (50, 880))
                elif index == 1:
                    board.blit(self.p2Img, (80, 880))
                elif index == 2:
                    board.blit(self.p3Img, (50, 910))
                else:
                    board.blit(self.p4Img, (80, 910))
        elif thisPlayer.currentSpace.spaceName == "Jigglypuff":
            if index == 0:
                board.blit(self.p1Img, (40, 800))
            elif index == 1:
                board.blit(self.p2Img, (40, 800))
            elif index == 2:
                board.blit(self.p3Img, (70, 830))
            else:
                board.blit(self.p4Img, (70, 830))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Pac Man":
            if index == 0:
                board.blit(self.p1Img, (40, 720))
            elif index == 1:
                board.blit(self.p2Img, (40, 750))
            elif index == 2:
                board.blit(self.p3Img, (70, 720))
            else:
                board.blit(self.p4Img, (70, 750))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Mewtwo":
            if index == 0:
                board.blit(self.p1Img, (40, 640))
            elif index == 1:
                board.blit(self.p2Img, (40, 670))
            elif index == 2:
                board.blit(self.p3Img, (70, 640))
            else:
                board.blit(self.p4Img, (70, 670))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Incineroar":
            if index == 0:
                board.blit(self.p1Img, (40, 560))
            elif index == 1:
                board.blit(self.p2Img, (40, 590))
            elif index == 2:
                board.blit(self.p3Img, (70, 560))
            else:
                board.blit(self.p4Img, (70, 590))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Ike":
            if index == 0:
                board.blit(self.p1Img, (40, 480))
            elif index == 1:
                board.blit(self.p2Img, (40, 510))
            elif index == 2:
                board.blit(self.p3Img, (70, 480))
            else:
                board.blit(self.p4Img, (70, 510))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Young Link":
            if index == 0:
                board.blit(self.p1Img, (40, 400))
            elif index == 1:
                board.blit(self.p2Img, (40, 430))
            elif index == 2:
                board.blit(self.p3Img, (70, 400))
            else:
                board.blit(self.p4Img, (70, 430))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "PokeBall2":
            if index == 0:
                board.blit(self.p1Img, (40, 320))
            elif index == 1:
                board.blit(self.p2Img, (40, 350))
            elif index == 2:
                board.blit(self.p3Img, (70, 320))
            else:
                board.blit(self.p4Img, (70, 350))
            if thisPlayer == activePlayer:
                drawPiles.drawPokeBall(thisPlayer, players)
        elif thisPlayer.currentSpace.spaceName == "Toon Link":
            if index == 0:
                board.blit(self.p1Img, (40, 240))
            elif index == 1:
                board.blit(self.p2Img, (40, 270))
            elif index == 2:
                board.blit(self.p3Img, (70, 240))
            else:
                board.blit(self.p4Img, (70, 270))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Link":
            if index == 0:
                board.blit(self.p1Img, (40, 160))
            elif index == 1:
                board.blit(self.p2Img, (40, 190))
            elif index == 2:
                board.blit(self.p3Img, (70, 160))
            else:
                board.blit(self.p4Img, (70, 190))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Free Parking":
            if index == 0:
                board.blit(self.p1Img, (40, 70))
            elif index == 1:
                board.blit(self.p2Img, (40, 100))
            elif index == 2:
                board.blit(self.p3Img, (70, 70))
            else:
                board.blit(self.p4Img, (70, 100))
        elif thisPlayer.currentSpace.spaceName == "Falco":
            if index == 0:
                board.blit(self.p1Img, (160, 60))
            elif index == 1:
                board.blit(self.p2Img, (160, 90))
            elif index == 2:
                board.blit(self.p3Img, (190, 60))
            else:
                board.blit(self.p4Img, (190, 90))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "AssistTrophy2":
            if index == 0:
                board.blit(self.p1Img, (240, 60))
            elif index == 1:
                board.blit(self.p2Img, (270, 90))
            elif index == 2:
                board.blit(self.p3Img, (240, 60))
            else:
                board.blit(self.p4Img, (270, 90))
            if thisPlayer == activePlayer:
                drawPiles.drawAssistTrophy(thisPlayer, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Wolf":
            if index == 0:
                board.blit(self.p1Img, (320, 60))
            elif index == 1:
                board.blit(self.p2Img, (350, 90))
            elif index == 2:
                board.blit(self.p3Img, (320, 60))
            else:
                board.blit(self.p4Img, (350, 90))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Fox":
            if index == 0:
                board.blit(self.p1Img, (400, 60))
            elif index == 1:
                board.blit(self.p2Img, (430, 90))
            elif index == 2:
                board.blit(self.p3Img, (400, 60))
            else:
                board.blit(self.p4Img, (430, 90))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Roy":
            if index == 0:
                board.blit(self.p1Img, (480, 60))
            elif index == 1:
                board.blit(self.p2Img, (510, 90))
            elif index == 2:
                board.blit(self.p3Img, (480, 60))
            else:
                board.blit(self.p4Img, (510, 90))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Samus":
            if index == 0:
                board.blit(self.p1Img, (560, 60))
            elif index == 1:
                board.blit(self.p2Img, (590, 90))
            elif index == 2:
                board.blit(self.p3Img, (560, 60))
            else:
                board.blit(self.p4Img, (590, 90))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Dark Samus":
            if index == 0:
                board.blit(self.p1Img, (640, 60))
            elif index == 1:
                board.blit(self.p2Img, (670, 90))
            elif index == 2:
                board.blit(self.p3Img, (640, 60))
            else:
                board.blit(self.p4Img, (670, 90))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Mr Game & Watch":
            if index == 0:
                board.blit(self.p1Img, (720, 60))
            elif index == 1:
                board.blit(self.p2Img, (750, 90))
            elif index == 2:
                board.blit(self.p3Img, (720, 60))
            else:
                board.blit(self.p4Img, (750, 90))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Zero Suit Samus":
            if index == 0:
                board.blit(self.p1Img, (800, 60))
            elif index == 1:
                board.blit(self.p2Img, (830, 90))
            elif index == 2:
                board.blit(self.p3Img, (800, 60))
            else:
                board.blit(self.p4Img, (830, 90))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Ryu":
            if index == 0:
                board.blit(self.p1Img, (900, 150))
            elif index == 1:
                board.blit(self.p2Img, (930, 180))
            elif index == 2:
                board.blit(self.p3Img, (900, 150))
            else:
                board.blit(self.p4Img, (930, 180))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Terry":
            if index == 0:
                board.blit(self.p1Img, (900, 230))
            elif index == 1:
                board.blit(self.p2Img, (930, 260))
            elif index == 2:
                board.blit(self.p3Img, (900, 230))
            else:
                board.blit(self.p4Img, (930, 260))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "PokeBall3":
            if index == 0:
                board.blit(self.p1Img, (900, 310))
            elif index == 1:
                board.blit(self.p2Img, (930, 340))
            elif index == 2:
                board.blit(self.p3Img, (900, 310))
            else:
                board.blit(self.p4Img, (930, 340))
            if thisPlayer == activePlayer:
                drawPiles.drawPokeBall(thisPlayer, players)
        elif thisPlayer.currentSpace.spaceName == "Kazuya":
            if index == 0:
                board.blit(self.p1Img, (900, 390))
            elif index == 1:
                board.blit(self.p2Img, (930, 420))
            elif index == 2:
                board.blit(self.p3Img, (900, 390))
            else:
                board.blit(self.p4Img, (930, 420))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "Byleth":
            if index == 0:
                board.blit(self.p1Img, (900, 470))
            elif index == 1:
                board.blit(self.p2Img, (930, 500))
            elif index == 2:
                board.blit(self.p3Img, (900, 470))
            else:
                board.blit(self.p4Img, (930, 500))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "AssistTrophy3":
            if index == 0:
                board.blit(self.p1Img, (900, 550))
            elif index == 1:
                board.blit(self.p2Img, (930, 580))
            elif index == 2:
                board.blit(self.p3Img, (900, 550))
            else:
                board.blit(self.p4Img, (930, 580))
            if thisPlayer == activePlayer:
                drawPiles.drawAssistTrophy(thisPlayer, players, roll)
        elif thisPlayer.currentSpace.spaceName == "Pyra":
            if index == 0:
                board.blit(self.p1Img, (900, 630))
            elif index == 1:
                board.blit(self.p2Img, (930, 660))
            elif index == 2:
                board.blit(self.p3Img, (900, 630))
            else:
                board.blit(self.p4Img, (930, 660))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
        elif thisPlayer.currentSpace.spaceName == "DLC Tax":
            if index == 0:
                board.blit(self.p1Img, (900, 710))
            elif index == 1:
                board.blit(self.p2Img, (930, 740))
            elif index == 2:
                board.blit(self.p3Img, (900, 710))
            else:
                board.blit(self.p4Img, (930, 740))
            if thisPlayer == activePlayer:
                thisPlayer.money -= 100
        elif thisPlayer.currentSpace.spaceName == "Mythra":
            if index == 0:
                board.blit(self.p1Img, (900, 790))
            elif index == 1:
                board.blit(self.p2Img, (930, 820))
            elif index == 2:
                board.blit(self.p3Img, (900, 790))
            else:
                board.blit(self.p4Img, (930, 820))
            if thisPlayer == activePlayer:
                thisPlayer.currentSpace.propertyAction(thisPlayer, board, roll)
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