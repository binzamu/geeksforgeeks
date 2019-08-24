t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    power = 1
    a = p
    ans = 0
    while a < n:
        ans += n // a
        power += 1
        a = p ** power
    print(ans)