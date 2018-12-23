# write the function definition and import all the necessary module
import math

def trapezoidal(a, b):
    return round((b-a)*(f(b)+f(a))/2, 2)

def f(x):
    return (x**3)*math.exp(-1)

print(trapezoidal(5, 6.5))
print(trapezoidal(5, 5.5))
print(trapezoidal(6,6.5))
print(trapezoidal(6,2.5))