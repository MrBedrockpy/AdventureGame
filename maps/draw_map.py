import pygame

from util.array_util import *
from config import *


class DrawMapManager:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.size = 10

    def is_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def visualize(self, map: list):

        if map is None:
            print("Map is not!")
            return None

        for y in range(len(map)):
            for x in range(len(map[y])):
                if is_equal(map[y][x], [0, 0, 0]):
                    pygame.draw.rect(self.screen, (0, 0, 0),
                                     (x * self.size + 1, y * self.size + 1, self.size, self.size))
                elif is_equal(map[y][x], [255, 255, 255]):
                    pygame.draw.rect(self.screen, (255, 243, 110),
                                     (x * self.size + 1, y * self.size + 1, self.size, self.size))
                elif is_equal(map[y][x], [40, 40, 40]):
                    pygame.draw.rect(self.screen, (0, 255, 0),
                                     (x * self.size + 1, y * self.size + 1, self.size, self.size))
                elif is_equal(map[y][x], [60, 60, 60]):
                    pygame.draw.rect(self.screen, (255, 0, 0),
                                     (x * self.size + 1, y * self.size + 1, self.size, self.size))

    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)
