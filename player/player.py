import config
from util.array_util import is_equal

import pygame


class Player:

    def __init__(self, map: pygame.Surface, pos: list[int, int]):
        self.map = map
        self.horizontal_size = config.SIZE[0] // 100
        self.vertical_size = config.SIZE[1] // 100
        self.pos = pos

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if not is_equal(self.map[self.pos[1]][self.pos[0] + 1], [0, 0, 0]):
                self.pos[0] += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if not is_equal(self.map[self.pos[1]][self.pos[0] - 1], [0, 0, 0]):
                self.pos[0] -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if not is_equal(self.map[self.pos[1] + 1][self.pos[0]], [0, 0, 0]):
                self.pos[1] += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if not is_equal(self.map[self.pos[1] - 1][self.pos[0]], [0, 0, 0]):
                self.pos[1] -= 1

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, config.PLAYER, (self.pos[0] * self.horizontal_size + 1, self.pos[1] * self.vertical_size + 1, self.horizontal_size, self.vertical_size))
