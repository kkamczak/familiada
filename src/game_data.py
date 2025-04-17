"""
Żółci - 0, Niebiescy - 1, Zieloni - 2
"""
TEAMS = ['yellow', 'blue', 'green']
INDEX = {
    'yellow': 0,
    'blue': 1,
    'green': 2
}
TEAM_NAMES = ['Żółci', 'Niebiescy', 'Zieloni']
TEAM_ICONS = {
    'yellow_cap': 'content/ui/icons/yellow_cap.png',
    'blue_cap': 'content/ui/icons/blue_cap.png',
    'green_cap': 'content/ui/icons/green_cap.png'
}

DATA_PATH = 'content/database.xlsx'
BL_PATH = 'content/blacklist.txt'
IMAGES = 'content/images/'
FORMAT = '.png'
DATA_COLUMNS = {
    'id': 'Numer pytania',
    'category': 'Kategoria',
    'question': 'Pytanie',
    'answer': 'Odpowiedź',
    'tip_1': 'Podpowiedź 1',
    'tip_2': 'Podpowiedź 2',
    'tip_3': 'Podpowiedź 3'
}

TIME = 60
ROUND_AMOUNT = 8

ICON_SIZE = (8, 8)
BALANCE_SIZE = (16, 4)
BET_SIZE = (16, 6)
ADD_SIZE = (2, 2)
SUB_SIZE = (2, 2)
MULTI_SIZE = (4, 2)
VABANK_SIZE = (8, 3)
BUTTON_SIZE = (16, 4)
EXIT_SIZE = (4, 4)

# Button and label configuration [(X, Y), (WIDTH, HEIGHT)]:

MAIN_WINDOW_PLAN = {
    'round': [(115, 3), (0, 0)]
}

MAIN_MENU_PLAN = {
    #Labels:
    'header': [(47, 15), (19, 6)],
    #Buttons:
    'start': [(52, 25), (9, 3)],
    'options': [(52, 30), (9, 3)],
    'exit': [(52, 35), (9, 3)]
}

PLAN2 = {
    'exit': [(1, 1), (9, 3)],

    'yellow_cap': [(24, 2), ICON_SIZE],
    'yellow_text': [(28, 12), (0, 0)],
    'yellow_text_2': [(9, 64), (0, 0)],
    'yellow_balance': [(20, 16), BALANCE_SIZE],
    'yellow_balance_2': [(1, 66), BALANCE_SIZE],
    'yellow_bet': [(20, 26), BET_SIZE],
    'yellow_plus': [(37, 26), ADD_SIZE],
    'yellow_multi': [(37, 30), MULTI_SIZE],
    'yellow_minus': [(17, 28), SUB_SIZE],
    'yellow_vabank': [(24, 33), VABANK_SIZE],

    'blue_cap': [(56, 2), ICON_SIZE],
    'blue_text': [(60, 12), (0, 0)],
    'blue_text_2': [(26, 64), (0, 0)],
    'blue_balance': [(52, 16), BALANCE_SIZE],
    'blue_balance_2': [(18, 66), BALANCE_SIZE],
    'blue_bet': [(52, 26), BET_SIZE],
    'blue_plus': [(69, 26), ADD_SIZE],
    'blue_multi': [(69, 30), MULTI_SIZE],
    'blue_minus': [(49, 28), SUB_SIZE],
    'blue_vabank': [(56, 33), VABANK_SIZE],

    'green_cap': [(87, 2), ICON_SIZE],
    'green_text': [(91, 12), (0, 0)],
    'green_text_2': [(43, 64), (0, 0)],
    'green_balance': [(83, 16), BALANCE_SIZE],
    'green_balance_2': [(35, 66), BALANCE_SIZE],
    'green_bet': [(83, 26), BET_SIZE],
    'green_plus': [(100, 26), ADD_SIZE],
    'green_multi': [(100, 30), MULTI_SIZE],
    'green_minus': [(80, 28), SUB_SIZE],
    'green_vabank': [(87, 33), VABANK_SIZE],

    'auction_label': [(60, 24), BUTTON_SIZE],
    'pot_label': [(50, 40), (20, 4)],
    'end_label': [(75, 40), BUTTON_SIZE],

    'roll': [(52, 46), BUTTON_SIZE],
    'question': [(52, 52), BUTTON_SIZE],
    'tips': [(52, 58), BUTTON_SIZE],
    'answer': [(52, 64), BUTTON_SIZE],
    'new': [(95, 46), BUTTON_SIZE],
    'buy': [(29, 40), BUTTON_SIZE],

    'category': [(60, 48), (0, 0)],
    'text': [(60, 51), (0, 0)],
    'text_space': [(0, 0), (0, 2)],
    'tip_0': [(11, 60), (0, 0)],
    'tip_1': [(41, 60), (0, 0)],
    'tip_2': [(71, 60), (0, 0)],
    'tip_3': [(101, 60), (0, 0)],
    'correct': [(60, 64), (0, 0)],

    'good': [(77, 65), (10, 3)],
    'bad': [(90, 65), (10, 3)],

    'roll_window': [(33, 39), (54, 20)],
    'image_window': [(15, 1), (90, 38)],
    'buy_window': [(40, 55), (40, 12)],
    'end_window': [(32, 26), (55, 15)],
    'clock': [(110, 6), (6, 6)],
    'round': [(115, 3), (0, 0)]

}

FRAME = {
    'winner': [(35, 34), (48, 5)],
    'square': [(0, 5), (10, 10)],
    'end_roll': [(0, 0), EXIT_SIZE]
}

IMAGE_FRAME = {
    'end_image': [(0, 0), EXIT_SIZE],
    'image': [(15, 1), (60, 36)]
}

END_FRAME = {
    'end_image': [(0, 0), EXIT_SIZE],
    'image': [(15, 1), (60, 36)],
    'winner': [(27, 7), (0, 0)]
}

BUY_FRAME = {
    'team': [(12, 1), (0, 0)],
    'balance': [(12, 1), BALANCE_SIZE],
    'bet': [(12, 6), BALANCE_SIZE],
    'minus': [(9, 7), SUB_SIZE],
    'plus': [(29, 7), ADD_SIZE],
    'buy': [(33, 1), (6, 3)],
    'end_buy': [(0, 0), EXIT_SIZE]
}
