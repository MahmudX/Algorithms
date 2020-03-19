import math as math
import random as random
import sys as sys
sys.setrecursionlimit(1000000000)


def EuclidGCD(a, b):
    if b == 0:
        return a
    return EuclidGCD(b, a % b)


def stressTest():
    # Stress Test
    while True:
        randOne = random.randrange(
            100000, 100000000000000000000000000000000000000000)
        randTwo = random.randrange(
            100000, 100000000000000000000000000000000000000000)
        print(randOne)
        print(randTwo)
        Niev = math.gcd(randOne, randTwo)
        fast = EuclidGCD(randOne, randTwo)
        print("Fast GCD: ", fast)
        print("Niev GCD: ", Niev)
        if fast != Niev:
            break


def main():
    a = int(input("First Nummber: "))
    b = int(input("Second Nummber: "))
    print("GCD of A and B: ", EuclidGCD(a, b))


if __name__ == "__main__":
    main()
