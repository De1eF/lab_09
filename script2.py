A = set(range(101, 250))

T = set(n for n in A if n % 3 == 0)

T6 = set(n for n in T if n % 6 == 0)

print(T6)
