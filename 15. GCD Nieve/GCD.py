def GCD(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
        print('a: ', a, 'b: ', b, 't: ', t)
    return a


print(GCD(60, 96))
print(GCD(20, 8))
