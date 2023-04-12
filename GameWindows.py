import pygame
#import pygame.freetype

class gameWindows:
    def __init__(self, screen):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0,0,0)
        self.screen = screen
    def playerSelectWindow(self):
        titleFont = pygame.font.SysFont(None, 40)
        title = titleFont.render("Click Number of Players", True, self.WHITE)
        titleRect = title.get_rect(center = (500, 100))
        normalFont = pygame.font.SysFont(None, 25)

        buttonDimensions = (75, 75)
        buttonPadding = 25
        buttonArea = 3 * (buttonDimensions[0] + buttonPadding)
        startPos = (425 - buttonArea /2, 300)

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
        font = pygame.font.SysFont(None, 25)
        input_box_rect = pygame.Rect(250, 333, 500, 50)
        input_box_color = self.WHITE
        input_text_color = self.BLACK
        input_text = ""
        input_active = True
        namesAdded = []

        # Set up the submit button
        submit_button_rect = pygame.Rect(450, 666, 100, 50)
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

        # Quit Pygame cleanly
        pygame.quit()
