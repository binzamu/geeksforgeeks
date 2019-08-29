def quickSort(arr, low, high):
    print(arr)
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        # print(arr)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
        

def partition(arr, low, high):
    p = arr[high]
    pi = high
    for i in range(high, low - 1, -1):
        if arr[i] > p:
            value = arr.pop(i)
            arr.insert(high, value)
            pi -= 1
            # print(arr)

    return (pi)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()