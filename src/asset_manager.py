import pygame
from pathlib import Path


class AssetManager:
    ASSET_PATH = Path(__file__).parent / '..' / 'assets'

    @staticmethod
    def load_texture(name: str):
        return pygame.image.load(AssetManager.ASSET_PATH / 'textures' / name)

    @staticmethod
    def load_sound(name: str):
        return pygame.mixer.Sound(AssetManager.ASSET_PATH / 'audio' / name)

    @staticmethod
    def load_music(name: str):
        return pygame.mixer.music.load(AssetManager.ASSET_PATH / 'audio' / name)

    @staticmethod
    def load_map(name: str):
        with open(AssetManager.ASSET_PATH / 'maps' / name) as f:
            return f.read()

    @staticmethod
    def load_font(name: str, size: int):
        return pygame.font.Font(AssetManager.ASSET_PATH / 'fonts' / name, size)
