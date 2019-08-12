# https://practice.geeksforgeeks.org/problems/count-pairs-in-an-array/0
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for j in range(n):
        for k in range(j + 1, n):
            if j * arr[j] > k * arr[k]:
                ans += 1
    print(ans)
