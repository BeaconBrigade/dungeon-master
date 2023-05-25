import pygame
from map import Map
from player import Player

WIDTH = 800
HEIGHT = 800


def main():
    pygame.init()

    screen = pygame.display.set_mode(size=[WIDTH, HEIGHT], flags=pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Dungeon Master')

    level_map = Map('level_one.txt')
    player = Player()
    entity_list = [player]

    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h),
                                                 pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT | pygame.K_a:
                        player.vector[0] = -1
                    case pygame.K_RIGHT | pygame.K_d:
                        player.vector[0] = 1
                    case pygame.K_UP | pygame.K_w:
                        player.vector[1] = -1
                    case pygame.K_DOWN | pygame.K_s:
                        player.vector[1] = 1
            elif event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_LEFT | pygame.K_a | pygame.K_RIGHT | pygame.K_d:
                        player.vector[0] = 0
                    case pygame.K_UP | pygame.K_w | pygame.K_DOWN | pygame.K_s:
                        player.vector[1] = 0

            elif event.type == pygame.KEYUP:
                pass

        # fill background
        screen.fill((50, 50, 50))
        level_map.draw(screen, (0, 0))

        # update entities
        for entity in entity_list:
            entity.update()
            entity.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
