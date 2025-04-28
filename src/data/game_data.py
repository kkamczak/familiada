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

X_LINE_1 = 23
X_LINE_2 = 92
X_SIZE = (6, 6)
ANS_LINE = 39
ANS_SIZE = (40, 2)
ANS_SHOW_LINE = 33
PT_LINE = 82

PT_SIZE = (3, 2)
SHOW_SIZE = (2, 2)



GAME_PLAN = {
    #Labels:
    'question': [(ANS_LINE, 14), ANS_SIZE],
    'answer 1': [(ANS_LINE, 20), ANS_SIZE], 'points 1': [(PT_LINE, 20), PT_SIZE],
    'answer 2': [(ANS_LINE, 25), ANS_SIZE], 'points 2': [(PT_LINE, 25), PT_SIZE],
    'answer 3': [(ANS_LINE, 30), ANS_SIZE], 'points 3': [(PT_LINE, 30), PT_SIZE],
    'answer 4': [(ANS_LINE, 35), ANS_SIZE], 'points 4': [(PT_LINE, 35), PT_SIZE],
    'answer 5': [(ANS_LINE, 40), ANS_SIZE], 'points 5': [(PT_LINE, 40), PT_SIZE],
    'answer 6': [(ANS_LINE, 45), ANS_SIZE], 'points 6': [(PT_LINE, 45), PT_SIZE],
    'points_sum': [(80, 50), (12, 2)],
    'points_team_1': [(25, 55), (4, 2)],
    'points_team_2': [(92, 55), (4, 2)],


    #Stickers:
    'left_small_x_1': [(X_LINE_1, 16), X_SIZE], 'right_small_x_1': [(X_LINE_2, 16), X_SIZE],
    'left_small_x_2': [(X_LINE_1, 26), X_SIZE], 'right_small_x_2': [(X_LINE_2, 26), X_SIZE],
    'left_small_x_3': [(X_LINE_1, 36), X_SIZE], 'right_small_x_3': [(X_LINE_2, 36), X_SIZE],

    #Buttons:
    'pause': [(1, 1), (9, 3)],
    'question_show': [(ANS_SHOW_LINE, 14), SHOW_SIZE],
    'answer_show_1': [(ANS_SHOW_LINE, 20), SHOW_SIZE], 'blind_show_1': [(PT_LINE, 20), PT_SIZE],
    'answer_show_2': [(ANS_SHOW_LINE, 25), SHOW_SIZE], 'blind_show_2': [(PT_LINE, 25), PT_SIZE],
    'answer_show_3': [(ANS_SHOW_LINE, 30), SHOW_SIZE], 'blind_show_3': [(PT_LINE, 30), PT_SIZE],
    'answer_show_4': [(ANS_SHOW_LINE, 35), SHOW_SIZE], 'blind_show_4': [(PT_LINE, 35), PT_SIZE],
    'answer_show_5': [(ANS_SHOW_LINE, 40), SHOW_SIZE], 'blind_show_5': [(PT_LINE, 40), PT_SIZE],
    'answer_show_6': [(ANS_SHOW_LINE, 45), SHOW_SIZE], 'blind_show_6': [(PT_LINE, 45), PT_SIZE],
    'next_round_1': [(48, 55), (8, 4)],
    'next_round_2': [(58, 55), (8, 4)],

    'wrong_1': [(0, 15), (8, 32)],
    'wrong_2': [(115, 15), (8, 32)]
}

FINAL_PLAN = {
    #Labels:
    'f_header': [(ANS_LINE, 14), ANS_SIZE],
    'f_answer 1': [(ANS_LINE, 20), ANS_SIZE], 'f_points 1': [(PT_LINE, 20), PT_SIZE],
    'f_answer 2': [(ANS_LINE, 25), ANS_SIZE], 'f_points 2': [(PT_LINE, 25), PT_SIZE],
    'f_answer 3': [(ANS_LINE, 30), ANS_SIZE], 'f_points 3': [(PT_LINE, 30), PT_SIZE],
    'f_answer 4': [(ANS_LINE, 35), ANS_SIZE], 'f_points 4': [(PT_LINE, 35), PT_SIZE],
    'f_answer 5': [(ANS_LINE, 40), ANS_SIZE], 'f_points 5': [(PT_LINE, 40), PT_SIZE],
    'f_points_sum': [(80, 50), (12, 2)],
    'f_points_team_1': [(25, 55), (4, 2)],
    'f_points_team_2': [(92, 55), (4, 2)],

    #Buttons:
    'f_pause': [(1, 1), (9, 3)],
    'f_answer_show_1': [(ANS_SHOW_LINE, 20), SHOW_SIZE], 'f_blind_show_1': [(PT_LINE, 20), PT_SIZE],
    'f_answer_show_2': [(ANS_SHOW_LINE, 25), SHOW_SIZE], 'f_blind_show_2': [(PT_LINE, 25), PT_SIZE],
    'f_answer_show_3': [(ANS_SHOW_LINE, 30), SHOW_SIZE], 'f_blind_show_3': [(PT_LINE, 30), PT_SIZE],
    'f_answer_show_4': [(ANS_SHOW_LINE, 35), SHOW_SIZE], 'f_blind_show_4': [(PT_LINE, 35), PT_SIZE],
    'f_answer_show_5': [(ANS_SHOW_LINE, 40), SHOW_SIZE], 'f_blind_show_5': [(PT_LINE, 40), PT_SIZE],
    'f_next_round_1': [(48, 55), (8, 4)],
    'f_next_round_2': [(58, 55), (8, 4)],
}

ANSWER_PLAN = {
    #Stickers:
    'background': [(ANS_SHOW_LINE-5, 20), (3, 24)],
    #Buttons:
    'back': [(ANS_SHOW_LINE-5, 20), (3, 3)],
    'choice_1': [(ANS_SHOW_LINE-5, 23), (3, 3)],
    'choice_2': [(ANS_SHOW_LINE-5, 26), (3, 3)],
    'choice_3': [(ANS_SHOW_LINE-5, 29), (3, 3)],
    'choice_4': [(ANS_SHOW_LINE-5, 32), (3, 3)],
    'choice_5': [(ANS_SHOW_LINE-5, 35), (3, 3)],
    'choice_6': [(ANS_SHOW_LINE-5, 38), (3, 3)],
    'choice_bad': [(ANS_SHOW_LINE-5, 41), (3, 3)]
}
