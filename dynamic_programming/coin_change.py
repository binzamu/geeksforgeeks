# https://practice.geeksforgeeks.org/problems/coin-change/0

# set table stores the number of choices which row total number of currency(n), and which column money I can use, and implement dp

t = int(input())

for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    m = int(input())

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(n):
        if ar[i] <= m:
            dp[ar[i]][i + 1] += 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i - ar[j - 1] >= 0:
                x = dp[i - ar[j - 1]][j]
            else:
                x = 0
            y = dp[i][j - 1]

            dp[i][j] += x + y
            # print(dp)
    print(dp[m][n])