def set_bit(num, k):
    return num | (1 << k)


def clear_bit(num, k):
    return num ^ (1 << k) if test_bit(num, k) else num


def test_bit(num, k):
    return (num & (1 << k)) != 0
