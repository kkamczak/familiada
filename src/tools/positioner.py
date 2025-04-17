import pygame
from typing import Union
from tools.settings import YELLOW, FONT_NORMAL, WHITE, GRID, GREEN, LINE
from tools.support import draw_text


class Positioner:
    def __init__(self, screen_size: tuple, tile_size: int) -> None:
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.tile_size = tile_size

        self.clicked = False

        self.start = [0, 0, 0, 0]
        self.checking = False

    def draw_lines(self, screen):
        x_pos = 0
        while x_pos < self.width:
            if x_pos == self.width / 2:
                pygame.draw.line(screen, GREEN, [x_pos, 0], [x_pos, self.height], 1)
            else:
                pygame.draw.line(screen, LINE, [x_pos, 0], [x_pos, self.height], 1)
            x_pos += self.tile_size
        y_pos = 0
        while y_pos < self.height:
            if y_pos == self.height / 2:
                pygame.draw.line(screen, GREEN, [0, y_pos], [self.width, y_pos], 1)
            else:
                pygame.draw.line(screen, LINE, [0, y_pos], [self.width, y_pos], 1)
            y_pos += self.tile_size

    def check_cursor(self, screen: pygame.surface.Surface) -> None:
        pos = pygame.mouse.get_pos()
        x_cord = int(pos[0] / self.tile_size)
        y_cord = int(pos[1] / self.tile_size)
        x_pos = self.position(x_cord, self.tile_size)
        y_pos = self.position(y_cord, self.tile_size)

        if pos[0] < 5 * self.tile_size or pos[1] < 5 * self.tile_size:
            correction = 2 * self.tile_size
        else:
            correction = -2 * self.tile_size

        if not self.checking:
            pygame.draw.rect(screen, YELLOW, (x_pos, y_pos, self.tile_size, self.tile_size))
        else:
            x_start, y_start = self.start[0], self.start[1]
            pygame.draw.rect(screen, YELLOW, (self.start[0], self.start[1], self.tile_size, self.tile_size))
            while x_start <= x_pos:
                y_start = self.start[1]
                while y_start <= y_pos:
                    pygame.draw.rect(screen, YELLOW, (x_start, y_start, self.tile_size, self.tile_size))
                    y_start += self.tile_size
                x_start += self.tile_size
            text = f'({int(self.start[0] / self.tile_size)}, {int(self.start[1] / self.tile_size)})'
            draw_text(screen, text, FONT_NORMAL, WHITE, self.start[2], self.start[3], frame=True)
            pygame.draw.rect(screen, YELLOW, (x_pos, y_pos, self.tile_size, self.tile_size))

            # Width and height:
            if x_pos > self.start[0] and y_pos > self.start[1]:
                width = x_cord + 1 - self.start[0] / self.tile_size
                height = y_cord + 1 - self.start[1] / self.tile_size
                draw_text(screen, f'Width: {width}, height: {height}', FONT_NORMAL, WHITE,
                          self.position(52, self.tile_size), self.position(2, self.tile_size), frame=True)

        draw_text(screen, f'({x_cord}, {y_cord})', FONT_NORMAL, WHITE, pos[0] + correction, pos[1] + correction, frame=True)

        if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
            self.clicked = True
            if not self.checking:
                self.start = [x_pos, y_pos, x_pos + correction, y_pos + correction]
                self.checking = True
            else:
                self.checking = False
        elif pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    def update(self, screen: pygame.surface.Surface) -> None:
        if GRID:
            self.draw_lines(screen)
            self.check_cursor(screen)

    def transform(self, positions: dict) -> dict:
        new_dict = {}
        for element in positions:
            position = self.position(positions[element][0], self.tile_size)
            size = self.position(positions[element][1], self.tile_size)
            new_dict[element] = [position, size]
        return new_dict

    @staticmethod
    def position(position: Union[int, tuple], tile_size: int) -> Union[int, tuple]:
        """
        Kalkuluje pozycje / długość w oparciu o szerkość kafelka

        :param position:
        :param tile_size:
        :return:
        """
        if isinstance(position, tuple):
            return position[0] * tile_size, position[1] * tile_size
        elif isinstance(position, int):
            return position * tile_size
        else:
            print('Function position() error...')
            return 0
