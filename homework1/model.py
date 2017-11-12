import random
import json


class Shark:
    FULLNESS = 20
    REPRODUCTION = 100
    LIFE = 250

    def __init__(self, ocean, x, y):
        # type: (Ocean, int, int) -> None

        self._fullness = Shark.FULLNESS
        self._reproduction = Shark.REPRODUCTION
        self._life = Shark.LIFE
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

    def inc_fullness(self):
        self._fullness = Shark.FULLNESS

    def dec_fullness(self):
        self._fullness = max(0, self._fullness - 1)

    def is_dead(self):
        return self._fullness == 0 or self._life == 0

    def inc_reproduction(self):
        self._reproduction = Shark.REPRODUCTION

    def dec_reproduction(self):
        self._reproduction = max(0, self._reproduction - 1)

    def has_child(self):
        return self._reproduction == 0

    def dec_life(self):
        self._life = max(0, self._life - 1)

    def percent_life(self):
        return min(self._life / Shark.LIFE, self._fullness / Shark.FULLNESS)

    @classmethod
    def set_fullness(cls, fullness):
        cls.FULLNESS = fullness

    @classmethod
    def set_reproduction(cls, reproduction):
        cls.REPRODUCTION = reproduction

    @classmethod
    def set_life(cls, life):
        cls.LIFE = life


class Guppies:
    REPRODUCTION = 2
    LIFE = 200

    def __init__(self, ocean, x, y):
        # type: (Ocean, int, int) -> None

        self._reproduction = Guppies.REPRODUCTION
        self._life = Guppies.LIFE
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

    def inc_reproduction(self):
        self._reproduction = Shark.REPRODUCTION

    def dec_reproduction(self):
        self._reproduction = max(0, self._reproduction - 1)

    def has_child(self):
        return self._reproduction == 0

    def is_dead(self):
        return self._life == 0

    def dec_life(self):
        self._life = max(0, self._life - 1)

    def percent_life(self):
        return self._life / self.LIFE

    @classmethod
    def set_reproduction(cls, reproduction):
        cls.REPRODUCTION = reproduction

    @classmethod
    def set_life(cls, life):
        cls.LIFE = life


class Land:
    def __new__(cls, *args, **kwargs):
        if not hasattr(Land, '__instance'):
            Land.__instance = object.__new__(cls)

        return Land.__instance


class Water:
    def __new__(cls, *args, **kwargs):
        if not hasattr(Water, '__instance'):
            Water.__instance = object.__new__(cls)

        return Water.__instance


class Ocean:
    DEFAULT_SIZE = 100

    def __init__(self, size=None):
        self._size = size or Ocean.DEFAULT_SIZE
        self._map = [[None] * self._size for _ in range(self._size)]

    def __iter__(self):
        for row in self._map:
            for cell in row:
                yield cell

    def get_cell(self, i, j):
        return self._map[i][j]

    def set_cell(self, i, j, value):
        self._map[i][j] = value

    def is_dead(self):
        for row in self._map:
            for cell in row:
                if isinstance(cell, (Shark, Guppies)):
                    return False

        return True

    @property
    def size(self):
        return self._size

    @classmethod
    def set_default_size(cls, size):
        cls.DEFAULT_SIZE = size


class Strategy:
    @staticmethod
    def run_ocean(ocean):
        for obj in ocean:
            if isinstance(obj, Shark):
                Strategy.run_shark(obj)

        for obj in ocean:
            if isinstance(obj, Guppies):
                Strategy.run_guppies(obj)

        # ocean.inc_time()

    @staticmethod
    def run_guppies(obj):
        Strategy._dead(obj) or \
        Strategy._reproduction(obj) or \
        Strategy._move(obj) or \
        obj.dec_reproduction() or \
        obj.dec_life()

    @staticmethod
    def run_shark(obj):
        Strategy._dead(obj) or \
        Strategy._reproduction(obj) or \
        Strategy._eat(obj) or \
        Strategy._move(obj) or \
        obj.dec_reproduction() or \
        obj.dec_life() or \
        obj.dec_fullness()

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
                    obj.dec_life()

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
                obj.dec_life()

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
                obj.dec_life()
                obj.inc_fullness()

                return True

        return False

    @staticmethod
    def _dead(obj):
        ocean = obj.ocean
        x, y = obj.x, obj.y

        if obj.is_dead():
            ocean.set_cell(x, y, Water())

            return True

        return False


def init(filename):
    with open(filename) as f:
        str_json = f.read()
        config = json.loads(str_json)

        size = config.get("size")
        if size is not None:
            Ocean.set_default_size(size)

        shark_config = config.get("shark")
        if shark_config is not None:
            Shark.set_fullness(shark_config.get("fullness", Shark.FULLNESS))
            Shark.set_life(shark_config.get("life", Shark.LIFE))
            Shark.set_reproduction(shark_config.get("reproduction", Shark.REPRODUCTION))

        guppies_config = config.get("guppies")
        if guppies_config is not None:
            Guppies.set_reproduction(guppies_config.get("reproduction", Guppies.REPRODUCTION))
            Guppies.set_life(guppies_config.get("life", Guppies.LIFE))


def generate_ocean(size=None):
    size = size or Ocean.DEFAULT_SIZE

    weighted_choices = [(Shark, 2), (Guppies, 30), (Land, 10), (Water, 57)]
    population = [val for val, cnt in weighted_choices for _ in range(cnt)]
    choices = [random.choice(population) for _ in range(size * size)]

    ocean = Ocean(size)

    for idx, cls in enumerate(choices):
        x, y = divmod(idx, size)
        cell = cls(ocean, x, y)
        ocean.set_cell(x, y, cell)

    return ocean


def read_ocean(filename, size=None):
    ocean = Ocean(size)

    map_symbols = {
        '*': Water,
        '#': Land,
        'S': Shark,
        'G': Guppies,
    }

    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, s in enumerate(line.strip()):
                cls = map_symbols[s]
                ocean.set_cell(i, j, cls(ocean, i, j))

    return ocean


def write_ocean(filename, ocean):
    size = ocean.size

    map_class = {
        Water: '*',
        Land: '#',
        Shark: 'S',
        Guppies: 'G',
    }

    with open(filename, 'w') as f:
        for idx, cell in enumerate(ocean):
            x, y = divmod(idx, size)
            s = map_class[cell.__class__]
            f.write(s + '\n' if y == size - 1 else s)


def run(ocean, num_it):
    if num_it is not None:
        for _ in range(num_it):
            Strategy.run_ocean(ocean)
    else:
        while True:
            Strategy.run_ocean(ocean)
            if ocean.is_dead():
                break
