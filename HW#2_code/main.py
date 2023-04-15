import numpy as np

# this is the T() function,
def funT(x):
    return 2 * (x + (x**3)/3 + (x**5)/5 + (x**7)/7 + (x**9)/9)

# the x value may differe according to difference in the f(x) function
x = 0.49/2.49

# the value inside log may differ so check your HW
y = np.log(1.49)
# the value here is related to the x above
y_hat = funT(x)

print("y\":",y_hat)

AE = abs(y-y_hat)		# absolute Error
RE = abs(y-y_hat) / y 	# Relative Error

print("AE: ",AE)
print("RE: ",RE)


# the code below is to check for the Significant digits 
# by the way double check your SD value, this code below may result in Error
try:
    SD = abs(int(str(RE).split('e')[1]))
    print("SD: ",SD - 1)
except Exception as e:
    nu = str(RE).split('.')[1]
    sig=0
    for i in range(len(nu)):
        if int(nu[i]) == 0:
            sig+=1
        elif int(nu[i]) != 0 and int(nu[i]) > 5:
            sig+=1
            break
        elif int(nu[i]) != 0:
            break