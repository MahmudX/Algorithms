def getleast(seq):
    if seq[0] > seq[1]:
        return seq[1]
    else:
        return seq[0]


def getRotating(seq):
    length = len(seq)

    if length == 1:
        # Recursion end gate
        return seq[0]
    elif length == 2:
        # Recursion end gate
        return getleast(seq)

    elif seq[0] < (seq[1] and seq[length - 1]):
        # For the best case point at index 0
        return seq[0]

    elif seq[length - 1] < (seq[0] and seq[length - 2]):
        # For the best case point at index max
        return seq[length - 1]

    else:
        mid = int((length / 2))
        if seq[mid] > (seq[0] and seq[length-1]):
            # Rotating pint is in the right side
            return getRotating(seq[mid:length])
        else:
            # Rotating pint is in the left side
            return getRotating(seq[0:mid+1])


def main():
    seq1 = [3, 4, 5, 7, 10]  # 3
    seq2 = [4, 5, 7, 10, 3]  # 3
    seq3 = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]  # 0
    seq4 = [5, 7, 10, 3, 4]  # 3
    seq5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 333, 666, 5555]  # 1
    seq6 = [3, 1, 2]  # 1
    seq = [seq1, seq2, seq3, seq4, seq5, seq6]
    for x in seq:
        print(getRotating(x))


if __name__ == "__main__":
    main()
