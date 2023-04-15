import numpy as np
from sig_digits import sig_digits as sd
from rounding import rounding as rnd


# this is the T() function,
def funT(x):
  return 2 * (x + (x**3) / 3 + (x**5) / 5 + (x**7) / 7 + (x**9) / 9)

def RE(y, y_hat):
  return abs(abs(y - y_hat) / y)


# the x value may differe according to difference in the f(x) function
x = -0.3 / 1.7

# the value inside log may differ so check your HW
y = np.log(0.7)
# the value here is related to the x above
y_hat = funT(x)

print("y\":", round(y_hat,6))
print("y: ", round(y,6))

AE = rnd(abs(y - y_hat), 6)[-1]  # absolute Error
RE1 = rnd(RE(y, y_hat), 6)[-1]  # Relative Error

print("AE: ", AE)
print("RE: ", RE1)
print("SD: ", sd(RE1)[-1])











# OUT OF ORDER

# the code below is to check for the Significant digits
# by the way double check your SD value, this code below may result in Error
# try:
#   SD = abs(int(str(RE).split('e')[1]))
#   print("SD: ", SD)
# except Exception as e:
#   nu = str(RE).split('.')[1]
#   sig = 0
#   for i in range(len(nu)):
#     if int(nu[i]) == 0:
#       sig += 1
#     elif int(nu[i]) != 0 and int(nu[i]) > 6:
#       sig += 1
#       break
#     elif int(nu[0]) != 0 and int(nu[i]) < 6:
#       sig=2
#       break
#     elif int(nu[i]) != 0:
#       break
