# https://practice.geeksforgeeks.org/problems/first-repeating-element/0

import collections

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    tmp_dict = collections.defaultdict(list)

    for i in range(n):
        tmp_dict[a[i]].append(i)
    # print(dict(tmp_dict).values)
    # tmp_dict = dict(tmp_dict)
    twice_list = list(filter(lambda key: len(tmp_dict[key]) >= 2, tmp_dict))

    if len(twice_list) == 0:
        print(-1)
        exit()
    ans = float("INF")
    for v in twice_list:
        ans = min(ans, tmp_dict[v][0])

    print(ans + 1)

