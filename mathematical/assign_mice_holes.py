# https://practice.geeksforgeeks.org/problems/assign-mice-holes/0

import math

t = int(input())
for _ in range(t):
    n = int(input())
    mice = list(map(int, input().split()))
    holes = list(map(int, input().split()))

    mice.sort()
    holes.sort()

    # for i in range(len(mice)):
    print(max(map(lambda x: abs(x[0] - x[1]), list(zip(mice, holes)))))
