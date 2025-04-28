import pygame

class MyFont(pygame.font.Font):
    def __init__(self, name: str, pt_size: int):
        font_path = pygame.font.match_font(name)
        super().__init__(font_path, pt_size)
        self.pt_size = pt_size

    def get_pt_size(self) -> int:
        return self.pt_size