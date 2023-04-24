import pygame
from ImageModifier import ImageModifier
from GameWindows import gameWindows
class Space():
    def __init__(self, spaceName, move2, move3, move4, move5, move6, move7, move8, move9, move10, move11, move12, back3, nearestRetro, nearestFE, baseRent, rent1House, rent2House, rent3House, rent4House, rentHotel, buyCost, houseCost):
        self.spaceName = spaceName
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.move5 = move5
        self.move6 = move6
        self.move7 = move7
        self.move8 = move8
        self.move9 = move9
        self.move10 = move10
        self.move11 = move11
        self.move12 = move12
        self.back3 = back3
        self.nearestRetro = nearestRetro
        self.nearestFE = nearestFE
        self.rent = baseRent
        self.baseRent = baseRent
        self.buyCost = buyCost
        self.mortgageValue = buyCost/2
        self.monopolyValue = baseRent * 2
        self.rent1House = rent1House
        self.rent2House = rent2House
        self.rent3House = rent3House
        self.rent4House = rent4House
        self.rentHotel = rentHotel
        self.houseCost = houseCost
        self.isMortgaged = False
        self.owner = None
        self.numHouses = 0
        self.BLACK = (0, 0, 0)
        
    def propertyAction(self, activePlayer, board, roll, players, drawPiles):
        gw = gameWindows(board)
        imgMod = ImageModifier()
        isDisplayed = True
        font = pygame.font.SysFont(None, 20)
        smallFont = pygame.font.SysFont(None, 16)
        gw.createBoard(smallFont, players, drawPiles, None)
        board.blit(imgMod.space_modifier("roll" +str(roll[0])+ ".jpg", 60, 60, 0), (400, 300))            
        board.blit(imgMod.space_modifier("roll" +str(roll[1])+ ".jpg", 60, 60, 0), (500, 300)) 
        if ((self.owner == None) & (activePlayer.money >= self.buyCost)):
            messageText = font.render("Would " + activePlayer.playerName + " like to buy " + self.spaceName + "?", True, self.BLACK)
            textRect = messageText.get_rect()
            textRect.center = (350, 750)
            buttonText = smallFont.render("No", True, self.BLACK)
            buttonRect = buttonText.get_rect()
            buttonRect.center = (300, 800)
            buttonText2 = smallFont.render("Yes", True, self.BLACK)
            buttonRect2 = buttonText2.get_rect()
            buttonRect2.center = (400, 800)
            board.blit(buttonText, buttonRect)
            board.blit(buttonText2, buttonRect2)
            board.blit(messageText, textRect)
            pygame.display.update()

            while isDisplayed:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if buttonRect.collidepoint(event.pos):
                            print("bruh2")
                            isDisplayed = False
                            return
                        elif (buttonRect2.collidepoint(event.pos) & (self.numHouses <= 4)):
                            print("bruh5")
                            activePlayer.properties.append(self)
                            activePlayer.money -= self.buyCost
                            self.owner = activePlayer
                            isDisplayed = False
                            return
        else:
            if ((self.owner == activePlayer) & (self.numHouses < 5) & (activePlayer.money >= self.houseCost) & (self.spaceName not in ["Marth", "Ike", "Roy", "Byleth", "Pac Man", "Mr Game & Watch"])):
                messageText = font.render("Would " + self.owner.playerName + " like to buy a house?", True, self.BLACK)
                textRect = messageText.get_rect()
                textRect.center = (350, 750)
                buttonText = smallFont.render("No", True, self.BLACK)
                buttonRect = buttonText.get_rect()
                buttonRect.center = (300, 800)
                buttonText2 = smallFont.render("Yes", True, self.BLACK)
                buttonRect2 = buttonText2.get_rect()
                buttonRect2.center = (400, 800)
                board.blit(buttonText, buttonRect)
                board.blit(buttonText2, buttonRect2)
                board.blit(messageText, textRect)                         
                pygame.display.update()
                while isDisplayed:
                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                            pygame.quit()
                            exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if buttonRect.collidepoint(event.pos):
                                print("bruh2")
                                isDisplayed = False
                                return
                            elif buttonRect2.collidepoint(event.pos):
                                print("bruh5")
                                self.numHouses += 1
                                if self.numHouses == 1:
                                    self.rent = self.rent1House
                                elif self.numHouses == 2:
                                    self.rent = self.rent2House
                                elif self.numHouses == 3:
                                    self.rent = self.rent3House
                                elif self.numHouses == 4:
                                    self.rent = self.rent4House
                                else:
                                    self.rent = self.rentHotel
                                activePlayer.money -= self.houseCost
                                rect = []
                                if self.spaceName == "Ganondorf":
                                    rect = [782, 860, 76, 20]
                                elif self.spaceName == "Little Mac":
                                    rect = [622, 860, 76, 20]
                                elif self.spaceName == "King Dedede":
                                    rect = [382, 860, 76, 20]
                                elif self.spaceName == "Kirby":
                                    rect = [222, 860, 76, 20]
                                elif self.spaceName == "Meta Knight":
                                    rect = [142, 860, 76, 20]
                                elif self.spaceName == "Jigglypuff":
                                    rect = [120, 782, 20, 76]
                                elif self.spaceName == "Mewtwo":
                                    rect = [120, 622, 20, 76]
                                elif self.spaceName == "Incineroar":
                                    rect = [120, 542, 20, 76]
                                elif self.spaceName == "Young Link":
                                    rect = [120, 382, 20, 76]
                                elif self.spaceName == "Toon Link":
                                    rect = [120, 222, 20, 76]
                                elif self.spaceName == "Link":
                                    rect = [120, 142, 20, 76]
                                elif self.spaceName == "Falco":
                                    rect = [142, 120, 76, 20]
                                elif self.spaceName == "Wolf":
                                    rect = [302, 120, 76, 20]
                                elif self.spaceName == "Fox":
                                    rect = [382, 120, 76, 20]
                                elif self.spaceName == "Samus":
                                    rect = [542, 120, 76, 20]
                                elif self.spaceName == "Dark Samus":
                                    rect = [622, 120, 76, 20]
                                elif self.spaceName == "Zero Suit Samus":
                                    rect = [782, 120, 76, 20]
                                elif self.spaceName == "Ryu":
                                    rect = [860, 142, 20, 76]
                                elif self.spaceName == "Terry":
                                    rect = [860, 222, 20, 76]
                                elif self.spaceName == "Kazuya":
                                    rect = [860, 382, 20, 76]
                                elif self.spaceName == "Pyra":
                                    rect = [860, 622, 20, 76]
                                elif self.spaceName == "Mythra":
                                    rect = [860, 782, 20, 76]
                                self.setHouses(board, rect)
                                return
            elif(((self.owner != activePlayer) & (self.owner != None)) & (self.isMortgaged == False)):
                if ((self.spaceName == "Pac Man") or (self.spaceName == "Mr Game & Watch")):
                    if ((self.owner.calcNumUtils() == 2)):
                        rent = 10 * (roll[0] + roll[1])
                        activePlayer.money -= (10 * (roll[0]+roll[1]))
                        self.owner.money += (10 * (roll[0]+roll[1]))
                    else:
                        rent = 4*(roll[0]+roll[1])
                        activePlayer.money -= (4 * (roll[0]+roll[1]))
                        self.owner.money += (4 * (roll[0]+roll[1]))
                elif ((self.spaceName == "Marth") or (self.spaceName == "Ike") or (self.spaceName == "Roy") or (self.spaceName == "Byleth")):
                    numUtils = self.owner.calcNumFEs()
                    rent = 0
                    if numUtils == 1:
                        rent = 25
                        activePlayer.money -= 25
                        self.owner.money += 25
                    if numUtils == 2:
                        rent = 50
                        activePlayer.money -= 50
                        self.owner.money += 50
                    if numUtils == 3:
                        rent = 100
                        activePlayer.money -= 100
                        self.owner.money += 100
                    if numUtils == 4:
                        rent = 200
                        activePlayer.money -= 200
                        self.owner.money += 200               
                else:                        
                    if self.numHouses == 0:
                        if self.partOfMonopoly():
                            rent = self.baseRent * 2
                            activePlayer.money -= (self.baseRent * 2)
                            self.owner.money += (self.baseRent * 2)
                        else:
                            rent = self.baseRent
                            activePlayer.money -= self.baseRent
                            self.owner.money += self.baseRent
                    elif self.numHouses == 1:
                        if self.partOfMonopoly():
                            rent = self.rent1House * 2
                            activePlayer.money -= (self.rent1House * 2)
                            self.owner.money += (self.rent1House * 2)
                        else:
                            rent = self.rent1House
                            activePlayer.money -= self.rent1House
                            self.owner.money += self.rent1House
                    elif self.numHouses == 2:
                        if self.partOfMonopoly():
                            rent = self.rent2House * 2
                            activePlayer.money -= (self.rent2House * 2)
                            self.owner.money += (self.rent2House * 2)
                        else:
                            rent = self.rent2House
                            activePlayer.money -= self.rent2House
                            self.owner.money += self.rent2House
                    elif self.numHouses == 3:
                        if self.partOfMonopoly():
                            rent = self.rent3House * 2
                            activePlayer.money -= (self.rent3House * 2)
                            self.owner.money += (self.rent3House * 2)
                        else:
                            rent = self.rent3House
                            activePlayer.money -= self.rent3House
                            self.owner.money += self.rent3House
                    elif self.numHouses == 4:
                        if self.partOfMonopoly():
                            rent = self.rent4House * 2
                            activePlayer.money -= (self.rent4House * 2)
                            self.owner.money += (self.rent4House * 2)
                        else:
                            rent = self.rent4House
                            activePlayer.money -= self.rent4House
                            self.owner.money += self.rent4House
                    elif self.numHouses == 5:
                        if self.partOfMonopoly():
                            rent = self.rentHotel * 2
                            activePlayer.money -= (self.rentHotel * 2)
                            self.owner.money += (self.rentHotel * 2)
                        else:
                            rent = self.rentHotel
                            activePlayer.money -= self.rentHotel
                            self.owner.money += self.rentHotel
                messageText = font.render(activePlayer.playerName + " paid $" + str(rent) + " to " + self.owner.playerName, True, self.BLACK)
                textRect = messageText.get_rect()
                textRect.center = (350, 750)
                board.blit(messageText, textRect)
                pygame.display.update()
    def setOwnerOutline(self, board, players, coords):
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        GREEN = (0, 255, 0)
        BLACK = (0, 0, 0)
        colorList = [BLUE, RED, GREEN, YELLOW]
        if self.owner == None:
            pygame.draw.rect(board, BLACK, coords, 1)
        else:
            for i in range(len(players)):
                if self.owner == players[i]:
                    pygame.draw.rect(board, colorList[i], coords, 1)
                    break
    def setHouses(self, board, rect):
        imgMod = ImageModifier()
        if self.spaceName in ["Ganondorf", "Little Mac", "King Dedede", "Kirby", "Meta Knight", "Falco", "Wolf", "Fox", "Samus", "Dark Samus", "Zero Suit Samus"]:
            houseWidth = rect[2]/4
            if self.numHouses == 5:
                board.blit(imgMod.space_modifier('hotel.jpg', houseWidth, rect[3], 0), (rect[0], rect[1]))
            else:
                for i in range(self.numHouses):
                    if i == 0:
                        board.blit(imgMod.space_modifier('house.jpg', houseWidth, rect[3], 0), (rect[0] + houseWidth * i, rect[1]))
                    else:
                        board.blit(imgMod.space_modifier('house.jpg', houseWidth, rect[3], 0), (rect[0] + houseWidth * i, rect[1]))
        elif self.spaceName in ["Jigglypuff", "Mewtwo", "Incineroar", "Young Link", "Toon Link", "Link", "Ryu", "Terry", "Kazuya", "Pyra", "Mythra"]:
            houseHeight = rect[3]/4
            if self.numHouses == 5:
                board.blit(imgMod.space_modifier('hotel.jpg', rect[2], houseHeight, 0), (rect[0], rect[1]))
            else:
                for i in range(self.numHouses):
                    if i == 0:
                        board.blit(imgMod.space_modifier('house.jpg', rect[2], houseHeight, 0), (rect[0], rect[1] + houseHeight * i))
                    else:
                        board.blit(imgMod.space_modifier('house.jpg', rect[2], houseHeight, 0), (rect[0], rect[1] + houseHeight * i))
                        
    def partOfMonopoly(self):
        check = 0
        if self.spaceName in ["Ganondorf", "Little Mac"]:
            for space in self.owner.properties:
                if space.spaceName == "Ganondorf":
                    check += 1
                elif space.spaceName == "Little Mac":
                    check += 1
            if check == 2:
                return True
            else: 
                return False
        elif self.spaceName in ["King Dedede", "Kirby", "Meta Knight"]:
            for space in self.owner.properties:
                if space.spaceName == "Meta Knight":
                    check += 1
                elif space.spaceName == "Kirby":
                    check += 1
                elif space.spaceName == "King Dedede":
                    check += 1
            if check == 3:
                return True
            else: 
                return False
        elif self.spaceName in ["Jigglypuff", "Mewtwo", "Incineroar"]:
            for space in self.owner.properties:
                if space.spaceName == "Jigglypuff":
                    check += 1
                elif space.spaceName == "Mewtwo":
                    check += 1
                elif space.spaceName == "Incineroar":
                    check += 1
            if check == 3:
                return True
            else: 
                return False
        elif self.spaceName in ["Young Link", "Toon Link", "Link"]:
            for space in self.owner.properties:
                if space.spaceName == "Young Link":
                    check += 1
                elif space.spaceName == "Toon Link":
                    check += 1
                elif space.spaceName == "Link":
                    check += 1
            if check == 3:
                return True
            else: 
                return False
        elif self.spaceName in ["Falco", "Wolf", "Fox"]:
            for space in self.owner.properties:
                if space.spaceName == "Falco":
                    check += 1
                elif space.spaceName == "Wolf":
                    check += 1
                elif space.spaceName == "Fox":
                    check += 1
            if check == 3:
                return True
            else: 
                return False
        elif self.spaceName in ["Samus", "Dark Samus", "Zero Suit Samus"]:
            for space in self.owner.properties:
                if space.spaceName == "Samus":
                    check += 1
                elif space.spaceName == "Dark Samus":
                    check += 1
                elif space.spaceName == "Zero Suit Samus":
                    check += 1
            if check == 3:
                return True
            else: 
                return False
        elif self.spaceName in ["Ryu", "Ken", "Kazuya"]:
            for space in self.owner.properties:
                if space.spaceName == "Ryu":
                    check += 1
                elif space.spaceName == "Ken":
                    check += 1
                elif space.spaceName == "Kazuya":
                    check += 1
            if check == 3:
                return True
            else: 
                return False
        else:
            for space in self.owner.properties:
                if space.spaceName == "Pyra":
                    check += 1
                elif space.spaceName == "Mythra":
                    check += 1
            if check == 2:
                return True
            else: 
                return False
                    
        
            


