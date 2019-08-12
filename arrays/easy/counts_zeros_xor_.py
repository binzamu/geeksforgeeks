# https://practice.geeksforgeeks.org/problems/counts-zeros-xor-pairs/0

import collections

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = collections.Counter(a)
    ans = 0
    for i in c.values():
        if i >= 2:
            ans += i * (i - 1) / 2
    print(int(ans))
