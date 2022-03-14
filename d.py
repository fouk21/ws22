import math

print ("Ax^2 + Bx +C = 0")
A = float(input("A="))
B = float(input("B="))
C = float(input("C="))

D = B**2 - 4*A*C
if D < 0 :
    print("no real solutions")
elif D == 0:
    x = -B /2*A
    print (f"x = {x}")
else:
    x1 = (-B + math.sqrt(D)) / 2*A
    x2 = (-B - math.sqrt(D)) / 2*A
    print (f"x1 , x2 = {x1},{x2}")