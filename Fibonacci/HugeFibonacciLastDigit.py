from Fibonacci import GetFibonacci
from Pisano import GetPisano


def GetFibonacciLastDigit(n, m):
    r = n % GetPisano(m)
    return GetFibonacci(r) % m


print(GetFibonacciLastDigit(2816213588, 239))
