calculate_gcd = lambda m, n: abs(m) if not n else calculate_gcd(n, m % n)
