output = []
inputArr = [1, 1, 2, 2, 3, 3, 4, 4]
for x in inputArr:
    index = abs(x) - 1
    if inputArr[index] < 0:
        output.append(index + 1)
    inputArr[index] = inputArr[index] * -1
print(output)
