import numpy as np

def baby(n):
  if n==0:
    return 85
  else:
    return (1/2) * (baby(n-1) + (857/baby(n-1)))

Xn = np.sqrt(857)

for i in range(10):
  if i>=1 and baby(i) == baby(i-1):
    print("\nXn**2: ",baby(i)**2)
    break
  print(i,"\t", round(baby(i) , 6))


print("sqrt(Xn**2) : ", Xn)