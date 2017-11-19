
from typing import (
    TypeVar,
    Generic,
    Iterable
)


T = TypeVar('T')


class MidSkipQueue(Generic[T]):
    def __init__(self, k, it):
        # type: (int, Iterable[T]) -> None

        if not isinstance(k, int):
            k = int(k)

        if k <= 0:
            raise ValueError("Not valid value for k")

        self._queue = [None] * (2 * k)
        self._cur_idx = 2 * k - 1
        self._k = k
        self._len = 0

        self.__add__(it)

    def append(self, *args):
        for el in args:
            self._queue[self._cur_idx] = el
            self._next_cur_idx()
            self._next_len()

    def _next_len(self):
        # type: () -> None

        self._len = min(self._len + 1, 2 * self._k)

    def _next_cur_idx(self):
        # type: () -> None

        self._cur_idx -= 1
        if self._cur_idx < 0:
            self._cur_idx = self._k - 1

    def __eq__(self, other):
        pass

    def __add__(self, it):
        # type: (Iterable[T]) -> None

        for el in it:
            self.append(el)

    def __len__(self):
        # type: () -> int

        return self._len

    def __str__(self):
        pass

    def __repr__(self):
        return str(self)
