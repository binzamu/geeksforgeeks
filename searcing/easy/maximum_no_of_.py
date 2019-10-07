# https://practice.geeksforgeeks.org/problems/maximum-no-of-1s-row/0

t = int(input())

for _ in range(t):
    row, col = map(int, input().split())

    a = list(map(int, input().split()))
    max_1 = 0
    ans = 0
    for i in range(row):
        if a[i * col:(i + 1) * col].count(1) > max_1:
            max_1 = a[i * col:(i + 1) * col].count(1)
            ans = i

    print(ans)
