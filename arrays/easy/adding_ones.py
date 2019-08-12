# https://practice.geeksforgeeks.org/problems/adding-ones/0


t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    a = [0] * n
    # print(a)
    for i in arr:
        for j in range(i - 1, n):
            a[j] += 1

    print(*a)