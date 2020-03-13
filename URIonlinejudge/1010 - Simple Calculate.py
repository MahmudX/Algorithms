uInputOne = list(map(float, (input().split())))
uInputTwo = list(map(float, (input().split())))
result = (uInputOne[1] * uInputOne[2]) + (uInputTwo[1] * uInputTwo[2])
print("VALOR A PAGAR: R$ %.2f" % result)
