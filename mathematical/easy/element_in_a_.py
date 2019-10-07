import math
import itertools

t = int(input())
n = [int(input()) for _ in range(t)]

largest_digit = math.ceil(math.log2(max(n) + 2) - 1)

product_list = []
for i in range(1, largest_digit + 1):
    product_list.extend(itertools.product('47', repeat=i))

for v in n:
    print(''.join(product_list[v - 1]))
