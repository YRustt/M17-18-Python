import random


class Shark:
    FULLNESS = 10

    def __init__(self, ocean, x, y):
        # type: (Ocean, int, int) -> None

        self._fullness = Shark.FULLNESS
        self._ocean = ocean
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @classmethod
    def set_fullness(cls, fullness):
        cls.FULLNESS = fullness


class Guppies:
    def __init__(self, ocean, x, y):
        # type: (Ocean, int, int) -> None

        self._ocean = ocean
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y


class Land:
    def __init__(self, ocean, x, y):
        # type: (Ocean, int, int) -> None

        self._ocean = ocean
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y


class Water:
    def __new__(cls, *args, **kwargs):
        if not hasattr(Water, '__instance'):
            Water.__instance = object.__new__(cls)

        return Water.__instance

    def __init__(self, *args, **kwargs):
        pass


class Ocean:
    def __init__(self, size):
        self._size = size
        self._map = [[None] * self._size for _ in range(self._size)]

    def __iter__(self):
        for row in self._map:
            for cell in row:
                yield cell

    def get_cell(self, i, j):
        return self._map[i][j]

    def set_cell(self, i, j, value):
        self._map[i][j] = value

    @property
    def size(self):
        return self._size


class Move:
    @staticmethod
    def move_obj(obj):
        pass


class Eat:
    pass


class Reproduction:
    pass


def generate_ocean():
    size = 100
    weighted_choices = [(Shark, 10), (Guppies, 7), (Land, 2), (Water, 81)]
    population = [val for val, cnt in weighted_choices for i in range(cnt)]
    choices = [random.choice(population) for _ in range(size * size)]

    ocean = Ocean(size)

    for idx, cls in enumerate(choices):
        x, y = divmod(idx, size)
        cell = cls(ocean, x, y)
        ocean.set_cell(x, y, cell)

    return ocean
