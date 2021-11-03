def f(x): return x%3 == 0 or x%5 == 0
print(sum(filter(f, range(1, 1000))))
