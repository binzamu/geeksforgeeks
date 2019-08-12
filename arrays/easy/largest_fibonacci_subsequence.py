# https://practice.geeksforgeeks.org/problems/largest-fibonacci-subsequence/0
def fibonacci(fib, max_num):
    while True:
        if fib[-1] > max_num:
            return fib
        fib.append(fib[-1] + fib[-2])


t = int(input())
fib = [0, 1]
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = max(arr)
    ans = []
    fib = fibonacci(fib, max_num)
    for j in arr:
        if j in fib:
            ans.append(j)

    print(*ans)