# https://practice.geeksforgeeks.org/problems/pairs-which-are-divisible-by-4/0

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % 4 == 0:
                ans += 1
    print(ans)

