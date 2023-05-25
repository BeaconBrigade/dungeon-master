import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        print("update not implemented")

    def draw(self, view: pygame.surface.Surface):
        print("draw not implemented")
