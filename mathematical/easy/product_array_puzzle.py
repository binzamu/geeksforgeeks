# https://practice.geeksforgeeks.org/problems/product-array-puzzle/0

from functools import reduce

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total_product = reduce(lambda x, y: x * y, a)
    ans_list = list()
    for i in range(n):
        # ans_list.append(reduce(lambda x, y: x * y, tmp_list))
        ans_list.append(total_product // a[i])

    print(*ans_list)


