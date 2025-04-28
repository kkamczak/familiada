import pygame
import sys
from tools.game_utils import toggle_label


class ButtonsManager:
    def __init__(self, main_window):
        """
        Kontroluje akcje wszystkich przecisków
        """
        self.main = main_window

    def create_timer(self) -> None:
        self.main.create_timer()

    def check_action(self, button) -> None:
        action = button.action()
        game = self.main.windows['Game']
        final = self.main.windows['Final']
        if action == 'exit':
            self.exit_game()
        elif 'pause' in action:
            self.main.pause_game()
        elif action == 'start':
            self.main.open_game_window()
        elif action == 'question_show':
            toggle_label(game.labels, 'question', True)
        elif action.startswith('answer_show_'):
            game.show_answer(action[-1])
        elif action.startswith('blind_show_'):
            game.blind_answer(action[-1])
        elif action.startswith('wrong_'):
            game.show_wrong_answer(int(action[-1]))
        elif action.startswith('next_round_'):
            if game.go_next_round(int(action[-1])):
                self.main.go_final()
        #Final:
        elif action.startswith('f_answer_show_'):
            final.show_answer(action[-1])


    @staticmethod
    def exit_game() -> None:
        pygame.quit()
        sys.exit()

    @staticmethod
    def change_buttons(buttons: list, click_on=None, click_off=None, show_on=None, show_off=None) -> None:
        if click_on is None:
            click_on = []
        if click_off is None:
            click_off = []
        if show_on is None:
            show_on = []
        if show_off is None:
            show_off = []
        for button in buttons:
            if button.kind in click_on:
                button.clickable = True
            elif button.kind in click_off:
                button.clickable = False
                button.set_image(False)
            if button.kind in show_off:
                button.clickable = False
                button.show = False
            elif button.kind in show_on:
                button.clickable = True
                button.show = True


