def e_approx(n):
    e = f = 1
    m = n + 1
    for i in range(2, m+1):
        e += 1 / f
        f *= i
    return e


