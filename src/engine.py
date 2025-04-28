import pygame
import sys


class Engine:
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
        if action == 'exit':
            self.exit_game()
        elif action == 'pause':
            self.main.switch_window('Main Menu')
        elif action == 'start':
            self.main.open_game_window()

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


