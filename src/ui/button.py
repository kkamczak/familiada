import pygame
from tools.support import draw_text, scale_image, import_image, puts, now
from data.settings import WHITE, BUTTON_BASIC_COLOR, BUTTON_ACTIVE_COLOR, RED
from data.game_data import BUTTONS_ACTION_TEXT


class Button(pygame.sprite.Sprite):
    def __init__(self, position: tuple, kind: str, text: str, font: pygame.font.SysFont, size: tuple, offset: tuple = (0, 0)):
        super().__init__()

        # Image:
        self.kind = kind
        self.color_basic = BUTTON_BASIC_COLOR
        self.color_active = BUTTON_ACTIVE_COLOR
        self.position = position
        self.image = None
        self.size = size
        self.rect = None
        self.images = self.load_images()
        self.set_image(False)

        # Text on button:
        self.text = text
        self.font = font
        if self.kind in BUTTONS_ACTION_TEXT:
            self.action_text = BUTTONS_ACTION_TEXT[self.kind]
        else:
            self.action_text = 'Ten przycisk nic nie robi...'

        # Conditions:
        self.clickable = True
        self.clicked = False
        self.show = True
        self.offset = offset
        self.mask = None
        self.mask_time = now()
        self.exist = True

    def load_images(self, file: str = "button") -> dict:

        normal_image = import_image(f'content/ui/buttons/{file}.png')
        normal_image = scale_image(normal_image, self.size)
        active_image = import_image(f'content/ui/buttons/{file}_active.png')
        active_image = scale_image(active_image, self.size)
        self.rect = normal_image.get_rect(topleft=self.position)

        images = {
            'normal': normal_image,
            'active': active_image
        }
        return images

    def set_image(self, active):
        if not active:
            self.image = self.images['normal']
        else:
            self.image = self.images['active']

    def draw(self, screen):
        if self.show:
            screen.blit(self.image, self.rect.topleft)
            draw_text(screen, self.text, self.font, WHITE, self.rect.centerx, self.rect.centery, size=self.size[0] - 10)

    def check_click(self):
        if not self.show:
            return
        if not self.clickable:
            return
        action = False

        # Get mouse position
        m_pos = pygame.mouse.get_pos()
        pos = (m_pos[0] - self.offset[0], m_pos[1] - self.offset[1])

        # Check if button active and clicked:
        if self.rect.collidepoint(pos):
            self.set_image(True)

            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.set_image(False)

        return action

    def action(self):
        puts(self.action_text)
        return self.kind


class QuestionShowButton(Button):
    def __init__(self, position: tuple, kind: str, text: str, font: pygame.font.SysFont, size: tuple):
        super().__init__(position, kind, text, font, size)
        self.images = self.load_images(self.kind)

class AnswerShowButton(Button):
    def __init__(self, position: tuple, kind: str, text: str, font: pygame.font.SysFont, size: tuple):
        super().__init__(position, kind, text, font, size)
        file = 'answer_show'
        self.images = self.load_images(file)

    def action(self) -> str:
        puts(f'Pokazuje odpowiedz nr {self.kind[-1]}...')
        return self.kind

class BlindButton(Button):
    def __init__(self, position: tuple, kind: str, text: str, font: pygame.font.SysFont, size: tuple):
        super().__init__(position, kind, text, font, size)
        self.images = self.create_blind_images()

    def create_blind_images(self) -> dict:
        normal_image = pygame.surface.Surface(self.size)
        active_image = pygame.surface.Surface(self.size)
        normal_image.fill(RED)
        active_image.fill(RED)
        normal_image.set_alpha(0)
        active_image.set_alpha(50)
        self.rect = normal_image.get_rect(topleft=self.position)

        images = {
            'normal': normal_image,
            'active': active_image
        }
        return images
