import pygame
class Block():
    def __init__(self, color, gridxPosition, gridyPosition):
        self.gridxPosition = int(gridxPosition)
        self.gridyPosition = int(gridyPosition)
        self.color = color
        self.size = 25

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.gridxPosition*self.size, self.gridyPosition*self.size, self.size-1, self.size-1], 0)