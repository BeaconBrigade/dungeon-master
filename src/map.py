import pygame
from asset_manager import AssetManager


class Map:
    TILE_MAP = {
        "s": AssetManager.load_texture("floor.png"),
        "w": AssetManager.load_texture("wall.png"),
    }

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

    def draw(self, view: pygame.surface.Surface, player_pos: (int, int)):
        """Draws the map to `view` and draws the"""
        win_x, win_y = view.get_size()
        map_x, map_y = self.dimensions()
        p_x, p_y = player_pos
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

        """
        win_x, win_y = view.get_size()
        rel_x, rel_y = relative_pos
        rel_x -= win_x // 2
        rel_y -= win_y // 2
        # for each tile
        for i in range(rel_x - win_x // 2, min(rel_x + win_x // 2, self.cols * 64), 64):
            for j in range(rel_y - win_y // 2, min(rel_y + win_y // 2, self.rows * 64), 64):
                try:
                    letter = self.map[j // 64][i // 64]
                    view.blit(Map.TILE_MAP[letter], (i, j))
                # this is a blank spot on the map
                except IndexError:
                    continue
        """


class InvalidMapFile(Exception):
    pass
