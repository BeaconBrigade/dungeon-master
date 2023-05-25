import pygame
from map import Map


def main():
    run_game()


WIDTH = 800
HEIGHT = 800


def run_game():
    pygame.init()

    screen = pygame.display.set_mode(size=[WIDTH, HEIGHT], flags=pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Dungeon Master')

    level_map = Map('level_one.txt')

    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h),
                                                 pygame.RESIZABLE)

        # fill background
        screen.fill((50, 50, 50))
        level_map.draw(screen, (0, 0))

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
