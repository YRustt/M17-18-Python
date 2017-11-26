
from unittest import TestCase

from .functional import (
    scalar_product,
    flatten
)


class ScalarProductTests(TestCase):
    def test_1(self):
        expected = 1
        actual = scalar_product([1, '2'], [-1, 1])
        self.assertEqual(expected, actual)

    def test_2(self):
        expected = None
        actual = scalar_product([1, 'abc'], [-1, 1])
        self.assertIs(expected, actual)

    def test_3(self):
        expected = 1
        actual = scalar_product([1, '0x2'], [-1, '0o1'])
        self.assertEqual(expected, actual)


class FlattenTests(TestCase):
    def test_1(self):
        expected = [1, 2, 0, 1, 1, 2, 1, 'ab']
        actual = flatten([1, 2, range(2), [[], [1], [[2]]], (x for x in [1]), 'ab'])
        self.assertEqual(expected, list(actual))
