# https://practice.geeksforgeeks.org/problems/equal-sum-and-product/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(i, n):
            times = 1
            for v in a[i:j + 1]:
                times *= v
            if times == sum(a[i:j + 1]):
                ans += 1

    print(ans)