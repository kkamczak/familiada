from managers.buttons_manager import ButtonsManager
from data.game_data import MAIN_WINDOW_PLAN as PLAN
from data.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, FONT_ROUND, WHITE, SHOW_GRID, DB_PATH
from tools.support import load_background, now, show_rounds
from tools.positioner import Positioner
from tools.grid import Grid
from windows.main_menu import MainMenu
from windows.game import Game
from windows.final import Final


class MainWindow:
    def __init__(self):
        self.background = load_background((SCREEN_WIDTH, SCREEN_HEIGHT), 'content/ui/wallpaper.png')
        self.main_menu = MainMenu(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE)
        self.game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE)
        self.final = Final(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, self.game.round_manager)

        self.windows = {
            'Main Menu': self.main_menu,
            'Game': self.game,
            'Final': self.final
        }
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

    def open_game_window(self):
        if not self.windows['Game'].finished:
            self.switch_window('Game')
        else:
            self.switch_window('Final')

    def pause_game(self) -> None:
        self.switch_window('Main Menu')
        buttons = self.windows['Main Menu'].buttons
        for button in buttons:
            if button.kind == 'start':
                button.text = 'Wznów'

    def go_final(self):
        self.switch_window('Final')
        self.windows['Final'].transfer_points()
    def elements_update(self):
        def check(buttons):
            for button in buttons:
                if button.check_click() and self.allow_click:
                    self.buttons_manager.check_action(button)
                    self.clicked()
        for name, window in self.windows.items():
            if window is None:
                continue
            elif window.active:
                if name == 'Final' and window.answer_window.active:
                    check(window.answer_window.buttons)
                else:
                    check(window.buttons)

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
        if self.windows['Game'].active or self.windows['Final']:
            show_rounds(screen, self.windows['Game'].round_manager.index, FONT_ROUND,
                        WHITE, Positioner.position(PLAN['round'][0], TILE_SIZE))


    def run(self, screen):
        self.click_timer()
        self.elements_update()
        self.draw(screen)

