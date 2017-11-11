import random


class Shark:
    FULLNESS = 50
    REPRODUCTION = 100

    def __init__(self, ocean, x, y):
        # type: (Ocean, int, int) -> None

        self._fullness = Shark.FULLNESS
        self._reproduction = Shark.REPRODUCTION
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

    @property
    def fullness(self):
        return self._fullness

    def inc_fullness(self):
        self._fullness = Shark.FULLNESS

    def dec_fullness(self):
        self._fullness = max(0, self._fullness - 1)

    def is_dead(self):
        return self._fullness == 0

    def inc_reproduction(self):
        self._reproduction = Shark.REPRODUCTION

    def dec_reproduction(self):
        self._reproduction = max(0, self._reproduction - 1)

    def has_child(self):
        return self._reproduction == 0

    @property
    def ocean(self):
        return self._ocean

    @classmethod
    def set_fullness(cls, fullness):
        cls.FULLNESS = fullness

    @classmethod
    def set_reproduction(cls, reproduction):
        cls.REPRODUCTION = reproduction


class Guppies:
    REPRODUCTION = 2

    def __init__(self, ocean, x, y):
        # type: (Ocean, int, int) -> None

        self._reproduction = Guppies.REPRODUCTION
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

    def inc_reproduction(self):
        self._reproduction = Shark.REPRODUCTION

    def dec_reproduction(self):
        self._reproduction = max(0, self._reproduction - 1)

    def has_child(self):
        return self._reproduction == 0

    @property
    def ocean(self):
        return self._ocean

    @ocean.setter
    def ocean(self, ocean):
        self._ocean = ocean


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

    @property
    def ocean(self):
        return self._ocean

    @ocean.setter
    def ocean(self):
        return self._ocean


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
        self._time = 0

    def __iter__(self):
        for row in self._map:
            for cell in row:
                yield cell

    def get_cell(self, i, j):
        return self._map[i][j]

    def set_cell(self, i, j, value):
        self._map[i][j] = value

    def inc_time(self):
        self._time += 1

    @property
    def size(self):
        return self._size


class Run:
    @staticmethod
    def run_ocean(ocean):
        for obj in ocean:
            if isinstance(obj, Shark):
                Run.run_shark(obj)

        for obj in ocean:
            if isinstance(obj, Guppies):
                Run.run_guppies(obj)

        ocean.inc_time()

    @staticmethod
    def run_guppies(obj):
        Run._reproduction(obj) or Run._move(obj)

    @staticmethod
    def run_shark(obj):
        Run._reproduction(obj) or Run._eat(obj) or Run._dead(obj) or Run._move(obj)

    @staticmethod
    def _reproduction(obj):
        ocean = obj.ocean
        size = ocean.size
        x, y = obj.x, obj.y

        if obj.has_child():
            shifts = [(xs, ys) for xs in [-1, 0, 1] for ys in [-1, 0, 1] if xs or ys]
            random.shuffle(shifts)

            for xs, ys in shifts:
                new_x, new_y = (x + xs) % size, (y + ys) % size
                cell = ocean.get_cell(new_x, new_y)

                if isinstance(cell, Water):
                    obj_child = obj.__class__(ocean, new_x, new_y)
                    ocean.set_cell(new_x, new_y, obj_child)

                    obj.inc_reproduction()

                    if hasattr(obj, 'dec_fullness'):
                        obj.dec_fullness()

                    return True

        return False

    @staticmethod
    def _move(obj):
        ocean = obj.ocean
        size = ocean.size
        x, y = obj.x, obj.y

        shifts = [(xs, ys) for xs in [-1, 0, 1] for ys in [-1, 0, 1]]
        random.shuffle(shifts)

        for xs, ys in shifts:
            new_x, new_y = (x + xs) % size, (y + ys) % size
            cell = ocean.get_cell(new_x, new_y)

            if isinstance(cell, Water):
                obj.x, obj.y = new_x, new_y

                ocean.set_cell(obj.x, obj.y, obj)
                ocean.set_cell(x, y, cell)

                obj.dec_reproduction()

                if hasattr(obj, 'dec_fullness'):
                    obj.dec_fullness()

                return True

        return False

    @staticmethod
    def _eat(obj):
        ocean = obj.ocean
        size = ocean.size
        x, y = obj.x, obj.y

        shifts = [(xs, ys) for xs in [-1, 0, 1] for ys in [-1, 0, 1]]
        random.shuffle(shifts)

        for xs, ys in shifts:
            new_x, new_y = (x + xs) % size, (y + ys) % size
            cell = ocean.get_cell(new_x, new_y)

            if isinstance(cell, Guppies):
                obj.x, obj.y = new_x, new_y

                ocean.set_cell(obj.x, obj.y, obj)
                ocean.set_cell(x, y, Water())

                obj.dec_reproduction()
                obj.inc_fullness()

                return True

        return False

    @staticmethod
    def _dead(obj):
        ocean = obj.ocean
        x, y = obj.x, obj.y

        if obj.is_dead():
            ocean.set_cell(x, y, Water())


def generate_ocean():
    size = 100
    weighted_choices = [(Shark, 2), (Guppies, 30), (Land, 10), (Water, 57)]
    population = [val for val, cnt in weighted_choices for _ in range(cnt)]
    choices = [random.choice(population) for _ in range(size * size)]

    ocean = Ocean(size)

    for idx, cls in enumerate(choices):
        x, y = divmod(idx, size)
        cell = cls(ocean, x, y)
        ocean.set_cell(x, y, cell)

    return ocean


def read_ocean():
    pass


def write_ocean():
    pass

