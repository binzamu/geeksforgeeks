# https://practice.geeksforgeeks.org/problems/maximize-toys/0
t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    total_value = 0
    for i in range(len(a)):
        if total_value + a[i] > k:
            print(i)
            break
        else:
            total_value += a[i]
