
import inspect
import timeit

from typing import (
    TypeVar,
    Callable
)
from functools import (
    wraps
)
from collections import OrderedDict


T = TypeVar('T')


def _get_key(f, args, kwargs):
    arg_names = f.__code__.co_varnames
    defaults = f.__defaults__

    d_key = OrderedDict((name, None) for name in arg_names)

    for name, value in zip(arg_names[::-1], defaults[::-1]):
        d_key[name] = value

    for name, value in kwargs.items():
        d_key[name] = value

    for name, value in zip(arg_names, args):
        d_key[name] = value

    return tuple(d_key.items())


def memorize(f):
    cache = {}

    @wraps(f)
    def wrapper(*args, **kwargs):
        key = _get_key(f, args, kwargs)

        if cache.get(key) is None:
            cache[key] = f(*args, **kwargs)

        return cache.get(key)

    return wrapper


def profile(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        res = [None,]
        print(timeit.timeit(
            "res[0] = f(*args, **kwargs)",
            number=10,
            globals={'f': f, 'args': args, 'kwargs': kwargs, 'res': res}
        ))
        return res[0]

    return wrapper


class convolve:
    def __init__(self, k):
        # type: (int) -> None

        if not isinstance(k, int) or k <= 0:
            raise ValueError("Not valid value for k")

        self._k = k

    def __call__(self, f):
        # type: (Callable[[T], T]) -> Callable[[T], T]

        @wraps(f)
        def wrapper(arg):
            # type: (T) -> T

            tmp = f(arg)
            for _ in range(1, self._k):
                tmp = f(tmp)

            return tmp

        return wrapper
