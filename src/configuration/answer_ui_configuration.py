from ui.label import Label, LabelBig
from ui.sticker import Sticker
from ui.button import Button, QuestionShowButton, AnswerShowButton, BlindButton
from tools.support import add_dots


class AnswerUiConfiguration:
    def __init__(self):
        self.labels = {}
        self.stickers = {}
        self.buttons = {}

        self.setup()

    def setup(self) -> None:
        # Stickers
        # kind: (Class, is_visible)
        self.stickers = {
            'background': (Sticker, True)
        }
        # Buttons
        # kind: (Class, text)
        self.buttons = {
            'back': (Button, '<-'),
            'choice_1': (Button, '1'),
            'choice_2': (Button, '2'),
            'choice_3': (Button, '3'),
            'choice_4': (Button, '4'),
            'choice_5': (Button, '5'),
            'choice_6': (Button, '6'),
            'choice_bad': (Button, 'X')
        }
