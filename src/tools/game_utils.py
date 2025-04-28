from tools.support import add_dots_until_width, puts
from managers.round_manager import RoundManager
from ui.label import Label


def toggle_button(buttons: list, kind: str, status: bool) -> None:
    """
    Zmiana stanu wyświetlania przycisku
    :param buttons: lista przycisków
    :param kind: unikalna nazwa przycisku
    :param status: nowy status exist
    :return: None
    """
    for button in buttons:
        if button.kind == kind:
            button.exist = status


def toggle_label(labels: list, kind: str, status: bool) -> None:
    """
    Zmiana statusu wyświetlania treści labela.
    :param labels: Lista obiektów Label
    :param kind: unikalna nazwa Labela
    :param status: nowy stan parametru exist
    :return: None
    """
    for label in labels:
        if label.kind == kind:
            label.visible = status


def update_label(label: Label, question: dict, dots: bool) -> bool:
    """
    Zaktualizowanie labela do nowego tekstu, wraz z włączeniem jego exist i wyłączeniem visibility
    :param label: Obiekt klasy Label
    :param question: słownik zawierający aktualne pytania i odpowiedzi
    :return: None
    """
    if label.kind in question:
        text = str(question[label.kind])
        if dots:
            # text = add_dots(text,50)
            text = add_dots_until_width(text, label.font, label.size[0], 200)
        label.change_text(text)
        label.exist = True
        label.visible = False
        return True
    else:
        label.exist = False
        return False

def hide_label(label: Label) -> None:
    label.exist = True
    label.visible = False

def active_point_label(labels: list, kind: str, manager: RoundManager) -> None:
    """
    Zmiana statusu wyświetlania treści labela z punktami.
    :param labels: Lista obiektów Label
    :param kind: unikalna nazwa Labela
    :param manager:
    :return: None
    """
    pot_label = None
    for label in labels:
        if label.kind == 'points_sum':
            pot_label = label
    for label in labels:
        if label.kind == kind:
            if label.visible is False:
                label.visible = True
                add_to_sum(pot_label, label, manager)


def blind_point_label(labels: list, kind: str) -> None:
    """
    Wyświetla label punktowy wyzerowany.
    :param labels: Lista obiektów Label
    :param kind: unikalna nazwa Labela
    :return: None
    """
    for label in labels:
        if label.kind == kind:
            if label.visible is False:
                label.visible = True


def add_to_sum(pot_label: Label, label: Label, manager: RoundManager):
    """
    Dodaje wartośc odpowiedzi do sumy ogólnej do zdobycia
    :param pot_label:
    :param label:
    :param manager:
    :return:
    """
    value = 0
    try:
        value += int(label.text)
    except:
        puts('Nie udało się odczytać wartości odpowiedzi...')

    manager.pot += value
    pot_label.text = str(manager.pot)

def clear_sum(labels: list, manager: RoundManager) -> None:
    """
    Wyczyść pole SUMA oraz zaktualizuj pola punktów drużyn
    :param labels:
    :param manager:
    :return:
    """
    for label in labels:
        if 'points_sum' in label.kind:
            label.text = str(manager.pot)
        if 'points_team_1' in label.kind:
            label.change_text(str(manager.team_points[1]))
        if 'points_team_2' in label.kind:
            label.change_text(str(manager.team_points[2]))

def add_strike(team: int, stickers: list, manager: RoundManager) -> None:
    """
    Dodaje strike dla wybranej drużyny
    :param team:
    :param stickers:
    :param manager:
    :return:
    """
    site = 'left'
    if team == 2:
        site = 'right'
    if team == manager.first_team:
        if manager.xs[team] <= 3:
            for sticker in stickers:
                if sticker.kind == f'{site}_small_x_{manager.xs[team]}':
                    sticker.visible = True
        else:
            puts(f'Drużyna {team} przegrywa...')
    else:
        if manager.xs[team] <= 1:
            for sticker in stickers:
                if sticker.kind == f'{site}_small_x_2':
                    sticker.visible = True
        else:
            puts(f'Drużyna {team} przegrywa...')


def clear_strikes(stickers: list) -> None:
    """
    Ukrywa na początku rundy wszytkie striki
    :param stickers:
    :return:
    """
    for sticker in stickers:
        if sticker.kind.startswith('left_small_x'):
            sticker.visible = False
        elif sticker.kind.startswith('right_small_x'):
            sticker.visible = False


def load_choice_to_label(labels: list, kind: str, choice: str, manager: RoundManager) -> None:
    number = int(kind[-1])
    for label in labels:
        #Answer:
        if label.kind == kind:
            if choice == '7':
                text = '.'
            else:
                text = manager.question[number][f'answer {choice}']
            new_text = add_dots_until_width(text, label.font, label.size[0], 200)
            label.change_text(new_text)
            label.visible = True
        #Points:
        if label.kind == f'f_points {number}':
            if choice == '7':
                label.change_text('0')
            else:
                label.change_text(str(manager.question[number][f'points {choice}']))
            label.visible = True

            for pot_label in labels:
                if pot_label.kind == 'f_points_sum':
                    check_sum(pot_label, labels, manager)


def check_sum(pot_label: Label, labels: list, manager: RoundManager):
    """
    Sumuje widoczne odpowiedzi
    :param pot_label:
    :param labels:
    :param manager:
    :return:
    """
    new_sum = 0
    for label in labels:
        if label.kind.startswith('f_points ') and label.visible:
            new_sum += int(label.text)
            puts(f'Dodaje {label.text} z {label.kind} do sumy ogólnej')
    manager.pot = new_sum
    pot_label.change_text(str(new_sum))

