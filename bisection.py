import numpy as np
from rounding import rounding as rnd


def f_(x):
    return 3.64*x * (1 - x**2 + x)*np.log(x) - x**2 +1
    # return x**3 + 2*x**2 - (41*x) - 32

def p_(a,b):
    return (a+b)/2

def sign_(a,p):
    if f_(a)*f_(p) > 0:
        return True,'+'
    elif f_(a)*f_(p)<0:
        return False, '-'

def RE_(p1, p0):
    return abs((p1 - p0)/p1)

def printing(a, p, b, sign, RE):
    a = round(a, 10)
    b = round(b, 10)
    p = round(p, 10)
    # RE = round(RE, 10)        // since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
    print(a,"\t||\t", p,"\t||\t", b,"\t||\t",sign,"\t||\t", RE)



def bisect(f, a, b, p0, tol=1e-3, fpa=7):
    """Find root of f(x) = 0 on interval [a,b] to within tolerance tol."""
    if f(a)*f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    while RE_(b, a) > tol:
        p1 = rnd(p_(a,b), fpa)[-1]
        sign = sign_(a,p1)
        RE = rnd(RE_(p1,p0), fpa)[-1]

        printing(a, p1, b, sign[1], RE)

        if sign[0]:
            a = p1
        else:
            b = p1
        p0 = p1

    p1 = rnd(p_(a,b), fpa)[-1]
    sign = sign_(a,p1)
    RE = rnd(RE_(p1,p0), fpa)[-1]
    printing(a, p1, b, sign[1], RE)



print(bisect(f_, a=0.05, b=0.5, p0=0.05, fpa=6))


