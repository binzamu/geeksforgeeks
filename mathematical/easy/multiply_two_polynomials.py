# https://practice.geeksforgeeks.org/problems/multiply-two-polynomals/0

t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    ans_list = [0] * (m + n - 1)

    for i in range(m):
        for j in range(n):
            ans_list[i + j] += a1[i] * a2[j]
    
    print(*ans_list)
    