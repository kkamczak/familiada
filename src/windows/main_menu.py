from windows.window import Window
from ui.label import Label
from ui.button import Button
from data.game_data import MAIN_MENU_PLAN
from data.settings import FONT_BUTTON


class MainMenu(Window):
    def __init__(self, screen_width: int, screen_height: int, tile_size: int):
        super().__init__(screen_width, screen_height, tile_size)

    def create_window(self):
        self.grid = self.positioner.transform(MAIN_MENU_PLAN)

        # Header label:
        label_configurations = {
            'header': (Label, "Familiada"),
        }
        for key, (label_class, text) in label_configurations.items():
            label = label_class(key, self.grid[key][0], text, FONT_BUTTON, True, self.grid[key][1])
            self.labels.append(label)

        button_configurations = {
            'start': (Button, "Rozpocznij grę"),
            'options': (Button, "Opcje"),
            'exit': (Button, 'Wyjdź')
        }
        for key, (button_class, text) in button_configurations.items():
            button = button_class(self.grid[key][0], key, text, FONT_BUTTON, self.grid[key][1])
            self.buttons.append(button)
