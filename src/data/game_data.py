DATA_PATH = 'content/database.xlsx'
BL_PATH = 'content/blacklist.txt'
IMAGES = 'content/images/'
FORMAT = '.png'
BUTTONS_ACTION_TEXT = {
    'start': 'Rozpoczynam gre...',
    'options': 'Uruchamiam opcje...',
    'exit': 'Wychodze z gry...',
    'pause': 'Uruchamiam pauze...',
    'question_show': 'Pokazuje pytanie...',
    'answer_show_1': 'Pokazuje odpowiedz nr 1',
    'answer_show_2': 'Pokazuje odpowiedz nr 2',
    'answer_show_3': 'Pokazuje odpowiedz nr 3',
    'answer_show_4': 'Pokazuje odpowiedz nr 4',
    'answer_show_5': 'Pokazuje odpowiedz nr 5',
    'answer_show_6': 'Pokazuje odpowiedz nr 6',
    'next_round_1': 'Rundę wygrywa drużyna 1...',
    'next_round_2': 'Rundę wygrywa drużyna 2...'
}

TIME = 60
ROUND_AMOUNT = 8

QUESTION_SIZE = (8, 8)

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

GAME_PLAN = {
    #Labels:
    'question': [(45, 14), (30, 2)],
    'answer 1': [(45, 20), (30, 2)], 'points 1': [(80, 20), (2, 2)],
    'answer 2': [(45, 25), (30, 2)], 'points 2': [(80, 25), (2, 2)],
    'answer 3': [(45, 30), (30, 2)], 'points 3': [(80, 30), (2, 2)],
    'answer 4': [(45, 35), (30, 2)], 'points 4': [(80, 35), (2, 2)],
    'answer 5': [(45, 40), (30, 2)], 'points 5': [(80, 40), (2, 2)],
    'answer 6': [(45, 45), (30, 2)], 'points 6': [(80, 45), (2, 2)],
    'points_sum': [(80, 50), (12, 2)],
    'points_team_1': [(25, 55), (4, 2)],
    'points_team_2': [(92, 55), (4, 2)],


    #Stickers:
    'left_small_x_1': [(25, 16), (8, 8)], 'right_small_x_1': [(92, 16), (8, 8)],
    'left_small_x_2': [(25, 26), (8, 8)], 'right_small_x_2': [(92, 26), (8, 8)],
    'left_small_x_3': [(25, 36), (8, 8)], 'right_small_x_3': [(92, 36), (8, 8)],

    #Buttons:
    'pause': [(1, 1), (9, 3)],
    'question_show': [(41, 14), (2, 2)],
    'answer_show_1': [(41, 20), (2, 2)],
    'answer_show_2': [(41, 25), (2, 2)],
    'answer_show_3': [(41, 30), (2, 2)],
    'answer_show_4': [(41, 35), (2, 2)],
    'answer_show_5': [(41, 40), (2, 2)],
    'answer_show_6': [(41, 40), (2, 2)],
    'next_round_1': [(48, 55), (8, 4)],
    'next_round_2': [(58, 55), (8, 4)],

    'wrong_1': [(0, 15), (8, 32)],
    'wrong_2': [(115, 15), (8, 32)]
}
