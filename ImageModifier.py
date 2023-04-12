import pygame

class ImageModifier:

    def space_modifier(self, imageName, xScale, yScale, degreesRotated):
        img = pygame.image.load(imageName).convert()
        img = pygame.transform.scale(img, (xScale, yScale))
        img = pygame.transform.rotate(img, degreesRotated)
        return img