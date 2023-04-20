import pygame

class ImageModifier:

    def space_modifier(self, imageName, xScale, yScale, degreesRotated):
        img = pygame.image.load(imageName).convert()
        img = pygame.transform.scale(img, (xScale, yScale))
        if degreesRotated != 0:
            img = pygame.transform.rotate(img, degreesRotated)
        return img
    
    def combineTextAndImage(self, board, imageName, xScale, yScale, font, name, costStr, nameCoord, costCoord, imgCoord):
        BLACK = (0, 0, 0)
        img = self.space_modifier(imageName, xScale, yScale, 0)
        text = font.render(name, True, BLACK)
        text2 = font.render(costStr, True, BLACK)
        rect = text.get_rect()
        rect2 = text2.get_rect()
        rect.center = nameCoord
        rect2.center = costCoord
        board.blit(text, rect)
        board.blit(img, imgCoord)
        board.blit(text2, rect2)