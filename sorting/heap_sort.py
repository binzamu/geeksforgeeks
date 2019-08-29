import math


def heapify(arr, n, i):
    li = 2 * i + 1
    ri = 2 * i + 2
    large_child_index = 0
    if n == 2:
        if arr[0] <= arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

    if ri <= n - 1:
        if arr[li] >= arr[ri]:
            large_child_index = li
        elif arr[li] < arr[ri]:
            large_child_index = ri

        if arr[i] < arr[large_child_index]:
            arr[i], arr[large_child_index] = arr[large_child_index], arr[i]
            heapify(arr, n, large_child_index)


def buildHeap(arr, n):
    # build max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # pop last component repeatedly
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        buildHeap(arr, n)
        print(*arr)