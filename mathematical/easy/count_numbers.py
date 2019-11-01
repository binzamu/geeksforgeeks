t = int(input())
for _ in range(t):
    n = int(input())

    ans = 0
    for i in range(1, n + 1):
        if '3' not in str(i):
            ans += 1
    print(ans)