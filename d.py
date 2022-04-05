import math
from matplotlib import pyplot as plt

plotsize = 10
X = list(range(-plotsize,plotsize+1))
fig, ax = plt.subplots()

def addplot (A,B,C):
    Y = []

    for x in X:
        Y.append(A*x**2+B*x+C)
    ax.plot(X,Y)
def calculate (A,B,C):

    D = B**2 - 4*A*C
    if D < 0.0 :
        print("no real solutions")
    elif D == 0.0:
        x = -B /2*A
        print (f"x = {x}")
    else:
        x1 = (-B + math.sqrt(D)) / 2*A
        x2 = (-B - math.sqrt(D)) / 2*A
        print (f"x1 , x2 = {x1},{x2}")

N = int(input("How many equations? "))

for i in range(N):
    print (i+1, ": Ax^2 + Bx +C = 0")
    A = float(input("A="))
    B = float(input("B="))
    C = float(input("C="))

    calculate(A,B,C)
    addplot(A,B,C)

plt.show()