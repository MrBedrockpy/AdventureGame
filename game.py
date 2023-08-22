from maps.draw_map import DrawMapManager
from player.player import Player
from util.scanner import Scanner
from util.array_util import is_equal

import pygame


class Game:

    def __init__(self):
        self.start_player_pos = [0, 0]
        self.victory_point_pos = [0, 0]
        self.enemies = []
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 1000))

    def start(self, level: str):
        visual_map = DrawMapManager(self.screen)

        map = Scanner.scanner(level)

        if map is None:
            return None

        self.player = Player(map, self.start_player_pos, 10, "player\\skins\\skin1.png")

        run = True

        while run:

            if visual_map.is_quit():
                run = False

            self.player.move()

            self.contact_enemy()

            if self.is_vectory():
                run = False

            visual_map.visualize(map)

            self.player.draw(self.screen)

            visual_map.update()

    def search_entity(self):

        there_is_player = False

        for y in range(len(map)):
            for x in range(len(map[y])):

                if is_equal(map[y][x], [40, 40, 40]):
                    self.victory_point_pos = [x, y]

                elif is_equal(map[y][x], [20, 20, 20]):
                    map[y][x] = [255, 255, 255]
                    self.start_player_pos = [x, y]
                    there_is_player = True

                elif is_equal(map[y][x], [60, 60, 60]):
                    self.enemies.append([x, y])

        if not there_is_player:
            print("Set default position of player!")

    def contact_enemy(self, ):
        for enemy in self.enemies:
            if is_equal(self.player.pos, enemy):
                self.player.pos = self.start_player_pos

    def is_vectory(self) -> bool:
        if is_equal(self.victory_point_pos, self.start_player_pos):
            return True
        return False
