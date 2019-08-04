# https://www.geeksforgeeks.org/bubble-sort/
def bubbleSort(arr, n):
    # code here
    for i in range(n - 1):
        arr = bubble(arr, i, n)
    return arr


def bubble(arr, i, n):
    for j in range(n - (i + 1)):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        arr = bubbleSort(arr, n)
        for i in arr:
            print(i, end=' ')
        print('')
