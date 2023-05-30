import typing

import pygame
from entity import Entity
from asset_manager import AssetManager
from src.map import Map


class Player(Entity):
    def __init__(self, win_x, win_y, x, y):
        super().__init__()

        self.position = [x, y]
        self.window_pos = [win_x, win_y]
        self.vector = [0, 0]
        self.max_speed = 10
        self.current_speed = [0, 0]
        self.acceleration = 4
        self.texture = AssetManager.load_texture("player-v1.png")

    def update(self, entity_list: list[Entity]):
        # speed up or slow down depending on vector
        if self.vector[0] != 0:
            self.current_speed[0] = min(
                self.current_speed[0] + self.acceleration, self.max_speed
            )
        else:
            self.current_speed[0] = max(self.current_speed[0] - self.acceleration, 0)
        if self.vector[1] != 0:
            self.current_speed[1] = min(
                self.current_speed[1] + self.acceleration, self.max_speed
            )
        else:
            self.current_speed[1] = max(self.current_speed[1] - self.acceleration, 0)

        # update new position
        new_x = self.position[0] + self.vector[0] * self.current_speed[0]
        new_y = self.position[1] + self.vector[1] * self.current_speed[1]

        level_map = typing.cast(Map, entity_list[0])
        print('player\t\t\t', new_x, new_y)
        tile = level_map.tile_at((new_x, new_y))
        print(tile, '\n')
        # if both x + y is blocked
        if tile is None or tile == 'w':
            # if y only is blocked
            tile = level_map.tile_at((self.position[0], new_y))
            if tile is None or tile == 'w':
                # if x only is blocked
                tile = level_map.tile_at((new_x, self.position[1]))
                if tile is None or tile == 'w':
                    return
                new_y = self.position[1]
            else:
                new_x = self.position[0]

        self.position = [new_x, new_y]

    def draw(self, view: pygame.surface.Surface, relative_pos: (int, int)):
        x, y = self.window_pos
        view.blit(self.texture, (x, y))
