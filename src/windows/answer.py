from windows.window import Window
from configuration.answer_ui_configuration import AnswerUiConfiguration
from data.game_data import ANSWER_PLAN
from data.settings import FONT_LABEL, FONT_BUTTON

class Answer(Window):
    def __init__(self, screen_width: int, screen_height: int, tile_size: int):
        self.configuration = None
        super().__init__(screen_width, screen_height, tile_size)

    def create_window(self):
        self.configuration = AnswerUiConfiguration()
        self.grid = self.positioner.transform(ANSWER_PLAN)

        for key, (label_class, text, background) in self.configuration.labels.items():
            label = label_class(key, self.grid[key][0], text, FONT_LABEL, background, self.grid[key][1])
            self.labels.append(label)

        for key, (sticker_class, visible) in self.configuration.stickers.items():
            sticker = sticker_class(key, self.grid[key][0], self.grid[key][1], visible)
            self.stickers.append(sticker)

        for key, (button_class, text) in self.configuration.buttons.items():
            button = button_class(self.grid[key][0], key, text, FONT_BUTTON, self.grid[key][1])
            self.buttons.append(button)