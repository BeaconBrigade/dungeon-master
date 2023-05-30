import pygame
from asset_manager import AssetManager
from entity import Entity


class Map:
    TILE_MAP = {
        "s": AssetManager.load_texture("floor.png"),
        "w": AssetManager.load_texture("wall.png"),
    }
    map: list[list[str]]

    def __init__(self, map_name: str):
        """Create a map with a map file name (located within assets/maps)"""
        self.text_source = AssetManager.load_map(map_name)

        self.map = []
        rows = 0
        cols = 0
        for line in self.text_source.splitlines():
            rows += 1
            tmp_cols = 0
            row = []
            for c in line:
                if c.isspace():
                    continue
                if c in Map.TILE_MAP.keys():
                    tmp_cols += 1
                    row.append(c)
                else:
                    raise InvalidMapFile()
            cols = max(cols, tmp_cols)
            self.map.append(row)

        self.rows = rows
        self.cols = cols

    def dimensions(self) -> (int, int):
        return self.cols * 64, self.rows * 64

    def draw(self, view: pygame.surface.Surface, relative_pos: (int, int)):
        """Draws the map to `view` and draws the"""
        map_x, map_y = self.dimensions()
        p_x, p_y = relative_pos
        # for each tile
        for i in range(0, map_x, 64):
            for j in range(0, map_y, 64):
                try:
                    letter = self.map[j // 64][i // 64]
                    draw_x, draw_y = i - p_x, j - p_y
                    view.blit(Map.TILE_MAP[letter], (draw_x, draw_y))
                # this is a blank spot on the map
                except IndexError:
                    continue

    def tile_at(self, pixel: (int, int)) -> str | None:
        map_x, map_y = self.dimensions()
        print('map\t\t\t\t', map_x, map_y)
        x = (pixel[0] + map_x // 2) - 2
        y = pixel[1] + map_y // 2
        print('adjusted\t\t', x, y)
        try:
            return self.map[y // 64][x // 64]
        except IndexError:
            return None

    def update(self, entity_list: list[Entity]):
        pass


class InvalidMapFile(Exception):
    pass
