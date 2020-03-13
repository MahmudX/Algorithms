cin = 0
cout = 0
for x in range(int(input())):
    i = int(input())
    if (i >= 10 and i <= 20):
        cin += 1
    else:
        cout += 1
print(cin, "in")
print(cout, "out")
