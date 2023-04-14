import numpy as np
from rounding import rounding as rnd        # rounding.py is in the same folder, its pupose is to round according to FPA


# defining the function
def fun_(x):
    return x**6 - 2*x**5 - 3*x**4 + 4*x**3 - 5*x**2 + 6*x + -7

# custom printing function
def printing(a, alpb, b):
    a = round(a, 10)
    if alpb == 0:       # if the value is 0 and i round it it will return 1, so therefore i have to check if it is 0 and if it is i will return 0
        alpb = 0
    else:
        alpb= round(alpb, 10)
    b = round(b, 10)
    # RE = round(RE, 10)        # since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
    print(a,"\t||\t", alpb,"\t||\t", b)



# main function
def horners(alpha):
    coef = [1, -2, -3, 4, -5, 6, -7]
    b0 = 0
    # print(coef[0],"\t||\t", 0,"\t||\t", b0)

    for a in coef:
        alpb = rnd(alpha*b0,  7)[-1]
        b = rnd(a + alpb, 7)[-1]
        printing(a, alpb, b)
        b0 = b
        
        
horners(-1.15)