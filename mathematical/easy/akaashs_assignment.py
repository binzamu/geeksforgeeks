t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print((n + 1) ** k - 1 - (n ** k - 1))
    