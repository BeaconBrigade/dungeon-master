import pygame
from map import Map


def main():
    run_game()


WIDTH = 768
HEIGHT = 768


def run_game():
    pygame.init()

    screen = pygame.display.set_mode(size=[WIDTH, HEIGHT])
    clock = pygame.time.Clock()

    level_map = Map('level_one.txt')

    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            running = handle_event(event)

        # fill background
        screen.fill((255, 255, 255))
        level_map.draw(screen, (0, 0))

        pygame.display.flip()
        clock.tick(30)


def handle_event(event: pygame.event.Event) -> bool:
    """
    Handle each event.
    Returns: whether the game should continue
    """
    if event.type == pygame.QUIT:
        return False
    return True


if __name__ == '__main__':
    main()
