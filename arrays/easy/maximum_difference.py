t = int(input())

ans = 0
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        ans = max(ans, max(a[i + 1:]) - a[i])
        # print(i, ans)

    print(ans)
