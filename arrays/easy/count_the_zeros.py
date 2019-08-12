# https://practice.geeksforgeeks.org/problems/count-the-zeros/0

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(a.count(0))