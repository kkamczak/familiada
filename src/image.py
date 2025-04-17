import pygame
from tools.support import import_image, scale_image


class Image(pygame.sprite.Sprite):
    def __init__(self, position: tuple, path: str, size: tuple):
        super().__init__()

        # Image:
        self.position = position
        self.image = None
        self.rect = None
        self.set_image(path, size)

    def set_image(self, path: str, size: tuple) -> None:
        self.image = import_image(path)
        self.image = scale_image(self.image, size)
        self.rect = self.image.get_rect(topleft=self.position)

    def set_alpha(self, alpha):
        self.image.set_alpha(alpha)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
