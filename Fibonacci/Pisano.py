def GetPisano(m):
    # In number theory, the nth Pisano period, written π(n),
    # is the period with which the sequence of Fibonacci
    # numbers taken modulo n repeats.
    # GetPisano(m) returns the length of the Pisano period.
    if m == 1:
        return 1
    a, b, c = 0, 1, 0
    for x in range(2, m**3):
        c = (a+b) % m
        a, b = b, c
        if a == 1 and b == 0:
            return x


def main():
    n = int(input())
    print(GetPisano(n))


if __name__ == "__main__":
    main()
