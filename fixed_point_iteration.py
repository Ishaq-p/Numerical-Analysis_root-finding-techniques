import numpy as np
import rounding as rnd


def func(x):
    return (x**3)/17 + (x**2)/13 + 1/3

def RE(x1, x0):
    return abs((x1 - x0)/x1)



def fixed_point(x0, criterion):
    interations = 0
    x1 = rnd.rounding(func(x0),7)[-1]
    RE = rnd.rounding(abs((x1 - x0)/x1),7)[-1]
    print(x0,"\t||\t", x1,"\t||\t", RE)

    while abs(x1 - x0) > criterion:
        x0 = x1
        x1 = rnd.rounding(func(x0),7)[-1]
        RE = rnd.rounding(abs((x1 - x0)/x1),7)[-1]


        print(x0,"\t||\t", x1,"\t||\t", RE)
        interations += 1

    return x1, f"iterarions: {interations}"

print(fixed_point(1, 1e-5))