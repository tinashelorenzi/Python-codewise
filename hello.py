import math

a = 1
b = 2
c = 1

under_root = b*b - 4*a*c
numerator1 = -b + math.sqrt(under_root)
numerator2 = -b - math.sqrt(under_root)
denominator = 2*a

x1 = numerator1/denominator
x2 = numerator2/denominator

print("X1 is",x1)
print("X2 is",x2)