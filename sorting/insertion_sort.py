# https://www.geeksforgeeks.org/insertion-sort/
def insert(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j, arr[i])
                arr.pop(i + 1)
    return arr


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        insert(arr)

        for i in range(n):
            print(arr[i], end=" ")

        print()