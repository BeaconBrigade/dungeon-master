import pygame
from map import Map
from player import Player
from enemy import Enemy

WIDTH = 800
HEIGHT = 800


def main():
    pygame.init()

    screen = pygame.display.set_mode(size=[WIDTH, HEIGHT], flags=pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dungeon Master")

    level_map = Map("level_one.txt")
    win_x, win_y = screen.get_size()
    player_x, player_y = 0, 0
    player = Player(win_x // 2, win_y // 2, player_x, player_y)
    enemy = Enemy()
    entity_list = [level_map, player, enemy]

    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.vector[0] = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.vector[0] = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.vector[1] = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.vector[1] = 1
        if (
            not keys[pygame.K_LEFT]
            and not keys[pygame.K_a]
            and not keys[pygame.K_RIGHT]
            and not keys[pygame.K_d]
        ):
            player.vector[0] = 0
        if (
            not keys[pygame.K_UP]
            and not keys[pygame.K_w]
            and not keys[pygame.K_DOWN]
            and not keys[pygame.K_s]
        ):
            player.vector[1] = 0

        # fill background
        screen.fill((50, 50, 50))

        # update entities
        for entity in entity_list:
            entity.update(entity_list)
            entity.draw(screen, player.position)

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
