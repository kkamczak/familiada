from ui.label import Label, LabelBig
from ui.sticker import Sticker
from ui.button import Button, QuestionShowButton, AnswerShowButton, WrongButton
from tools.support import add_dots


class GameUiConfiguration:
    def __init__(self):
        self.labels = None
        self.stickers = None
        self.buttons = None

        self.setup()

    def setup(self) -> None:
        # Labels
        # kind: (Class, text, with_background)
        self.labels = {
            'question': (Label, "Pytanie jakieś tam", False),
            'answer 1': (Label, add_dots("Odpowiedz 1 która jest dłuższa", 50), False),
            'answer 2': (Label, add_dots("Odpowiedz 2", 50), False),
            'answer 3': (Label, add_dots("Odpowiedz 3", 50), False),
            'answer 4': (Label, add_dots("Odpowiedz 4", 50), False),
            'answer 5': (Label, add_dots("Odpowiedz 5", 50), False),
            'answer 6': (Label, add_dots("Odpowiedz 6", 50), False),

            'points 1': (Label, "0", False),
            'points 2': (Label, "0", False),
            'points 3': (Label, "0", False),
            'points 4': (Label, "0", False),
            'points 5': (Label, "0", False),
            'points 6': (Label, "0", False),

            'points_sum': (Label, "0", False),

            'points_team_1': (Label, '0', False),
            'points_team_2': (Label, '0', False),
        }
        # Stickers
        # kind: (Class, is_visible)
        self.stickers = {
            'left_small_x_1': (Sticker, False), 'right_small_x_1': (Sticker, False),
            'left_small_x_2': (Sticker, False), 'right_small_x_2': (Sticker, False),
            'left_small_x_3': (Sticker, False), 'right_small_x_3': (Sticker, False)
        }
        # Buttons
        # kind: (Class, text)
        self.buttons = {
            'pause': (Button, 'Menu'),
            'question_show': (QuestionShowButton, ''),
            'answer_show_1': (AnswerShowButton, ''),
            'answer_show_2': (AnswerShowButton, ''),
            'answer_show_3': (AnswerShowButton, ''),
            'answer_show_4': (AnswerShowButton, ''),
            'answer_show_5': (AnswerShowButton, ''),
            'answer_show_6': (AnswerShowButton, ''),
            'next_round_1': (Button, ''),
            'next_round_2': (Button, ''),

            'wrong_1': (WrongButton, ''),
            'wrong_2': (WrongButton, '')
        }
