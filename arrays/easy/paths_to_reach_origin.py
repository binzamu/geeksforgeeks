# https://practice.geeksforgeeks.org/problems/paths-to-reach-origin/0

import math

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    print(int(math.factorial(n + m) / math.factorial(n) / math.factorial(m)))

