n = int(input())
count = 0
while(count < 6):
    if n % 2 != 0:
        count += 1
        print(n)
    n += 1
