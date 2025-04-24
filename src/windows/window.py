from tools.positioner import Positioner
from pygame.surface import Surface


class Window:
    def __init__(self, screen_width: int, screen_height: int, tile_size: int):
        self.active = True
        self.labels = []
        self.buttons = []
        self.stickers = []

        self.grid = None
        self.positioner = Positioner((screen_width, screen_height), tile_size)

        self.create_window()

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def create_window(self):
        pass

    def draw(self, screen: Surface):
        for button in self.buttons:
            if button.exist:
                button.draw(screen)
        for label in self.labels:
            if label.exist:
                label.draw(screen)
        for sticker in self.stickers:
            sticker.draw(screen)
