# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
t = int(input())

for i in range(t):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*(arr[d:] + arr[:d]))