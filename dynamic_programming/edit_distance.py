t = int(input())

for _ in range(t):
    p, q = map(int, input().split())
    str1, str2 = input().split()

    dp = [[0] * (q + 1) for _ in range(p + 1)]
    for i in range(q + 1):
        dp[0][i] = i
    for i in range(p + 1):
        dp[i][0] = i
    # print(dp)

    for i in range(1, p + 1):
        for j in range(1, q + 1):
            # replace cost
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
        
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    
    print(dp[p][q])

