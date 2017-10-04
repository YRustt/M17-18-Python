
def get_primes(n: int) -> set:
    return [t for t in range(2, n) if all(False if t % p == 0 else True for p in range(2, round(t ** 0.5) + 1))]
    # return set(range(2, n)) - {t for t in range(2, n) for p in range(2, round(t ** 0.5) + 1) if t % p == 0}
