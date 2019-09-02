import collections
import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    a_component_num = dict(collections.Counter(a))
    # print(a_component_num)
    pair_list = []
    for i in range(1, (k + 1) // 2):
        if i in a_component_num and k - i in a_component_num:
            pair_list.append([a_component_num[i], a_component_num[k - i]])

    # print(a_component_num)
    ans = 0
    for pair in pair_list:
        ans += pair[0] * pair[1]
    if k % 2 == 0:
        if k // 2 in a_component_num and a_component_num[k // 2] >= 2:
            div2 = k // 2
            ans += math.factorial(a_component_num[div2]) // (math.factorial(2) * math.factorial(a_component_num[div2] - 2))
    print(ans)