import numpy as np
from rounding import rounding as rnd        # rounding.py is in the same folder, its pupose is to round according to FPA


# defining the function
def func(x):
    return (x**3)/16 + (x**2)/6 + 1/5

# defining the RE, Relative Error
def RE_(x1, x0):
    
    return abs((x1 - x0)/x1)

# custom printing function
def printing(x0, x1, RE):
    x0 = round(x0, 10)
    x1 = round(x1, 10)
    # RE = round(RE, 10)        # since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
    print(x0,"\t||\t", x1,"\t||\t", RE)



# main function
def fixed_point(x0, criterion):
    interations = 0
    # rnd1 = rnd.rounding()

    # first iteration
    x1 = rnd(func(x0),7)[-1]
    RE = rnd( RE_(x1,x0) ,7)[-1]
    printing(x0, x1, RE)

    # the middle iterations
    while abs(x1 - x0) > criterion:
        x0 = x1
        x1 = rnd(func(x0),7)[-1]
        RE = rnd( RE_(x1,x0) ,7)[-1]

        printing(x0, x1, RE)
        interations += 1
    
    # the last iteration
    # x0 = x1
    # x1 = rnd(func(x0),7)[-1]
    # RE = rnd( RE_(x1,x0) ,7)[-1]
    # printing(round(x0,10), x1, RE)
    # interations += 1

    return x1, f"iterarions: {interations}"


print(fixed_point(1, 1e-5))