import config
from maps.draw_map import DrawMapManager
from player.player import Player
from util.scanner import Scanner
from util.array_util import is_equal

import pygame


class Game:

    def __init__(self):
        self.map = None
        self.player = None
        self.start_player_pos = [0, 0]
        self.victory_point_pos = [0, 0]
        self.enemies = []
        pygame.init()
        self.screen = pygame.display.set_mode(config.SIZE)

    def start(self, level: str):
        visual_map = DrawMapManager(self.screen)

        self.map = Scanner.scanner(level)

        if self.map is None:
            return None

        self.search_entity()

        self.player = Player(self.map, self.start_player_pos.copy())

        run = True

        while run:

            if self.is_quit():
                run = False
                return False

            self.player.move()

            self.contact_enemy()

            if self.is_victory():
                run = False
                return True

            visual_map.visualize(self.map)

            self.player.draw(self.screen)

            visual_map.update()

    def search_entity(self):

        there_is_player = False

        for y in range(len(self.map)):
            for x in range(len(self.map[y])):

                if is_equal(self.map[y][x], [40, 40, 40]):
                    self.victory_point_pos = [x, y]

                elif is_equal(self.map[y][x], [20, 20, 20]):
                    self.map[y][x] = [255, 255, 255]
                    self.start_player_pos = [x, y]
                    there_is_player = True

                elif is_equal(self.map[y][x], [60, 60, 60]):
                    self.enemies.append([x, y])

        if not there_is_player:
            print("Set default position of player!")

    def is_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def contact_enemy(self, ):
        for enemy in self.enemies:
            if is_equal(self.player.pos, enemy):
                self.player.pos = self.start_player_pos.copy()

    def is_victory(self) -> bool:
        if is_equal(self.victory_point_pos, self.player.pos):
            return True
        return False
