import pygame
from tools.support import draw_text, scale_image, import_image, now, puts
from data.settings import WHITE, BUTTON_BASIC_COLOR, BLACK, RED, SHOW_MASK


class Label(pygame.sprite.Sprite):
    def __init__(self, kind: str, position: tuple, text: str, font: pygame.font.SysFont, background: bool, size: tuple):
        super().__init__()

        # Type of label
        self.kind = kind

        # Image:
        self.color_basic = BUTTON_BASIC_COLOR
        self.position = position
        self.align = None
        self.image = None
        self.size = size
        self.rect = None
        self.set_image(background)

        # Text on button:
        self.text = text
        self.font = font
        self.mask = None
        self.mask_time = None

        if SHOW_MASK:
            self.show_mask()

    def set_image(self, background: bool) -> None:
        file = 'label'
        if background:
            self.image = import_image(f'content/ui/labels/{file}.png')
            self.image = scale_image(self.image, self.size)
            self.rect = self.image.get_rect(topleft=self.position)
        else:
            self.rect = pygame.rect.Rect(self.position, self.size)
            self.rect.topleft = self.position

    def update(self, text: str) -> None:
        self.text = text

    def show_mask(self) -> None:
        if self.mask is not None:
            return
        self.mask = pygame.surface.Surface(self.size)
        self.mask.fill(RED)
        self.mask.set_alpha(70)
        self.mask_time = now()

    def draw(self, screen):
        color = BLACK
        if self.image is not None:
            screen.blit(self.image, self.rect.topleft)
            color = WHITE
        if self.mask is not None:
            screen.blit(self.mask, self.rect.topleft)
        draw_text(screen, self.text, self.font, color, self.rect.centerx, self.rect.centery, size=self.size[0])