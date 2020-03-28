def getRotating(seq):

    length = len(seq)
    first = seq[0]
    last = seq[length - 1]

    if first < (seq[1] and last):
        # For the best case point at index 0
        return first

    elif last < (first and seq[length - 2]):
        # For the best case point at index max
        return last

    else:
        for x in range(length):
            if seq[x - 1] > seq[x + 1]:
                return seq[x + 1]


def main():
    seq1 = [3, 4, 5, 7, 10]  # 3
    seq2 = [4, 5, 7, 10, 3]  # 3
    seq3 = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]  # 0
    seq4 = [5, 7, 10, 3, 4]  # 3
    seq5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 333, 666, 5555]
    seq = [seq1, seq2, seq3, seq4, seq5]
    for x in seq:
        print(getRotating(x))


if __name__ == "__main__":
    main()
