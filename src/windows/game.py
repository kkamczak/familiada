from tools.utils import toggle_button, update_label, toggle_label, active_point_label, add_x, clear_sum, add_to_team_points
from windows.window import Window
from configuration.game_ui_configuration import GameUiConfiguration
from data.game_data import GAME_PLAN
from data.settings import FONT_BUTTON, DB_PATH
from managers.round_manager import RoundManager
from tools.support import puts


class Game(Window):
    def __init__(self, screen_width: int, screen_height: int, tile_size: int):
        self.configuration = None
        super().__init__(screen_width, screen_height, tile_size)
        self.round_manager = RoundManager(DB_PATH)
        self.update_question(self.round_manager.round_set[self.round_manager.index])

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

    def show_answer(self, number: str) -> None:
        """
        Wyświetla wybraną odpowiedz oraz jej punktacje
        :param number:
        :return:
        """
        toggle_label(self.labels, f'answer {number}', True)
        active_point_label(self.labels, f'points {number}', self.round_manager)

    def show_wrong_answer(self, team: int) -> None:
        """
        Wyświetla że dana drużyna źle odpowiedziała
        :param team:
        :return:
        """
        self.round_manager.wrong_answer(team)
        add_x(team, self.stickers, self.round_manager)

    def go_next_round(self, team: int) -> None:
        """
        Przechodzi do nastepnej rundy
        :return:
        """
        self.round_manager.add_points(team)
        clear_sum(self.labels, self.round_manager.pot)
        add_to_team_points(self.labels, self.round_manager)

