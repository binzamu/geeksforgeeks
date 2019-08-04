# https://practice.geeksforgeeks.org/problems/selection-sort/1
# 0.49s


# Initial Template for Python 3
def select(arr):
    for i in range(len(arr) - 1):
        xmin = i
        for j, item in enumerate(arr[i + 1:]):
            if item < arr[xmin]:
                xmin = i + 1 + j
        if i != xmin:
            arr[i], arr[xmin] = arr[xmin], arr[i]
        print(arr, i)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        select(arr)
        for i in range(n):
            print(arr[i], end=" ")
        print()
