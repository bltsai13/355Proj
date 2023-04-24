from ChanceCommunityChestCard import Card
from random import randint
from ImageModifier import ImageModifier
import pygame
from GameWindows import gameWindows
class cardStacks:
    def __init__(self, numPlayers, spaces, surface):
        self.newAssistTrophyPile = [Card("Advance to Mythra, if you pass GO collect $200"), Card("Advance to GO (Collect $200)"), Card("Advance to Fox. If you pass GO, collect $200"), Card("Advance to Jigglypuff. If you pass GO, collect $200"), Card("Advance to the nearest FE Character. If owned, pay owner double rent."), Card("Advance to the nearest FE Character. If owned, pay owner double rent."), Card("Advance to the nearest Retro Character. If owned, pay 10X dice roll."), Card("Bank pays you dividend of $50"), Card("Get out of jail free"), Card("Go back 3 spaces"), Card("Go directly to jail. Do not pass GO, do not collect $200."), Card("Software update. Pay $25 per house, $100 per hotel"), Card("Tournament fee, pay $15"), Card("Advance to Marth. If you pass GO, collect $200"), Card("Your faulty adapter broke everyone's controllers. Pay everyone $50"), Card("You won a regional! Collect $150.")]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        self.usedAssistTrophyPile = []
        self.newPokeBallPile = [Card("Advance to GO (Collect $200)"), Card("Win a major. Collect $200."), Card("Lose a money match. Pay $50"), Card("Your income from your combo video came in. Collect $50"), Card("Get out of jail free"), Card("Go directly to jail. Do not pass GO, do not collect $200"), Card("Win a major side bracket. Collect $100"), Card("Refund Steve & Kazuya DLC after they got banned. Collect $20"), Card("It's your birthday. Collect $10 from every player."), Card("Win a giveaway. Collect $100"), Card("Get caught throwing a crab in a tournament. Pay $100"), Card("Buy a new copy of Super Smash Bros Ultimate. Pay $50"), Card("Got to Elite Smash with your first character. Collect $25."), Card("Pay out tournament prize pot. Pay $40 per house, $115 per hotel."), Card("You placed in top 8 at a local. Collect $10"), Card("You got sponsored! Collect $100")]
        self.usedPokeBallPile = []
        self.numPlayers = numPlayers
        self.SCREENHEIGHT = 300
        self.SCREENWIDTH = 500
        self.font = pygame.font.SysFont(None, 20)
        self.smallFont = pygame.font.SysFont(None, 16)
        self.BLACK = (0,0,0)
        self.spaces = spaces
        self.surface = surface

    def findSpace(self, spaceName): #gets space from spaces given a spaceName
     for space in self.spaces:
         if spaceName == space.spaceName:
             print("First: " + space.spaceName)
             return space


    def drawAssistTrophy(self, activePlayer, allPlayers, roll):
        playerIndex = -1
        for i in range(len(allPlayers)):
            if activePlayer == allPlayers[i]:
                playerIndex = i
                break
        gw = gameWindows(self.surface)
        imgMod = ImageModifier()

        selectedCard = self.newAssistTrophyPile.pop(randint(0, len(self.newAssistTrophyPile) - 1))
        self.usedAssistTrophyPile.append(selectedCard)
        gw.createBoard(self.smallFont, allPlayers, self, None)
        self.surface.blit(imgMod.space_modifier("roll" +str(roll[0])+ ".jpg", 60, 60, 0), (400, 300))            
        self.surface.blit(imgMod.space_modifier("roll" +str(roll[1])+ ".jpg", 60, 60, 0), (500, 300)) 
        messageText = self.font.render(selectedCard.text, True, self.BLACK)
        textRect = messageText.get_rect()
        textRect.center = (375, 750)
        buttonText = self.smallFont.render("OK", True, self.BLACK)
        buttonRect = buttonText.get_rect()
        buttonRect.center = (375, 800)
        self.surface.blit(buttonText, buttonRect)
        self.surface.blit(messageText, textRect)
        pygame.display.update()
        if len(self.newAssistTrophyPile) == 0:
            self.newAssistTrophyPile = self.usedAssistTrophyPile.copy()
            self.usedAssistTrophyPile = []
        if selectedCard.text == "Advance to Mythra, if you pass GO collect $200":
            if allPlayers[playerIndex].currentSpace == self.findSpace("Mythra"):
                allPlayers[playerIndex].money += 200
            else:
                allPlayers[playerIndex].currentSpace = self.spaces[len(self.spaces)-1]
            allPlayers[playerIndex].getNewBoardPos(self.surface, allPlayers[playerIndex], playerIndex, allPlayers, self, activePlayer, roll)
            print("1")
        elif selectedCard.text == "Advance to GO (Collect $200)":
            allPlayers[playerIndex].currentSpace = self.spaces[0]
            allPlayers[playerIndex].money += 200
            allPlayers[playerIndex].getNewBoardPos(self.surface, allPlayers[playerIndex], playerIndex, allPlayers, self, activePlayer, roll)
            print("2")
        elif selectedCard.text == "Advance to Fox. If you pass GO, collect $200":
            for i in range(24, 40):
                if allPlayers[playerIndex].currentSpace == self.spaces[i]:
                    allPlayers[playerIndex].money += 200
            allPlayers[playerIndex].currentSpace = self.spaces[24]
            allPlayers[playerIndex].getNewBoardPos(self.surface, allPlayers[playerIndex], playerIndex, allPlayers, self, activePlayer, roll)
            print("3")
        elif selectedCard.text == "Advance to Jigglypuff. If you pass GO, collect $200":
            for i in range(11, 40):
                if allPlayers[playerIndex].currentSpace == self.spaces[i]:
                    allPlayers[playerIndex].money += 200
            allPlayers[playerIndex].currentSpace = self.spaces[11]
            allPlayers[playerIndex].getNewBoardPos(self.surface, allPlayers[playerIndex], playerIndex, allPlayers, self, activePlayer, roll)
            print("4")
        elif selectedCard.text == "Advance to the nearest FE Character. If owned, pay owner double rent.":
            origPos = self.spaces.index(allPlayers[playerIndex].currentSpace)
            newPos = self.spaces.index(self.findSpace(allPlayers[playerIndex].currentSpace.nearestFE))
            if origPos > newPos:
                allPlayers[playerIndex].money += 200
            allPlayers[playerIndex].currentSpace = self.findSpace(allPlayers[playerIndex].currentSpace.nearestFE)
            allPlayers[playerIndex].getNewBoardPos(self.surface, allPlayers[playerIndex], playerIndex, allPlayers, self, activePlayer, roll)
            print("5")
        elif selectedCard.text == "Advance to the nearest Retro Character. If owned, pay 10X your dice roll.":
            origPos = self.spaces.index(allPlayers[playerIndex].currentSpace)
            newPos = self.spaces.index(self.findSpace(allPlayers[playerIndex].currentSpace.nearestRetro))
            if origPos > newPos:
                allPlayers[playerIndex].money += 200
            allPlayers[playerIndex].currentSpace = self.findSpace(allPlayers[playerIndex].currentSpace.nearestRetro)
            allPlayers[playerIndex].getNewBoardPos(self.surface, allPlayers[playerIndex], playerIndex, allPlayers, self, activePlayer, roll)
            print("6")
        elif selectedCard.text == "Bank pays you dividend of $50":
            allPlayers[playerIndex].money += 50
            print("7")
        elif selectedCard.text == "Get out of jail free":
            allPlayers[playerIndex].hasGetOutOfJailFree = True
            print("8")
        elif selectedCard.text == "Go back 3 spaces":
            allPlayers[playerIndex].currentSpace = self.spaces[self.spaces.index(allPlayers[playerIndex].currentSpace) - 3]
            if allPlayers[playerIndex].currentSpace.spaceName == "PokeBall3":
                self.drawPokeBall(activePlayer, allPlayers, roll)
            elif allPlayers[playerIndex].currentSpace.spaceName == "Low Tier Tax":
                activePlayer.money -= 200
            else:
                allPlayers[playerIndex].getNewBoardPos(self.surface, allPlayers[playerIndex], playerIndex, allPlayers, self, activePlayer, roll)
            print("9")
        elif selectedCard.text == "Go directly to jail. Do not pass GO, do not collect $200.":
            allPlayers[playerIndex].currentSpace = self.findSpace("Jail")
            allPlayers[playerIndex].getNewBoardPos(self.surface, allPlayers[playerIndex], playerIndex, allPlayers, self, activePlayer, roll)
            allPlayers[playerIndex].inJail = True
            print("10")
        elif selectedCard.text == "Software update. Pay $25 per house, $100 per hotel":
            cost = 0
            for property in allPlayers[playerIndex].properties:
                if property.numHouses == 5:
                    cost += 100
                else:
                    cost += (25 * property.numHouses)
            allPlayers[playerIndex].money -= cost
            print("11")
        elif selectedCard.text == "Tournament fee, pay $15":
            allPlayers[playerIndex].money -= 15
            print("12")
        elif selectedCard.text == "Advance to Marth. If you pass GO, collect $200":
            origPos = self.spaces.index(allPlayers[playerIndex].currentSpace)
            if origPos > 5:
                allPlayers[playerIndex].money += 200
            allPlayers[playerIndex].currentSpace = self.findSpace("Marth")
            allPlayers[playerIndex].getNewBoardPos(self.surface, allPlayers[playerIndex], playerIndex, allPlayers, self, activePlayer, roll)
            print("13")
        elif selectedCard.text == "Your faulty adapter broke everyone's controllers. Pay everyone $50": 
            for player in allPlayers:
                if player != activePlayer:
                    player.money += 50
                    allPlayers[playerIndex].money -= 50
            print("14")
        elif selectedCard.text == "You won a regional! Collect $150.":
            allPlayers[playerIndex].money += 150
            print("15")
        gw.createBoard(self.smallFont, allPlayers, self, None)
        self.surface.blit(imgMod.space_modifier("roll" +str(roll[0])+ ".jpg", 60, 60, 0), (400, 300))            
        self.surface.blit(imgMod.space_modifier("roll" +str(roll[1])+ ".jpg", 60, 60, 0), (500, 300)) 
        messageText = self.font.render(selectedCard.text, True, self.BLACK)
        textRect = messageText.get_rect()
        textRect.center = (350, 750)
        buttonText = self.smallFont.render("OK", True, self.BLACK)
        buttonRect = buttonText.get_rect()
        buttonRect.center = (350, 800)
        self.surface.blit(buttonText, buttonRect)
        self.surface.blit(messageText, textRect)
        pygame.display.update()
        isDisplayed = True

        while isDisplayed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("bruh")
                    isDisplayed = False
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if buttonRect.collidepoint(event.pos):
                        print("bruh2")
                        isDisplayed = False
                        return

    def drawPokeBall(self, activePlayer, allPlayers, roll):
        playerIndex = -1
        for i in range(len(allPlayers)):
            if activePlayer == allPlayers[i]:
                playerIndex = i
                break
        gw = gameWindows(self.surface)
        imgMod = ImageModifier()

        selectedCard = self.newPokeBallPile.pop(randint(0, len(self.newPokeBallPile) - 1))
        self.usedPokeBallPile.append(selectedCard)
        if len(self.newPokeBallPile) == 0:
            self.newPokeBallPile = self.usedPokeBallPile.copy()
            self.usedPokeBallPile = []

        if selectedCard.text == "Advance to GO (Collect $200)":
            allPlayers[playerIndex].currentSpace = self.spaces[0]
            allPlayers[playerIndex].money += 200
            print("-1")
        elif selectedCard.text == "Win a major. Collect $200.":
            allPlayers[playerIndex].money += 200
            print("-2")
        elif selectedCard.text == "Lose a money match. Pay $50":
            allPlayers[playerIndex].money -= 50
            print("-3")
        elif selectedCard.text == "Your income from your combo video came in. Collect $50":
            allPlayers[playerIndex].money += 50
            print("-4")
        elif selectedCard.text == "Get out of jail free":
            allPlayers[playerIndex].getOutOfJailFree = True
            print("-5")
        elif selectedCard.text == "Go directly to jail. Do not pass GO, do not collect $200":
            allPlayers[playerIndex].currentSpace = self.findSpace("Jail")
            allPlayers[playerIndex].inJail = True
            print("-6")
        elif selectedCard.text == "Win a major side bracket. Collect $100":
            allPlayers[playerIndex].money += 100
            print("-7")
        elif selectedCard.text == "Refund Steve & Kazuya DLC after they got banned. Collect $20":
            allPlayers[playerIndex].money += 20
            print("-8")
        elif selectedCard.text == "It's your birthday. Collect $10 from every player.":
            for player in allPlayers:
                if player != activePlayer:
                    player.money -= 10
                    allPlayers[playerIndex].money += 10
            print("-9")
        elif selectedCard.text == "Win a giveaway. Collect $100":
            allPlayers[playerIndex].money += 100
            print("-10")
        elif selectedCard.text == "Get caught throwing a crab in a tournament. Pay $100":
            allPlayers[playerIndex].money -= 100
            print("-11")
        elif selectedCard.text == "Buy a new copy of Super Smash Bros Ultimate. Pay $50":
            allPlayers[playerIndex].money -= 50
            print("-12")
        elif selectedCard.text == "Got to Elite Smash with your first character. Collect $25.":
            allPlayers[playerIndex].money += 25
            print("-13")
        elif selectedCard.text == "Pay out tournament prize pot. Pay $40 per house, $115 per hotel.":
            cost = 0
            for property in allPlayers[playerIndex].properties:
                if property.numHouses == 5:
                    cost += 115
                else:
                    cost += (40 * property.numHouses)
            allPlayers[playerIndex].money -= cost
            print("-14")
        elif selectedCard.text == "You placed in top 8 at a local. Collect $10":
            allPlayers[playerIndex].money += 10
            print("-15")
        elif selectedCard.text == "You got sponsored! Collect $100":
            allPlayers[playerIndex].money += 100 
            print("-16")

        gw.createBoard(self.smallFont, allPlayers, self, None)
        self.surface.blit(imgMod.space_modifier("roll" +str(roll[0])+ ".jpg", 60, 60, 0), (400, 300))            
        self.surface.blit(imgMod.space_modifier("roll" +str(roll[1])+ ".jpg", 60, 60, 0), (500, 300)) 
        messageText = self.font.render(selectedCard.text, True, self.BLACK)
        textRect = messageText.get_rect()
        textRect.center = (350, 750)
        buttonText = self.smallFont.render("OK", True, self.BLACK)
        buttonRect = buttonText.get_rect()
        buttonRect.center = (350, 800)
        self.surface.blit(buttonText, buttonRect)
        self.surface.blit(messageText, textRect)
        pygame.display.update()
        isDisplayed = True

        while isDisplayed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("bruh3")
                    isDisplayed = False
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if buttonRect.collidepoint(event.pos):
                        print("bruh4")
                        isDisplayed = False
                        return
    

    
            



        



        

