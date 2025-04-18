import pygame
from tools.support import scale_image, import_image


class Sticker(pygame.sprite.Sprite):
    def __init__(self, kind: str, position: tuple, size: tuple, visible: bool):
        super().__init__()

        # Type of label
        self.kind = kind

        # Image:
        self.position = position
        self.image = None
        self.size = size
        self.rect = None
        self.set_image()
        self.visible = visible

    def set_image(self) -> None:
        file = self.kind
        if 'small_x' in file: file = 'small_x'
        self.image = import_image(f'content/ui/stickers/{file}.png')
        self.image = scale_image(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.position)

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect.topleft)

