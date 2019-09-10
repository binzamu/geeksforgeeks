# https://practice.geeksforgeeks.org/problems/element-appearing-once/0

import collections

t = int(input())

for _ in range(t):
    n = int(input())
    a = collections.Counter(list(map(int, input().split())))

    ans = list(filter(lambda key: a[key] == 1, a))
    if len(ans) != 1:
        print("error")
    else:
        print(ans[0])
