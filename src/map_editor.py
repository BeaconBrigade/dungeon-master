import os
import sys
import pygame

from map import Map, InvalidMapFile
from pathlib import Path

WIDTH = 800
HEIGHT = 800


def main():
    pygame.init()

    screen = pygame.display.set_mode(size=[WIDTH, HEIGHT], flags=pygame.RESIZABLE)
    clock = pygame.time.Clock()

    map_name = sys.argv[1] if len(sys.argv) == 2 else "level_one.txt"
    map_path = Path(__file__).parent / ".." / "assets" / "maps" / map_name
    level_map = Map(map_name)
    pygame.display.set_caption(f"Map Editor - {map_name}")

    modified_time = os.stat(map_path).st_mtime

    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # hot reload map
        tmp_time = os.stat(map_path).st_mtime
        if tmp_time != modified_time:
            print(f"Hot reloading {map_name}")
            modified_time = tmp_time
            try:
                level_map = Map(map_name)
            except InvalidMapFile:
                print("Hot reloaded map was invalid")

        # fill background
        screen.fill((50, 50, 50))
        level_map.draw(screen, (0, 0))

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
