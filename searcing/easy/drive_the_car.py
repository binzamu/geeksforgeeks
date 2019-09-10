# https://practice.geeksforgeeks.org/problems/drive-the-car/0

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k >= max(a):
        print(-1)
    else:
        print(max(a) - k)

    