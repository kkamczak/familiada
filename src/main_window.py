from managers.buttons_manager import ButtonsManager
from managers.round_manager import RoundManager
from data.game_data import MAIN_WINDOW_PLAN as PLAN
from data.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, FONT_ROUND, WHITE, SHOW_GRID, DB_PATH
from tools.support import load_background, now, show_rounds
from tools.positioner import Positioner
from tools.grid import Grid
from windows.main_menu import MainMenu
from windows.game import Game


class MainWindow:
    def __init__(self):
        self.background = load_background((SCREEN_WIDTH, SCREEN_HEIGHT), 'content/ui/wallpaper.png')
        self.main_menu = MainMenu(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE)
        self.game = None

        self.windows = {
            'Main Menu': self.main_menu,
            'Game': self.game
        }
        self.create_game_window()
        self.switch_window('Main Menu')

        self.buttons_manager = ButtonsManager(self)

        self.timer = None

        # Time to allow clicking
        self.start_time = now()
        self.allow_click = False
        self.timer_length = 200

        # Addons:
        if SHOW_GRID:
            self.grid_editor = Grid((SCREEN_WIDTH, SCREEN_HEIGHT), TILE_SIZE)

    def click_timer(self):
        if not self.allow_click:
            current_time = now()
            if current_time - self.start_time >= self.timer_length:
                self.allow_click = True

    def clicked(self):
        self.allow_click = False
        self.start_time = now()
        #self.sounds.play('click_normal')

    def switch_window(self, new_window: str)-> None:
        for name, window in self.windows.items():
            window.deactivate()
            if name == new_window:
                window.activate()

    def create_game_window(self):
        if self.game is None:
            for name, window in self.windows.items():
                if window is None:
                    continue
                else:
                    window.deactivate()
            self.game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE)
            self.windows['Game'] = self.game
        else:
            self.switch_window('Game')

    def pause_game(self) -> None:
        self.switch_window('Main Menu')
        buttons = self.windows['Main Menu'].buttons
        for button in buttons:
            if button.kind == 'start':
                button.text = 'Wznów'

    def elements_update(self):
        for window in list(self.windows.values()):
            if window is None:
                continue
            elif window.active:
                for button in window.buttons:
                    if button.check_click() and self.allow_click:
                        self.buttons_manager.check_action(button)
                        self.clicked()

    def draw(self, screen):
        #screen.blit(self.background, (0, 0))
        for name, window in self.windows.items():
            if window is None:
                continue
            elif window.active is True:
                window.draw(screen)

        if self.timer is not None:
            self.timer.draw(screen)

        if SHOW_GRID:
            self.grid_editor.update(screen)
        show_rounds(screen, 666, FONT_ROUND, WHITE, Positioner.position(PLAN['round'][0], TILE_SIZE))

    def run(self, screen):
        self.click_timer()
        self.elements_update()
        self.draw(screen)
