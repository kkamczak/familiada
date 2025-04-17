import pygame
from tools.support import draw_text, scale_image, import_image, now
from tools.settings import WHITE, BUTTON_BASIC_COLOR, BLACK, GREEN, RED, TURQ, GOLD


class Label(pygame.sprite.Sprite):
    def __init__(self, kind: str, position: tuple, text: str, font: pygame.font.SysFont, background: bool, size: tuple):
        super().__init__()

        # Type of label
        self.kind = kind

        # Image:
        self.color_basic = BUTTON_BASIC_COLOR
        self.position = position
        self.image = None
        self.size = size
        self.rect = None
        self.set_image(background)

        # Text on button:
        self.text = text
        self.font = font
        self.mask_color = None
        self.mask = None
        self.mask_time = None

    def set_image(self, background: bool) -> None:
        file = 'label'
        if background:
            self.image = import_image(f'content/ui/labels/{file}.png')
            self.image = scale_image(self.image, self.size)
            self.rect = self.image.get_rect(topleft=self.position)
        else:
            self.rect = pygame.rect.Rect(self.position, self.size)
            self.rect.center = self.position

    def update(self, text: str) -> None:
        self.text = text

    def show_mask(self, kind: str) -> None:
        if self.mask is not None:
            return
        self.mask = pygame.surface.Surface(self.size)
        if kind == 'green':
            self.mask.fill(GREEN)
        elif kind == 'gold':
            self.mask.fill(GOLD)
        elif kind == 'white':
            self.mask.fill(TURQ)
        elif kind == 'red':
            self.mask.fill(RED)
        else:
            return

        self.mask.set_alpha(70)
        self.mask_time = now()
        self.mask_color = kind

    def check_mask(self) -> None:
        if self.mask_color == 'green' or self.mask_color == 'white':
            if now() - self.mask_time > 3000:
                self.mask = None
        elif self.mask_color == 'gold':
            if now() - self.mask_time > 6000:
                self.mask = None

    def draw(self, screen):
        color = BLACK
        if self.image is not None:
            screen.blit(self.image, self.rect.topleft)
            color = WHITE
        draw_text(screen, self.text, self.font, color, self.rect.centerx, self.rect.centery)
        self.check_mask()
        if self.mask is not None:
            screen.blit(self.mask, self.rect.topleft)
