sum = 0
X = int(input())
Y = int(input())
if Y < X:
    temp = Y
    Y = X
    X = temp
for i in range(X+1, Y):
    if i % 2 != 0:
        sum += i
print(sum)
