n = int(input())
x = list(map(int, input().split()))
x.pop(0)
y = list(map(int, input().split()))
y.pop(0)
z = list(set(x) | set(y))
z.sort()
ln = len(z)
if ln == 0 or n > z[ln - 1] or ln < n:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")
