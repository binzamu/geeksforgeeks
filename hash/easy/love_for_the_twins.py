# https://practice.geeksforgeeks.org/problems/love-for-the-twins/0

import collections
# import heapq
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    c = collections.Counter(a)
    print(sum(map(lambda n: n - n % 2, c.values())))
