from typing import Union


class Positioner:
    def __init__(self, screen_size: tuple, tile_size: int) -> None:
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.tile_size = tile_size

        self.clicked = False

        self.start = [0, 0, 0, 0]
        self.checking = False

    def transform(self, positions: dict) -> dict:
        new_dict = {}
        for element in positions:
            position = self.position(positions[element][0], self.tile_size)
            size = self.position(positions[element][1], self.tile_size)
            new_dict[element] = [position, size]
        return new_dict

    @staticmethod
    def position(position: Union[int, tuple], tile_size: int) -> Union[int, tuple]:
        """
        Kalkuluje pozycje / długość w oparciu o szerkość kafelka

        :param position:
        :param tile_size:
        :return:
        """
        if isinstance(position, tuple):
            return position[0] * tile_size, position[1] * tile_size
        elif isinstance(position, int):
            return position * tile_size
        else:
            print('Function position() error...')
            return 0
