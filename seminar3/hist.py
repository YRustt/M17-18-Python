
def distribute(ar, k):
    _min, _max = min(ar), max(ar)
    step = (_max - _min) / k
    hist = [0] * k

    for a in ar:
        idx = int((a - _min) / step)

        if a == _max:
            idx -= 1

        hist[idx] += 1

    return hist


def print_distribute(hist):
    _max = max(hist)

    for i in range(_max):
        print(''.join(['{: ^3}'.format('*' if h >= _max - i else ' ') for h in hist]))


if __name__ == '__main__':
    print_distribute(distribute(
        [1, 1,
         2, 2,
         3, 3,
         4, 4, 4, 4,
         5, 5, 5, 5,
         6, 6, 6, 6, 6, 6, 6, 6,
         7, 7, 7, 7, 7, 7, 7, 7,], 2))
