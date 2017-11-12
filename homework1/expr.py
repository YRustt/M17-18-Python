"""
    Py3
"""

from typing import (
    Optional,
    Union,
    Callable,
    List
)


Variable = Union[int, float]
Function = Callable[[Variable, Variable], Variable]


OPERATORS = ['+', '-', '*', '/', '**', '(', ')', 'END']
PRIORITIES = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '**': 3,
    '(': 0,
    ')': 0,
    'END': -1,
}


def _is_operator(token):
    # type: (str) -> bool

    return token in OPERATORS


def _map_operator(token):
    # type: (str) -> Optional[Function]

    if token == '+':
        return lambda x, y: x + y
    elif token == '-':
        return lambda x, y: x - y
    elif token == '*':
        return lambda x, y: x * y
    elif token == '/':
        return lambda x, y: float(x) / float(y)
    elif token == '**':
        return lambda x, y: x ** y
    elif token in ('(', ')', 'END'):
        return None
    else:
        raise ValueError('Invalid token')


def _comp(token, op):
    # type: (str, str) -> bool

    if token == ')':
        return True if op != '(' else False
    elif token in ('(', '**'):
        return False
    elif token == 'END':
        return True

    return PRIORITIES[op] >= PRIORITIES[token]


def _pop_operations(token, Q, W):
    # type: (str, List[Variable], List[str]) -> None

    while W and _comp(token, W[-1]):
        op = W.pop()
        func = _map_operator(op)

        if func is not None:
            B = Q.pop()
            A = Q.pop()
            Q.append(func(A, B))


def _map_number(token):
    # type: (str) -> Variable

    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            raise ValueError('Invalid token')


def _tokenize(expr):
    # type: (str) -> List[str]

    expr = "{} END".format(expr.strip())

    return expr.split()


def interpreter(expr):
    # type: (str) -> Variable

    tokens = _tokenize(expr)
    Q, W = [], []

    for token in tokens:
        if _is_operator(token):
            _pop_operations(token, Q, W)
            W.append(token)
        else:
            Q.append(_map_number(token))

    return Q[0]


if __name__ == '__main__':
    while True:
        try:
            line = input()
            print(interpreter(line))
        except KeyboardInterrupt:
            break
