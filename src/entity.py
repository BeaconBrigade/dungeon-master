import pygame


class Entity(pygame.sprite.Sprite):
    position: list[int]
    vector: list[int]
    max_speed: int
    current_speed: list[int]
    acceleration: int

    def __init__(self):
        super().__init__()

    def update(self, entity_list: list['Entity']):
        print("update not implemented")

    def draw(self, view: pygame.surface.Surface, relative_pos: (int, int)):
        print("draw not implemented")
