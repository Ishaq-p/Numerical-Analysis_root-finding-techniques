from rounding import rounding as rnd
import numpy as np

def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n - 1)
  
def twisted_sum(a, b, FPN):
    a = rnd(a, FPN)[-1]
    b = rnd(b, FPN)[-1]  
    return rnd(a + b, FPN)

def twisted_sub(a, b, FPN):
    a = rnd(a, FPN)[-1]
    b = rnd(b, FPN)[-1]  
    return rnd(a - b, FPN)

def twisted_mul(a, b, FPN):
    a = rnd(a, FPN)[-1]
    b = rnd(b, FPN)[-1]  
    return rnd(a * b, FPN)

def twisted_div(a, b, FPN):
    a = rnd(a, FPN)[-1]
    b = rnd(b, FPN)[-1]  
    return rnd(a / b, FPN)

def fun_Z(n):
    if n == 0:
      return 1
    else:   return twisted_sum(fun_Z(n-1), 3.43**n / fact(n), 6)[-1]

for i in range(0,20):
    if i>=2 and fun_Z(i-1) == fun_Z(i-2):
        break
    print("n: ",i,"\t", f"Z({i}): ", fun_Z(i))

print("e^3.43: ", np.e**3.43)





























# OUT OF ORDER

# import numpy as np

# e = np.e**2.81

# def fact(n):
#   if n == 1:
#     return 1
#   else:
#     return (n * fact(n - 1))

# def exp(x):
#   result = str(round((2.81**x) / fact(x)))
#   if len(result.split('.')[0])==1:
#     return round(float(result), 5)
#   return round(float(result), 4)

# def round_(x, n):
#   re = x.split('.')[0]
#   if re ==1:
#     return round(x, n-1)
#   return round(x,n)

# def Z(x):
#   if x == 0:
#     return 1
#   else:
#     return round_(round(Z(x - 1), 4) + exp(x), 5)

# for i in range(0,20):
#   if i>=2 and Z(i-1) == Z(i-2):
#     break
#   print("n: ",i,"\t", f"Z({i}): ", round(Z(i), 6))

# print("\ne^(2.81): \t\t", round(e,6))
