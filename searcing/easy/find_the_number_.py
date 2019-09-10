# https://practice.geeksforgeeks.org/problems/find-the-number-of-sub-arrays-having-even-sum/0

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(i, n):
            if sum(a[i:j + 1]) % 2 == 0:
                ans += 1
    print(ans)
