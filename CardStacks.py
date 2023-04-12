from ChanceCommunityChestCard import Card
from random import randint
from MovementFile import movementLocation
import pygame
class cardStacks:
    def __init__(self, numPlayers):
        self.newAssistTrophyPile = [Card("Advance to Mythra, if you pass GO collect $200"), Card("Advance to GO (Collect $200)"), Card("Advance to Fox. If you pass GO, collect $200"), Card("Advance to Jigglypuff. If you pass GO, collect $200)"), Card("Advance to the nearest Fire Emblem Character. If unowned, you may buy it from the bank. If owned, pay owner twice the rental to which they are otherwise entitled. If you pass GO, collect $200"), Card("Advance to the nearest Fire Emblem Character. If unowned, you may buy it from the bank. If owned, pay owner twice the rental to which they are otherwise entitled. If you pass GO, collect $200"), Card("Advance to the nearest Retro Character. If unowned, you may buy it from the bank. If owned, pay owner ten times what you rolled on the dice. If you pass GO, collect $200"), Card("Bank pays you dividend of $50"), Card("Get out of jail free"), Card("Go back 3 spaces"), Card("Go directly to jail. Do not pass GO, do not collect $200."), Card("Make general repairs on all your property. For each house, pay $25. For each hotel, pay $100"), Card("Tournament fee, pay $15"), Card("Advance to Marth. If you pass GO, collect $200"), Card("Your faulty adapter broke everyone's controllers. Pay each player $50"), Card("You won a regional! Collect $150.")]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        self.usedAssistTrophyPile = []
        self.newPokeBallPile = [Card("Advance to GO (Collect $200)"), Card("Win a major. Collect $200."), Card("Lose a money match. Pay $50"), Card("Your income from your combo video came in. Collect $50"), Card("Get out of jail free"), Card("Go directly to jail. Do not pass GO, do not collect $200"), Card("Win a major side bracket. Collect $100"), Card("Refund your Steve and Kazuya DLC purchases after they got banned. Collect $20"), Card("It's your birthday. Collect $10 from every player."), Card("Win a giveaway. Collect $100"), Card("Get caught throwing a crab in a tournament. Pay $100"), Card("Buy a new copy of Super Smash Bros Ultimate. Pay $50"), Card("Got to Elite Smash with your first character. Collect $25."), Card("Pay out tournament prize pot. Pay $40 per house owned and $115 per hotel owned."), Card("You placed in top 8 at a local. Collect $10"), Card("You got sponsored! Collect $100")]
        self.usedPokeBallPile = []
        self.numPlayers = numPlayers
        self.SCREENHEIGHT = 300
        self.SCREENWIDTH = 500
        self.font = pygame.font.SysFont(None, 24)
        self.smallFont = pygame.font.SysFont(None, 20)
        self.BLACK = (0,0,0)

    def findSpace(self, spaceName, spaces): #gets space from spaces given a spaceName
     for space in spaces:
         if spaceName == space.spaceName:
             print("First: " + space.spaceName)
             return space


    def drawAssistTrophy(self, activePlayer, allPlayers, spaces):
        playerIndex = -1
        for i in range(len(allPlayers)):
            if activePlayer.playerName == allPlayers[i].playerName:
                playerIndex = i
                break

        selectedCard = self.newAssistTrophyPile.pop(randint(0, len(self.newAssistTrophyPile) - 1))
        self.usedAssistTrophyPile.append(selectedCard)
        if len(self.newAssistTrophyPile) == 0:
            self.newAssistTrophyPile = self.usedAssistTrophyPile.copy()
            self.usedAssistTrophyPile = []
        if selectedCard.text == "Advance to Mythra, if you pass GO collect $200":
            if allPlayers[playerIndex].currentSpace == self.findSpace("Mythra", spaces):
                allPlayers[playerIndex].money += 200
            else:
                allPlayers[playerIndex].currentSpace = spaces[len(spaces)-1]
        elif selectedCard.text == "Advance to GO (Collect $200)":
            allPlayers[playerIndex].currentSpace = spaces[0]
            allPlayers[playerIndex].money += 200
        elif selectedCard.text == "Advance to Fox. If you pass GO, collect $200":
            for i in range(24, 40):
                if allPlayers[playerIndex].currentSpace == spaces[i]:
                    allPlayers[playerIndex].money += 200
                    break
            allPlayers[playerIndex].currentSpace = spaces[24]
            for i in range(len(allPlayers)):
                if i != playerIndex:
                    if spaces[24] in allPlayers[i].properties & spaces[24].isMortgaged == False:
                        allPlayers[i].money += spaces[24].rent
                        allPlayers[playerIndex].money -= spaces[24].rent
                        break
        elif selectedCard.text == "Advance to Jigglypuff. If you pass GO, collect $200":
            for i in range(11, 40):
                if allPlayers[playerIndex].currentSpace == spaces[i]:
                    allPlayers[playerIndex].money += 200
                    break
            allPlayers[playerIndex].currentSpace = spaces[11]
            for i in range(len(allPlayers)):
                if i != playerIndex:
                    if spaces[11] in allPlayers[i].properties & spaces[11].isMortgaged == False:
                        allPlayers[i].money += spaces[11].rent
                        allPlayers[playerIndex].money -= spaces[11].rent
                        break
        elif selectedCard.text == "Advance to the nearest Fire Emblem Character. If unowned, you may buy it from the bank. If owned, pay owner twice the rental to which they are otherwise entitled. If you pass GO, collect $200":
            origPos = spaces.index(allPlayers[playerIndex].currentSpace)
            newPos = spaces.index(self.findSpace(allPlayers[playerIndex].currentSpace.nearestFE, spaces))
            if origPos > newPos:
                allPlayers[playerIndex].money += 200
            allPlayers[playerIndex].currentSpace = self.findSpace(allPlayers[playerIndex].currentSpace.nearestFE, spaces)
            for i in range(len(allPlayers)):
                if i != playerIndex:
                    if allPlayers[i].currentSpace in allPlayers[i].properties & allPlayers[i].currentSpace.isMortgaged == False:
                        allPlayers[i].money += allPlayers[i].currentSpace.rent
                        allPlayers[playerIndex].money -= allPlayers[i].currentSpace.rent
                        break
        elif selectedCard.text == "Advance to the nearest Retro Character. If unowned, you may buy it from the bank. If owned, pay owner ten times what you rolled on the dice. If you pass GO, collect $200":
            origPos = spaces.index(allPlayers[playerIndex].currentSpace)
            newPos = spaces.index(self.findSpace(allPlayers[playerIndex].currentSpace.nearestRetro, spaces))
            if origPos > newPos:
                allPlayers[playerIndex].money += 200
            allPlayers[playerIndex].currentSpace = self.findSpace(allPlayers[playerIndex].currentSpace.nearestRetro, spaces)
            for i in range(len(allPlayers)):
                if i != playerIndex:
                    if allPlayers[i].currentSpace in allPlayers[i].properties & allPlayers[i].currentSpace.isMortgaged == False:
                        allPlayers[i].money += allPlayers[i].currentSpace.rent
                        allPlayers[playerIndex].money -= allPlayers[i].currentSpace.rent
                        break
        elif selectedCard.text == "Bank pays you dividend of $50":
            allPlayers[playerIndex].money += 50
        elif selectedCard.text == "Get out of jail free":
            allPlayers[playerIndex].hasGetOutOfJailFree = True
        elif selectedCard.text == "Go back 3 spaces":
            allPlayers[playerIndex].currentSpace = spaces[spaces.index(allPlayers[playerIndex].currentSpace - 3)]
        elif selectedCard.text == "Go directly to jail. Do not pass GO, do not collect $200.":
            allPlayers[playerIndex].currentSpace = self.findSpace("Jail", spaces)
            allPlayers[playerIndex].inJail = True
        elif selectedCard.text == "Make general repairs on all your property. For each house, pay $25. For each hotel, pay $100":
            cost = 0
            for property in allPlayers[playerIndex].properties:
                if property.numHouses == 5:
                    cost += 100
                else:
                    cost += (25 * property.numHouses)
            allPlayers[playerIndex].money -= cost
        elif selectedCard.text == "Tournament fee, pay $15":
            allPlayers[playerIndex].money -= 15
        elif selectedCard.text == "Advance to Marth. If you pass GO, collect $200":
            origPos = spaces.index(allPlayers[playerIndex].currentSpace)
            #newPos = spaces.index(self.findSpace(allPlayers[playerIndex].currentSpace.nearestRetro, spaces))
            if origPos > 5:
                allPlayers[playerIndex].money += 200
            allPlayers[playerIndex].currentSpace = self.findSpace("Marth", spaces)
            for i in range(len(allPlayers)):
                if i != playerIndex:
                    if allPlayers[i].currentSpace in allPlayers[i].properties & allPlayers[i].currentSpace.isMortgaged == False:
                        allPlayers[i].money += allPlayers[i].currentSpace.rent
                        allPlayers[playerIndex].money -= allPlayers[i].currentSpace.rent
                        break
        elif selectedCard.text == "Your faulty adapter broke everyone's controllers. Pay each player $50":
            for player in allPlayers:
                if player != activePlayer:
                    player.money += 50
                    allPlayers[playerIndex] -= 50
        elif selectedCard.text == "You won a regional! Collect $150.":
            allPlayers[playerIndex].money += 150
        
        pygame.init()
        screen = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        screen.fill((255, 165, 0))
        message = pygame.Surface((300, 150))
        message.fill((255, 165, 0))
        messageText = self.font.render(selectedCard.text, True, self.BLACK)
        textRect = messageText.get_rect()
        textRect.center = message.get_rect().center
        buttonText = self.smallFont.render("OK", True, self.BLACK)
        buttonRect = buttonText.get_rect()
        buttonRect.bottomright=message.get_rect().bottomright
        pygame.draw.rect(message, (255, 165, 0), buttonRect, 1)
        message.blit(buttonText, buttonRect)

        messageRect = message.get_rect()
        messageRect.center = screen.get_rect().center
        screen.blit(message, messageRect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if buttonRect.collidepoint(event.pos):
                        pygame.quit()
                        exit()


        

    def drawPokeBall(self, activePlayer, allPlayers, spaces):
        playerIndex = -1
        for i in range(len(allPlayers)):
            if activePlayer.playerName == allPlayers[i].playerName:
                playerIndex = i
                break

        selectedCard = self.newPokeBallPile.pop(randint(0, len(self.newPokeBallPile) - 1))
        self.usedPokeBallPile.append(selectedCard)
        if len(self.newPokeBallPile) == 0:
            self.newPokeBallPile = self.usedPokeBallPile.copy()
            self.usedPokeBallPile = []

        if selectedCard.text == "Advance to GO (Collect $200)":
            allPlayers[playerIndex].currentSpace = spaces[0]
            allPlayers[playerIndex].money += 200
        elif selectedCard.text == "Win a major. Collect $200.":
            allPlayers[playerIndex].money += 200
        elif selectedCard.text == "Lose a money match. Pay $50":
            allPlayers[playerIndex].money -= 50
        elif selectedCard.text == "Your income from your combo video came in. Collect $50":
            allPlayers[playerIndex].money += 50
        elif selectedCard.text == "Get out of jail free":
            allPlayers[playerIndex].getOutOfJailFree = True
        elif selectedCard.text == "Go directly to jail. Do not pass GO, do not collect $200":
            allPlayers[playerIndex].currentSpace = self.findSpace("Jail", spaces)
            allPlayers[playerIndex].inJail = True
        elif selectedCard.text == "Win a major side bracket. Collect $100":
            allPlayers[playerIndex].money += 100
        elif selectedCard.text == "Refund your Steve and Kazuya DLC purchases after they got banned. Collect $20":
            allPlayers[playerIndex].money += 20
        elif selectedCard.text == "It's your birthday. Collect $10 from every player.":
            for player in allPlayers:
                if player != activePlayer:
                    player.money -= 10
                    allPlayers[playerIndex] += 10
        elif selectedCard.text == "Win a giveaway. Collect $100":
            allPlayers[playerIndex].money += 100
        elif selectedCard.text == "Get caught throwing a crab in a tournament. Pay $100":
            allPlayers[playerIndex].money -= 100
        elif selectedCard.text == "Buy a new copy of Super Smash Bros Ultimate. Pay $50":
            allPlayers[playerIndex].money -= 50
        elif selectedCard.text == "Got to Elite Smash with your first character. Collect $25.":
            allPlayers[playerIndex].money += 25
        elif selectedCard.text == "Pay out tournament prize pot. Pay $40 per house owned and $115 per hotel owned.":
            cost = 0
            for property in allPlayers[playerIndex].properties:
                if property.numHouses == 5:
                    cost += 115
                else:
                    cost += (40 * property.numHouses)
            allPlayers[playerIndex].money -= cost
        elif selectedCard.text == "You placed in top 8 at a local. Collect $10":
            allPlayers[playerIndex].money += 10
        elif selectedCard.text == "You got sponsored! Collect $100":
            allPlayers[playerIndex].money += 100 

        pygame.init()
        screen = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        screen.fill((255, 165, 0))
        message = pygame.Surface((300, 150))
        message.fill((255, 165, 0))
        messageText = self.font.render(selectedCard.text, True, self.BLACK)
        textRect = messageText.get_rect()
        textRect.center = message.get_rect().center
        buttonText = self.smallFont.render("OK", True, self.BLACK)
        buttonRect = buttonText.get_rect()
        buttonRect.bottomright=message.get_rect().bottomright
        pygame.draw.rect(message, (255, 165, 0), buttonRect, 1)
        message.blit(buttonText, buttonRect)

        messageRect = message.get_rect()
        messageRect.center = screen.get_rect().center
        screen.blit(message, messageRect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if buttonRect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

    
            



        



        

