n = int(input())
threes = twos = 0
if n % 2 != 0:
    threes = 1
    n -= 3
    twos += int(n/2)
else:
    twos = int(n/2)
print(twos+threes)
print(("2 "*twos).strip(), "3"*threes)
