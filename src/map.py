import pygame
from asset_manager import AssetManager


class Map:
    TILE_MAP = {
        's': AssetManager.load_texture('floor.png'),
        'w': AssetManager.load_texture('wall.png'),
    }

    def __init__(self, map_name: str):
        """ Create a map with a map file name (located within assets/maps) """
        self.text_source = AssetManager.load_map(map_name)

        self.map = []
        for line in self.text_source.splitlines():
            row = []
            for c in line:
                if c.isspace():
                    continue
                if c in Map.TILE_MAP.keys():
                    row.append(c)
                else:
                    raise InvalidMapFile()
            self.map.append(row)

    def draw(self, view: pygame.surface.Surface, relative_pos):
        """ Draws the map to `view` and draws the """
        win_x, win_y = view.get_size()
        # tiles_x = win_x / 64
        # tiles_y = win_y / 64
        # for each tile
        for i in range(0, win_x, 64):
            for j in range(0, win_y, 64):
                letter = self.map[i // 64][j // 64]
                view.blit(Map.TILE_MAP[letter], (i, j))

        # view.blit(Map.TILE_MAP[tile], (x, y), (cx, cy, 64, 64))


class InvalidMapFile(Exception):
    pass
