from ui.label import Label, LabelBig
from ui.sticker import Sticker
from ui.button import Button, QuestionShowButton, AnswerShowButton, BlindButton
from tools.support import add_dots


class FinalUiConfiguration:
    def __init__(self):
        self.labels = None
        self.stickers = None
        self.buttons = None

        self.setup()

    def setup(self) -> None:
        # Labels
        # kind: (Class, text, with_background)
        self.labels = {
            'f_header': (Label, "Finał", False),
            'f_answer 1': (Label, add_dots("Odpowiedz 1 która jest dłuższa", 50), False),
            'f_answer 2': (Label, add_dots("Odpowiedz 2", 50), False),
            'f_answer 3': (Label, add_dots("Odpowiedz 3", 50), False),
            'f_answer 4': (Label, add_dots("Odpowiedz 4", 50), False),
            'f_answer 5': (Label, add_dots("Odpowiedz 5", 50), False),

            'f_points 1': (Label, "0", False),
            'f_points 2': (Label, "0", False),
            'f_points 3': (Label, "0", False),
            'f_points 4': (Label, "0", False),
            'f_points 5': (Label, "0", False),

            'f_points_sum': (Label, "0", False),

            'f_points_team_1': (Label, '0', False),
            'f_points_team_2': (Label, '0', False),
        }
        # Stickers
        # kind: (Class, is_visible)
        self.stickers = {

        }
        # Buttons
        # kind: (Class, text)
        self.buttons = {
            'f_pause': (Button, 'Menu'),
            'f_answer_show_1': (AnswerShowButton, ''), 'f_blind_show_1': (BlindButton, ''),
            'f_answer_show_2': (AnswerShowButton, ''), 'f_blind_show_2': (BlindButton, ''),
            'f_answer_show_3': (AnswerShowButton, ''), 'f_blind_show_3': (BlindButton, ''),
            'f_answer_show_4': (AnswerShowButton, ''), 'f_blind_show_4': (BlindButton, ''),
            'f_answer_show_5': (AnswerShowButton, ''), 'f_blind_show_5': (BlindButton, ''),
            'f_next_round_1': (Button, ''),
            'f_next_round_2': (Button, ''),
        }
