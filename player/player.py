from util.array_util import is_equal

import pygame


class Player:

    def __init__(self, map: pygame.Surface, pos: list[int, int], size: int, skin: str):
        self.map = map
        self.skin = skin
        self.size = size
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
        screen.blit(pygame.image.load(self.skin), (self.pos[0] * self.size + 1, self.pos[1] * self.size + 1))
