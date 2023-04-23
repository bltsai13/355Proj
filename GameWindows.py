import pygame
from ImageModifier import ImageModifier

class gameWindows:
    def __init__(self, screen):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0,0,0)
        self.screen = screen
    def playerSelectWindow(self):
        titleFont = pygame.font.SysFont(None, 40)
        title = titleFont.render("Click Number of Players", True, self.WHITE)
        titleRect = title.get_rect(center = (250, 100))
        normalFont = pygame.font.SysFont(None, 24)

        buttonDimensions = (50, 50)
        buttonPadding = 25
        buttonArea = 3 * (buttonDimensions[0] + buttonPadding)
        startPos = (175 - buttonArea /2, 150)

        options = []
        for i in range(2,5):
            buttonSpace = pygame.Rect(startPos[0] + (buttonDimensions[0] + buttonPadding) * (i-1), startPos[1], buttonDimensions[0], buttonDimensions[1])
            surface = pygame.Surface(buttonSpace.size)
            surface.fill((255, 0, 0) if buttonSpace.collidepoint(pygame.mouse.get_pos()) else (255, 255, 255))
            button_text = normalFont.render(str(i), True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=surface.get_rect().center)
            surface.blit(button_text, button_text_rect)
            options.append((buttonSpace, i))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for button_rect, num_players in options:
                        if button_rect.collidepoint(mouse_pos):
                            return num_players
            self.screen.fill((0, 0, 0))
            self.screen.blit(title, titleRect)
            for button_rect, _ in options:
                pygame.draw.rect(self.screen, (255, 255, 255), button_rect)
            for button_rect, num_players in options:
                button_surf = pygame.Surface(button_rect.size)
                button_surf.fill((255, 0, 0) if button_rect.collidepoint(pygame.mouse.get_pos()) else (255, 255, 255))
                button_text = normalFont.render(str(num_players), True, (0, 0, 0))
                button_text_rect = button_text.get_rect(center=button_surf.get_rect().center)
                button_surf.blit(button_text, button_text_rect)
                self.screen.blit(button_surf, button_rect)
            pygame.display.update()
            pygame.time.Clock().tick(60)

    def playerNamesScreen(self, num_players):
        font = pygame.font.SysFont(None, 20)
        input_box_rect = pygame.Rect(125, 150, 250, 50)
        input_box_color = self.WHITE
        input_text_color = self.BLACK
        input_text = ""
        input_active = True
        namesAdded = []

        # Set up the submit button
        submit_button_rect = pygame.Rect(200, 225, 100, 50)
        submit_button_color = pygame.Color("green")

        # Set up the loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if submit button was clicked
                    if submit_button_rect.collidepoint(event.pos):
                        print("User entered:", input_text)
                        namesAdded.append(input_text)
                        if len(namesAdded) == num_players:
                            running = False
                            print("returning from function")
                            return namesAdded
                elif event.type == pygame.KEYDOWN:
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            print("User entered:", input_text)
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode

            # Fill the screen
            self.screen.fill(pygame.Color("gray"))

            # Render the input box
            #Text
            topText = font.render("Enter a name and click Submit for each player", True, (0,0,0))
            topTextRect = topText.get_rect()
            topTextRect.center = (250, 75)
            self.screen.blit(topText, topTextRect)
            input_box_surf = pygame.Surface(input_box_rect.size)
            input_box_surf.fill(input_box_color)
            input_box_surf.set_alpha(200)
            self.screen.blit(input_box_surf, input_box_rect)
            pygame.draw.rect(self.screen, input_text_color, input_box_rect, 2)
            input_text_surf = font.render(input_text, True, input_text_color)
            input_text_rect = input_text_surf.get_rect(center=input_box_rect.center)
            self.screen.blit(input_text_surf, input_text_rect)

            # Render the submit button
            pygame.draw.rect(self.screen, submit_button_color, submit_button_rect)
            submit_text_surf = font.render("Submit", True, pygame.Color("white"))
            submit_text_rect = submit_text_surf.get_rect(center=submit_button_rect.center)
            self.screen.blit(submit_text_surf, submit_text_rect)

            pygame.display.flip()

        pygame.quit()
        
    def createBoard(self, font, players, drawPiles, activePlayer):
        imageModifier = ImageModifier()
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BROWN = (165, 42, 42)
        LIGHTBLUE = (168, 255, 255)
        MAGENTA = (250, 45, 208)
        ORANGE = (255, 127, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        BLUE = (0, 0, 255)
        GREEN = (0, 53, 24)
        DARKBLUE = (0, 0, 255)
        LIGHTGREEN = (191, 219, 174)
        pygame.draw.rect(self.screen, LIGHTGREEN, [0, 0, 1000, 1000])
        pygame.draw.rect(self.screen, BLACK, [0, 0, 140, 140], 1)
        pygame.draw.rect(self.screen, BLACK, [860, 860, 140, 140], 1)
        pygame.draw.rect(self.screen, BLACK, [0, 860, 140, 140], 1)
        pygame.draw.rect(self.screen, BLACK, [860, 0, 140, 140], 1)
        for i in range(0, 9):
            pygame.draw.rect(self.screen, BLACK, [0, 140 + i*80, 140, 80], 1)
            pygame.draw.rect(self.screen, BLACK, [140 + i*80, 0, 80, 140], 1)
            pygame.draw.rect(self.screen, BLACK, [860, 140 + i*80, 140, 80], 1)
            pygame.draw.rect(self.screen, BLACK, [140 + i*80, 860, 80, 140], 1)

        pygame.draw.rect(self.screen, BROWN, [782, 860, 76, 20])
        pygame.draw.rect(self.screen, BROWN, [622, 860, 76, 20])
        pygame.draw.rect(self.screen, LIGHTBLUE, [142, 860, 76, 20])
        pygame.draw.rect(self.screen, LIGHTBLUE, [222, 860, 76, 20])
        pygame.draw.rect(self.screen, LIGHTBLUE, [382, 860, 76, 20])
        pygame.draw.rect(self.screen, MAGENTA, [120, 782, 20, 76])
        pygame.draw.rect(self.screen, MAGENTA, [120, 622, 20, 76])
        pygame.draw.rect(self.screen, MAGENTA, [120, 542, 20, 76])
        pygame.draw.rect(self.screen, ORANGE, [120, 142, 20, 76])
        pygame.draw.rect(self.screen, ORANGE, [120, 222, 20, 76])
        pygame.draw.rect(self.screen, ORANGE, [120, 382, 20, 76])
        pygame.draw.rect(self.screen, RED, [142, 120, 76, 20])
        pygame.draw.rect(self.screen, RED, [302, 120, 76, 20])
        pygame.draw.rect(self.screen, RED, [382, 120, 76, 20])
        pygame.draw.rect(self.screen, YELLOW, [542, 120, 76, 20])
        pygame.draw.rect(self.screen, YELLOW, [622, 120, 76, 20])
        pygame.draw.rect(self.screen, YELLOW, [782, 120, 76, 20])
        pygame.draw.rect(self.screen, GREEN, [860, 142, 20, 76])
        pygame.draw.rect(self.screen, GREEN, [860, 222, 20, 76])
        pygame.draw.rect(self.screen, GREEN, [860, 382, 20, 76])
        pygame.draw.rect(self.screen, DARKBLUE, [860, 622, 20, 76])
        pygame.draw.rect(self.screen, DARKBLUE, [860, 782, 20, 76])
        
        imageModifier.combineTextAndImage(self.screen, 'littleMac.png', 70, 90, font, 'Little Mac', '$60', (660, 890), (655, 985), (625, 895))
        imageModifier.combineTextAndImage(self.screen, 'ganon.png', 55, 85, font, 'Ganondorf', '$60', (820, 890), (815, 985), (790, 895))
        imageModifier.combineTextAndImage(self.screen, 'dedede.png', 60, 85, font, 'King Dedede', '$100', (420, 890), (415, 985), (385, 895))
        imageModifier.combineTextAndImage(self.screen, 'kirby.png', 50, 75, font, 'Kirby', '$100', (255, 890), (255, 985), (235, 900))
        imageModifier.combineTextAndImage(self.screen, 'Meta Knight.png', 60, 85, font, 'Meta Knight', '$120', (180, 890), (175, 985), (150, 895))
        
        self.screen.blit(imageModifier.space_modifier('jigglypuff.png', 70, 105, 270), (10, 785))
        self.screen.blit(imageModifier.space_modifier('pacman.png', 70, 105, 270), (10, 705))
        self.screen.blit(imageModifier.space_modifier('mewtwo.png', 70, 105, 270), (10, 625))
        self.screen.blit(imageModifier.space_modifier('incineroar.png', 70, 105, 270), (10, 545))
        self.screen.blit(imageModifier.space_modifier('ike.png', 70, 105, 270), (10, 465))
        self.screen.blit(imageModifier.space_modifier('yLink.png', 70, 105, 270), (10, 385))
        self.screen.blit(imageModifier.space_modifier('tLink.png', 70, 105, 270), (10, 225))
        self.screen.blit(imageModifier.space_modifier('link.png', 70, 105, 270), (10, 145))
        self.screen.blit(imageModifier.space_modifier('falco.png', 70, 105, 180), (145, 10))
        self.screen.blit(imageModifier.space_modifier('wolf.png', 70, 105, 180), (305, 10))
        self.screen.blit(imageModifier.space_modifier('fox.png', 70, 105, 180), (385, 10))
        self.screen.blit(imageModifier.space_modifier('roy.png', 70, 105, 180), (465, 10))
        self.screen.blit(imageModifier.space_modifier('samus.png', 60, 105, 180), (550, 10))
        self.screen.blit(imageModifier.space_modifier('darkSamus.png', 65, 105, 180), (630, 10))
        self.screen.blit(imageModifier.space_modifier('g&w.png', 65, 105, 180), (710, 10))
        self.screen.blit(imageModifier.space_modifier('zss.png', 65, 105, 180), (790, 10))
        self.screen.blit(imageModifier.space_modifier('ryu.png', 70, 105, 90), (885, 145))
        self.screen.blit(imageModifier.space_modifier('terry.png', 70, 105, 90), (885, 225))
        self.screen.blit(imageModifier.space_modifier('byleth.png', 70, 120, 90), (870, 465))
        self.screen.blit(imageModifier.space_modifier('kazuya.png', 70, 105, 90), (885, 385))
        self.screen.blit(imageModifier.space_modifier('pyra.png', 70, 105, 90), (885, 625))
        self.screen.blit(imageModifier.space_modifier('steve.png', 70, 115, 90), (870, 705))
        self.screen.blit(imageModifier.space_modifier('mythra.png', 70, 105, 90), (885, 785))
        imageModifier.combineTextAndImage(self.screen, 'marth.png', 70, 75, font, 'Marth', '$200', (500, 885), (500, 985), (465, 895))
        imageModifier.combineTextAndImage(self.screen, 'dkFace.png', 60, 75, font, 'Low Tier Tax', 'Pay $200', (580, 890), (575, 985), (550, 895))
        
        self.screen.blit(imageModifier.space_modifier('monopolyCenter.png', 720, 720, 0), (140, 140))
        self.screen.blit(imageModifier.space_modifier('goToJail.png', 138, 138, 0), (860, 0))
        self.screen.blit(imageModifier.space_modifier('go.png', 140, 140, 0), (860, 860))
        self.screen.blit(imageModifier.space_modifier('freeParking.png', 140, 140, 0), (0, 0))
        self.screen.blit(imageModifier.space_modifier('jail.png', 140, 140, 0), (0, 860))
        self.screen.blit(imageModifier.space_modifier('assistTrophyWithText.png', 70, 85, 0), (305, 895))
        self.screen.blit(pygame.transform.rotate(imageModifier.space_modifier('assistTrophyWithText.png', 70, 85, 0), 180), (225, 30))
        self.screen.blit(pygame.transform.rotate(imageModifier.space_modifier('assistTrophyWithText.png', 70, 85, 0), 90), (885, 545))
        self.screen.blit(imageModifier.space_modifier('pokeBallWithText.png', 65, 80, 0), (705, 890))
        self.screen.blit(pygame.transform.rotate(imageModifier.space_modifier('pokeBallWithText.png', 65, 80, 0), 90), (880, 310))
        self.screen.blit(pygame.transform.rotate(imageModifier.space_modifier('pokeBallWithText.png', 65, 80, 0), 270), (40, 310))
        
        pygame.draw.rect(self.screen, WHITE, [160, 420, 150, 75])
        p1Text = font.render(players[0].playerName, True, BLACK)
        p1Cash = font.render("Cash: " + str(players[0].money), True, BLACK)
        self.screen.blit(p1Text, (170, 430))
        self.screen.blit(p1Cash, (170, 450))       
        pygame.draw.rect(self.screen, WHITE, [700, 420, 150, 75])
        p2Text = font.render(players[1].playerName, True, BLACK)
        self.screen.blit(p2Text, (710, 430))
        p2Cash = font.render("Cash: " + str(players[1].money), True, BLACK)
        self.screen.blit(p2Cash, (710, 450))
        if len(players) >= 3:
            pygame.draw.rect(self.screen, WHITE, [160, 500, 150, 75])
            p3Text = font.render(players[2].playerName, True, BLACK)
            p3Cash = font.render("Cash: " + str(players[2].money), True, BLACK)
            self.screen.blit(p3Text, (170, 510))
            self.screen.blit(p3Cash, (170, 530))
            if len(players) >= 4:
                pygame.draw.rect(self.screen, WHITE, [700, 500, 150, 75])
                p4Text = font.render(players[3].playerName, True, BLACK)
                self.screen.blit(p4Text, (710, 510))
                p4Cash = font.render("Cash: " + str(players[3].money), True, BLACK)
                self.screen.blit(p4Cash, (710, 530))
        players[0].getNewBoardPos(self.screen, players[0], 0, players, drawPiles, activePlayer, (0,0))
        players[1].getNewBoardPos(self.screen, players[1], 1, players, drawPiles, activePlayer, (0,0))
        if len(players) >= 3:
            players[2].getNewBoardPos(self.screen, players[2], 2, players, drawPiles, activePlayer, (0,0))
            if len(players) == 4:
                players[3].getNewBoardPos(self.screen, players[3], 3, players, drawPiles, activePlayer, (0,0))
        posList = []
        posList.append([860, 860, 140, 140])
        for i in range(8,-1, -1):
            posList.append([140 + i*80, 860, 80, 140])
        posList.append([0, 860, 140, 140])
        for i in range(8, -1, -1):
            posList.append([0, 140+80*i, 140, 80])
        posList.append([0, 0, 140, 140])
        for i in range(0, 9):
            posList.append([140+i*80, 0, 80, 140])
        posList.append([860, 0, 140, 140])
        for i in range(0, 9):
            posList.append([860, 140+i*80, 140, 80])
        for i in range(len(players[0].spaces)):
                players[0].spaces[i].setOwnerOutline(self.screen, players, posList[i])
        for space in players[0].spaces:
            rect = []
            if space.spaceName == "Ganondorf":
                rect = [782, 860, 76, 20]
            elif space.spaceName == "Little Mac":
                rect = [622, 860, 76, 20]
            elif space.spaceName == "King Dedede":
                rect = [382, 860, 76, 20]
            elif space.spaceName == "Kirby":
                rect = [222, 860, 76, 20]
            elif space.spaceName == "Meta Knight":
                rect = [142, 860, 76, 20]
            elif space.spaceName == "Jigglypuff":
                rect = [120, 782, 20, 76]
            elif space.spaceName == "Mewtwo":
                rect = [120, 622, 20, 76]
            elif space.spaceName == "Incineroar":
                rect = [120, 542, 20, 76]
            elif space.spaceName == "Young Link":
                rect = [120, 382, 20, 76]
            elif space.spaceName == "Toon Link":
                rect = [120, 222, 20, 76]
            elif space.spaceName == "Link":
                rect = [120, 142, 20, 76]
            elif space.spaceName == "Falco":
                rect = [142, 120, 76, 20]
            elif space.spaceName == "Wolf":
                rect = [302, 120, 76, 20]
            elif space.spaceName == "Fox":
                rect = [382, 120, 76, 20]
            elif space.spaceName == "Samus":
                rect = [542, 120, 76, 20]
            elif space.spaceName == "Dark Samus":
                rect = [622, 120, 76, 20]
            elif space.spaceName == "Zero Suit Samus":
                rect = [782, 120, 76, 20]
            elif space.spaceName == "Ryu":
                rect = [860, 142, 20, 76]
            elif space.spaceName == "Terry":
                rect = [860, 222, 20, 76]
            elif space.spaceName == "Kazuya":
                rect = [860, 382, 20, 76]
            elif space.spaceName == "Pyra":
                rect = [860, 622, 20, 76]
            elif space.spaceName == "Mythra":
                rect = [860, 782, 20, 76]
            if rect != []:
                space.setHouses(self.screen, rect)
        pygame.display.update()
            
        
        
        
        
