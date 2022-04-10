from matplotlib import pyplot as plt
from math import sqrt

plotsize = 10
X = list(range(-plotsize, plotsize + 1))
fig, ax = plt.subplots()


def addplot (A, B, C):
    label = f"(A,B,C): ({A}, {B}, {C})"
    Y = []
    for x in X:
        Y.append(A * x * x + B * x + C)
    ax.plot(X, Y, label=label)

    
def calculate (A, B, C):
    D = (B * B) - (4 * A * C)
    if D < 0.0 :
        print("No real roots")
    elif D == 0.0:
        x = -B / (2 * A)
        print (f"Double root is x = {x}")
    else:
        x1 = (-B + sqrt(D)) / (2 * A)
        x2 = (-B - sqrt(D)) / (2 * A)
        print (f"Real roots are: x1 = {x1:.3f}, x2 = {x2:.3f}")


N = int(input("How many equations? "))

for i in range(1, N + 1):
    print (f"\n{i}) Ax^2 + Bx + C = 0")
    A = float(input("A="))
    B = float(input("B="))
    C = float(input("C="))

    calculate(A, B, C)
    addplot(A, B, C)

ax.grid()
ax.legend()
plt.show()
