import pygame
import sys
from tools.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, LIGHT_GREY, WHITE, FPS_SHOW, FONT_FPS
from tools.support import show_fps
from main_window import MainWindow


class Program:
    def __init__(self, screen, clock) -> None:
        # Overworld creation
        self.screen = screen
        self.clock = clock
        self.main_window = MainWindow()

    def loop(self) -> None:
        self.main_window.run(self.screen)
        if FPS_SHOW:
            show_fps(self.screen, self.clock.get_fps(), FONT_FPS, WHITE, (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 25))


    @staticmethod
    def exit_program() -> None:
        pygame.quit()
        sys.exit()


def start_game():
    # Pygame setup
    pygame.init()
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    # Start game:
    program = Program(screen, clock)

    # Game loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program.exit_program()

        screen.fill(LIGHT_GREY)
        program.loop()
        pygame.display.update()

        clock.tick(FPS)
