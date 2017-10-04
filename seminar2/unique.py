
def compress(ar):
    pair_counts = {}

    for a in ar:
        # can pair_counts.set_default
        pair_counts[a] = pair_counts.get(a, 0) + 1

    return list(pair_counts.items())
