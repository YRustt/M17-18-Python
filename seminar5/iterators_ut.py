import unittest

from .iterators import (
    unique,
    transpose
)


class UniqueTests(unittest.TestCase):
    def test_1(self):
        expected = [1, 2, 3]
        actual = unique([1, 2, 1, 3, 2])
        self.assertEqual(expected, list(actual))


class TransposeTests(unittest.TestCase):
    def test_1(self):
        expected = [[1, 2], [-1, 3]]
        actual = transpose([[1, -1], [2, 3]])
        self.assertEqual(expected, list(map(list, actual)))

    def test_2(self):
        expected = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        actual = transpose([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        self.assertEqual(expected, list(map(list, actual)))

    def test_3(self):
        expected = [[1], [2], [3]]
        actual = transpose([[1, 2, 3]])
        self.assertEqual(expected, list(map(list, actual)))
