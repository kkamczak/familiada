from engine import Engine
from game_data import MAIN_WINDOW_PLAN as PLAN
from tools.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, FONT_ROUND, WHITE
from tools.support import load_background, now, show_rounds
from tools.positioner import Positioner
from main_menu import MainMenu


class MainWindow:
    def __init__(self):
        self.background = load_background((SCREEN_WIDTH, SCREEN_HEIGHT), 'content/ui/wallpaper.png')
        self.main_menu = MainMenu(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE)

        self.windows = {
            'Main Menu': self.main_menu
        }

        self.engine = Engine(self)

        self.timer = None

        # Time to allow clicking
        self.start_time = now()
        self.allow_click = False
        self.timer_length = 200

    def click_timer(self):
        if not self.allow_click:
            current_time = now()
            if current_time - self.start_time >= self.timer_length:
                self.allow_click = True

    def clicked(self):
        self.allow_click = False
        self.start_time = now()
        #self.sounds.play('click_normal')

    def elements_update(self):
        for name, window in self.windows.items():
            if window.active is True:
                for button in window.buttons:
                    if button.check_click() and self.allow_click:
                        self.engine.check_action(button)
                        self.clicked()

    def draw(self, screen):
        #screen.blit(self.background, (0, 0))
        for name, window in self.windows.items():
            if window.active is True:
                for button in window.buttons:
                     button.draw(screen)
                for label in window.labels:
                    label.draw(screen)

        if self.timer is not None:
            self.timer.draw(screen)
        show_rounds(screen, 666, FONT_ROUND, WHITE, Positioner.position(PLAN['round'][0], TILE_SIZE))

    def run(self, screen):
        self.click_timer()
        self.elements_update()
        self.draw(screen)
