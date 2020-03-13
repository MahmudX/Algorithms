def evenOrOdd(n):
    return "EVEN" if n % 2 == 0 else "ODD"


for n in range(int(input())):
    x = int(input())
    if x == 0:
        print("NULL")
    elif x < 0:
        print(evenOrOdd(x), "NEGATIVE")
    else:
        print(evenOrOdd(x), "POSITIVE")
