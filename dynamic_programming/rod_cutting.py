# https://practice.geeksforgeeks.org/problems/rod-cutting/0


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n)]
    # dp[0][0] = 0
    for i in range(1, n + 1):
        dp[0][i] = a[i - 1]

    # print(dp[1])
    for i in range(1, n):
        for j in range(1, n + 1):
            for k in range(j // 2 + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + dp[i - 1][j - k])

    # print(dp)
    print(dp[n - 1][n])
# 1
# 8
# 1 5 8 9 10 17 17 20