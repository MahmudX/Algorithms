from math import sqrt


def GetFibonacciList(n):
    # Returns the list of Fibonacci numbers from 0 to n
    output = [0, 1]
    for x in range(2, n+1):
        output.append((output[x-1]+output[x-2]))
    return output


def GetFibonacciNumber_matrix(n):
    # Returns nth Fibonacci number using Matrix Formula
    sqrt5 = sqrt(5)
    fibNth = int(((1/sqrt5)*((1+sqrt5)/2)**n) - ((1/sqrt5)*((1-sqrt5)/2)**n))
    return fibNth


def GetFibonacciNumber_naive(n):
    # Returns nth Fibonacci number using Naive algorithm
    # Too much unefficient
    if(n <= 1):
        return n
    return GetFibonacciNumber_naive(n - 1) + GetFibonacciNumber_naive(n - 2)


def GetFibonacci(n):
    # Returns nth Fibonacci number using DP
    # a = n(0)
    # b = n(1)
    a = output = 0
    b = 1
    for x in range(2, n + 1):
        output = a + b
        a, b = b, output
    return output


def GetFibonacciLastDigitList(n):
    # Returns a list of Fibonacci numbers' last digit from 0 to n DP
    output = [0, 1]
    for x in range(2, n+1):
        output.append((output[x-1]+output[x-2]) % 10)
    return output


def GetFibonacciLastDigit(n):
    # Returns nth Fibonacci numbers' last digit using DP
    return GetFibonacci(n) % 10


def main():
    n = int(input("Enter a range: "))
    print(GetFibonacciLastDigit(n))


if __name__ == "__main__":
    main()
