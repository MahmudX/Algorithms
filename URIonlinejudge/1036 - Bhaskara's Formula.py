import math as math
inp = list(map(float, input().split()))
A = inp[0]
B = inp[1]
C = inp[2]
D = ((B**2) - 4 * A*C)
if A == 0 or D <= 0:
    print("Impossivel calcular")
else:
    D = math.sqrt(D)
    E = (2 * A)
    R1 = (-B + D) / E
    R2 = (-B - D) / E
    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)
