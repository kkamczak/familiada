import pygame
import sys
from tools.utils import toggle_label, active_point_label, add_x, clear_sum, add_to_team_points


class ButtonsManager:
    def __init__(self, main_window):
        """
        Kontroluje działanie aplikacji.
        Statusy:
            main menu - menu główne
            game - główna rozgrywka
            options - opcje gry
            final - final rozgrywki
        """
        self.main = main_window
        self.status = 'main menu'
        self.storage = None
        self.round = 1

        self.losers = []

    def change_status(self, new_status: str) -> None:
        self.status = new_status

    def create_timer(self) -> None:
        self.main.create_timer()

    def check_action(self, button) -> None:
        action = button.action()
        game = self.main.windows['Game']
        manager = self.main.round_manager
        if action == 'exit':
            self.exit_game()
        elif action == 'pause':
            self.main.switch_window('Main Menu')
            buttons = self.main.windows['Main Menu'].buttons
            for button in buttons:
                if button.kind == 'start':
                    button.text = 'Wznów'
        elif action == 'start':
            self.main.create_game_window()
        elif action == 'question_show':
            toggle_label(game.labels, 'question', True)
        elif 'answer_show' in action:
            for i in range(1, 7):
                if action == f'answer_show_{i}':
                    toggle_label(game.labels, f'answer {i}', True)
                    active_point_label(game.labels, f'points {i}', manager)
        elif action == 'wrong_1':
            manager.wrong_answer(1)
            add_x(1, game.stickers, manager)
        elif action == 'wrong_2':
            manager.wrong_answer(2)
            add_x(2, game.stickers, manager)
        elif action == 'next_round_1':
            manager.add_points(1)
            clear_sum(game.labels, manager.pot)
            add_to_team_points(game.labels, manager)
        elif action == 'next_round_2':
            manager.add_points(2)
            clear_sum(game.labels, manager.pot)
            add_to_team_points(game.labels, manager)




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


