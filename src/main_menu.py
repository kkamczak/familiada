from optparse import Option
from label import Label
from button import ExitButton, OptionsButton, StartButton
from tools.positioner import Positioner
from game_data import MAIN_MENU_PLAN, TEAM_NAMES, TEAM_ICONS
from tools.settings import FONT_BUTTON


class MainMenu:
    def __init__(self, screen_width: int, screen_height: int, tile_size: int):
        self.active = True
        self.labels = []
        self.buttons = []

        self.grid = None
        self.positioner = Positioner((screen_width, screen_height), tile_size)

        self.create_window()

    def create_window(self):
        self.grid = self.positioner.transform(MAIN_MENU_PLAN)

        # Header label:
        kind = 'header'
        label = Label(kind, self.grid[kind][0], 'Familiada', FONT_BUTTON, True, self.grid[kind][1])
        self.labels.append(label)

        button_configurations = {
            'start': (StartButton, "Rozpocznij grę"),
            'options': (OptionsButton, "Opcje"),
            'exit': (ExitButton, 'Wyjdź')
        }
        for key, (button_class, text) in button_configurations.items():
            button = button_class(self.grid[key][0], key, text, FONT_BUTTON, self.grid[key][1])
            self.buttons.append(button)
