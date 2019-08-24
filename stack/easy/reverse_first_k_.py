t = int(input())


def reverseK(queue, k, n):
    return ((queue[:k][::-1] + queue[k:]))


for i in range(t):
    n, k = map(int, input().split())
    queue = list(map(int, input().split()))
    print(*reverseK(queue, k, n))
