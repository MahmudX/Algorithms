inp = list(map(int, input().split()))
A = inp[0]
B = inp[1]
C = inp[2]
D = inp[3]
if B > C and D > A and (C + D) > (A + B) and C >= 0 and D >= 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
