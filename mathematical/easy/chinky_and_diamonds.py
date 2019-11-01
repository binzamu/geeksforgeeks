import heapq

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = [-int(v) for v in input().split()]

    # print(a)
    heapq.heapify(a)
    # print(type(a))
    ans = 0
    for _ in range(k):
        max_diamond = -heapq.heappop(a)
        ans += max_diamond
        heapq.heappush(a, -(max_diamond // 2))

    print(ans)
