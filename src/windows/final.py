from tools.game_utils import (toggle_button, update_label, toggle_label, active_point_label, add_strike, clear_sum,
                              clear_strikes, blind_point_label, hide_label, load_choice_to_label)
from windows.window import Window
from configuration.final_ui_configuration import FinalUiConfiguration
from data.game_data import FINAL_PLAN
from data.settings import FONT_BUTTON, FONT_LABEL, DB_PATH
from managers.round_manager import RoundManager
from tools.support import puts
from windows.answer import Answer
from pygame.surface import Surface
import random


class Final(Window):
    def __init__(self, screen_width: int, screen_height: int, tile_size: int, manager: RoundManager):
        self.configuration = None
        super().__init__(screen_width, screen_height, tile_size)
        self.final_manager = manager
        self.answer_window = Answer(screen_width, screen_height, tile_size)
        self.answer_window.deactivate()
        self.hide_answers()

    def create_window(self):
        self.configuration = FinalUiConfiguration()
        self.grid = self.positioner.transform(FINAL_PLAN)

        for key, (label_class, text, background) in self.configuration.labels.items():
            label = label_class(key, self.grid[key][0], text, FONT_LABEL, background, self.grid[key][1])
            self.labels.append(label)

        for key, (sticker_class, visible) in self.configuration.stickers.items():
            sticker = sticker_class(key, self.grid[key][0], self.grid[key][1], visible)
            self.stickers.append(sticker)

        for key, (button_class, text) in self.configuration.buttons.items():
            button = button_class(self.grid[key][0], key, text, FONT_BUTTON, self.grid[key][1])
            self.buttons.append(button)

    def hide_answers(self) -> None:
        for label in self.labels:
            for i in range(1, self.final_manager.max_answers + 1):
                if label.kind == f'f_answer {i}':
                    hide_label(label)
                if label.kind == f'f_points {i}':
                    hide_label(label)

    def transfer_points(self) -> None:
        for label in self.labels:
            if label.kind == 'f_points_team_1':
                label.change_text(str(self.final_manager.team_points[1]))
            if label.kind == 'f_points_team_2':
                label.change_text(str(self.final_manager.team_points[2]))
        puts('Transfer punktów udany')
        self.disable_next_button()

    def disable_next_button(self, team: str = None) -> None:
        off_team = '2'
        on_team = '1'
        if team is None:
            if self.final_manager.team_points[1] < self.final_manager.team_points[2]:
                off_team = '1'
                on_team = '2'
            elif self.final_manager.team_points[1] == self.final_manager.team_points[2]:
                numbers = [1, 2]
                random.shuffle(numbers)
                off_team = numbers[0]
                on_team = numbers[1]
        else:
            if team == '1':
                off_team = '1'
                on_team = '2'
        for button in self.buttons:
            if button.kind == f'f_next_round_{off_team}':
                button.clickable = False
            elif button.kind == f'f_next_round_{on_team}':
                button.clickable = True

    def update_question(self, question: dict) -> None:
        for label in self.labels:
            for i in range(1, ):
                if label.kind == f'f_answer {i}':
                    if update_label(label, question, True):
                        toggle_button(self.buttons, f'f_answer_show_{i}', True)
                    else:
                        toggle_button(self.buttons, f'f_answer_show_{i}', False)
                if label.kind == f'f_points {i}':
                    update_label(label, question, False)

    def show_answer(self, number: str) -> None:
        """
        Wyświetla menu odpowiedzi
        :param number:
        :return:
        """
        self.answer_window.show()
        self.answer_window.change_number(number)
        puts('Pokazuje menu z wyborem odpowiedzi')

    def pick_answer(self, number: str) -> None:
        load_choice_to_label(self.labels, f'f_answer {self.answer_window.number}', number, self.final_manager)
        self.answer_window.hide()

    def draw_winner(self) -> None:
        for label in self.labels:
            if label.kind == 'f_header':
                if self.final_manager.team_points[1] > self.final_manager.team_points[2]:
                    label.change_text(f'Wygrała drużyna nr 1!')
                elif self.final_manager.team_points[1] == self.final_manager.team_points[2]:
                    label.change_text(f'Remis!')
                else:
                    label.change_text(f'Wygrała drużyna nr 2!')
        for button in self.buttons:
            if button.kind == 'f_pause':
                continue
            else:
                button.clickable = False

    def go_next_round(self, team: int) -> bool:
        """
        Przechodzi do nastepnej rundy
        :return:
        """
        self.final_manager.add_points(team)
        clear_sum(self.labels, self.final_manager)
        if self.final_manager.index < self.final_manager.max_rounds:
            self.final_manager.next_round()
            self.disable_next_button(str(team))
            self.hide_answers()
            return False
        else:
            puts('Koniec wszystkich rund, koniec gry.')
            self.draw_winner()
            return True

    def draw(self, screen: Surface):
        for button in self.buttons:
            if button.exist:
                button.draw(screen)
        for label in self.labels:
            if label.exist:
                label.draw(screen)
        for sticker in self.stickers:
            sticker.draw(screen)
        if self.answer_window.active:
            self.answer_window.draw(screen)


