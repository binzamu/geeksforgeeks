# https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_v = 0
    ans = list()
    for i in range(n - 1, -1, -1):
        if a[i] >= max_v:
            ans.append(a[i])
            max_v = a[i]
        # print()
    print(*ans[::-1])
