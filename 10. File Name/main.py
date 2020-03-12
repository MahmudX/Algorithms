n = int(input())
s = str(input())
removal = 0
counter = 0
for x in s:
    if x != 'x':
        if counter >= 3:
            removal += counter - 2
        counter = 0
    elif x == 'x':
        counter += 1
if counter >= 3:
    removal += counter - 2
print(removal)
