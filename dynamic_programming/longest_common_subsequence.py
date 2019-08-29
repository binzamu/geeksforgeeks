# https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a_str = input()
    b_str = input()

    # dp = [[0] * (b + 1)] * (a + 1)
    dp = [[0] * (b + 1) for i in range(a + 1)]
    for i in range(a):
        for j in range(b):
            if a_str[i] == b_str[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    print(dp[a][b])
        

