inp = list(map(int, input().split()))
prices = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
print("Total: R$ %.2f" % (prices[inp[0]] * inp[1]))
