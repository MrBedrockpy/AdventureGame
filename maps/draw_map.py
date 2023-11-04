import pygame

from util.array_util import *
from config import *


class DrawMapManager:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.horizontal_size = SIZE[0] // 100
        self.vertical_size = SIZE[1] // 100

    def visualize(self, matrix: list):

        if matrix is None:
            print("Map is not!")
            return None

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if is_equal(matrix[y][x], [0, 0, 0]):
                    pygame.draw.rect(self.screen, WALLS,
                                     (x * self.horizontal_size + 1, y * self.vertical_size + 1, self.horizontal_size, self.vertical_size))
                elif is_equal(matrix[y][x], [255, 255, 255]):
                    pygame.draw.rect(self.screen, TRACK,
                                     (x * self.horizontal_size + 1, y * self.vertical_size + 1, self.horizontal_size, self.vertical_size))
                elif is_equal(matrix[y][x], [40, 40, 40]):
                    pygame.draw.rect(self.screen, END_POINT,
                                     (x * self.horizontal_size + 1, y * self.vertical_size + 1, self.horizontal_size, self.vertical_size))
                elif is_equal(matrix[y][x], [60, 60, 60]):
                    pygame.draw.rect(self.screen, ENEMIES,
                                     (x * self.horizontal_size + 1, y * self.vertical_size + 1, self.horizontal_size, self.vertical_size))

    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)
