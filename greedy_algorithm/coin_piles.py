# https://practice.geeksforgeeks.org/problems/coin-piles/0

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    ans = float("inf")
    removed_coin = 0
    for i in range(len(a)):
        tmp = removed_coin
        removed_coin += a[i]
        for j in range(i + 1, len(a)):
            if a[j] - a[i] >= k:
                tmp += a[j] - a[i] - k
            
        ans = min(ans, tmp)
    
    print(ans)


