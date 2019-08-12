# https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k/0

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    ans_arr = []
    for j in range(n - (k - 1)):
        for l in range(k):
            if arr[j + l] < 0:
                ans_arr.append(arr[j + l])
                break
            if l == k - 1:
                ans_arr.append(0)
    print(*ans_arr)
