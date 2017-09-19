def get_sequence_item(k):
    t = 0
    for i in range(1, k + 1):
        bias = (1 << (1 << (i - 1)))
        t = t * bias + (~t & (bias - 1))
    return bin(t)
