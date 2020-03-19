import GCD as GCD


def GetLcm(a, b):
    return int(a*b/GCD.EuclidGCD(a, b))


print(GetLcm(21, 6))

MAXN = 10
spf = [0 for i in range(MAXN)]
print(spf)
