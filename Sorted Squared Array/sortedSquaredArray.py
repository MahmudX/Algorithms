from collections import deque


def sortedSquaredArray(array):
    sortedArray = []
    left = 0
    right = len(array) - 1
    while True:
        if left == right:
            sortedArray.insert(0, abs(array[right])**2)
            break
        if abs(array[left]) >= abs(array[right]):
            sortedArray.insert(0, abs(array[left])**2)
            left += 1
        else:
            sortedArray.insert(0, abs(array[right])**2)
            right -= 1
    return sortedArray


def main():
    arr = [-10, 1, 9, 9, 10]
    print(sortedSquaredArray(arr))


if __name__ == "__main__":
    main()
