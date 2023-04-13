def f(x):
    return x**3 + 2*x**2 - (41*x) - 32

def bisect(f, a, b, tol=1e-3):
    """Find root of f(x) = 0 on interval [a,b] to within tolerance tol."""
    if f(a)*f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    while abs(b - a) > tol:
        c = (a + b)/2
        if f(c) == 0:
            return c
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return (a + b)/2

print(bisect(f, -8, -7))


