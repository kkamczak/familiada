from tools.support import add_dots
from tools.utils import toggle_button, update_label
from windows.window import Window
from configuration.game_ui_configuration import GameUiConfiguration
from data.game_data import GAME_PLAN
from data.settings import FONT_BUTTON


class Game(Window):
    def __init__(self, screen_width: int, screen_height: int, tile_size: int):
        self.configuration = None
        super().__init__(screen_width, screen_height, tile_size)

    def create_window(self):
        self.configuration = GameUiConfiguration()
        self.grid = self.positioner.transform(GAME_PLAN)

        for key, (label_class, text, background) in self.configuration.labels.items():
            label = label_class(key, self.grid[key][0], text, FONT_BUTTON, background, self.grid[key][1])
            self.labels.append(label)

        for key, (sticker_class, visible) in self.configuration.stickers.items():
            sticker = sticker_class(key, self.grid[key][0], self.grid[key][1], visible)
            self.stickers.append(sticker)

        for key, (button_class, text) in self.configuration.buttons.items():
            button = button_class(self.grid[key][0], key, text, FONT_BUTTON, self.grid[key][1])
            self.buttons.append(button)

    def update_question(self, question: dict) -> None:
        for label in self.labels:
            if label.kind == 'question':
                update_label(label, question, False)
            for i in range(1, 7):
                if label.kind == f'answer {i}':
                    if update_label(label, question, True):
                        toggle_button(self.buttons, f'answer_show_{i}', True)
                    else:
                        toggle_button(self.buttons, f'answer_show_{i}', False)
                if label.kind == f'points {i}':
                    update_label(label, question, False)

