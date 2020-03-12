def firstDuplicate(intArr):
    for x in intArr:
        index = abs(x) - 1
        if intArr[index] < 0:
            return abs(x)
        intArr[index] *= -1
    return -1


arr = [8, 8, 6, 2, 6, 4, 7, 9, 5, 8]
print(firstDuplicate(arr))
