# https://practice.geeksforgeeks.org/problems/reverse-coding/0
t = int(input())

for _ in range(t):
    i, o = map(int, input().split())
    if o == i * (i + 1) / 2:
        print(1)
    else:
        print(0) 