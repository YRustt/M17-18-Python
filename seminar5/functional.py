
import os
from collections import Iterable, OrderedDict
from itertools import starmap, chain
from operator import mul


def get_value(obj):
    return int(obj, 0) if isinstance(obj, str) else obj


def scalar_product(first_iterable, second_iterable):
    try:
        return sum(starmap(mul, zip(map(get_value, first_iterable), map(get_value, second_iterable))))
    except ValueError:
        return None


def flatten(iterable):
    it = iter(iterable)

    while it:
        el = next(it)

        if isinstance(el, Iterable) and not isinstance(el, str):
            it = chain(el, it)
        else:
            yield el


def walk_files(path):
    tree = OrderedDict()

    for root, dirs, files in os.walk(path):
        tree[root] = files + [walk_files(os.path.join(root, d)) for d in dirs]

    return tree
