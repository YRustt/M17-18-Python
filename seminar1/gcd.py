calculate_gcd = lambda m, n: m if not n else calculate_gcd(n, m % n)
# Мб нужно abs(m)
