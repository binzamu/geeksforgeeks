# https://practice.geeksforgeeks.org/problems/addition-of-submatrix/0
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    x1, y1, x2, y2 = map(int, input().split())
    c = []
    for j in range(n):
        c.append(arr[j * m:(j + 1) * m])
    # print(c)
    ans = 0
    for j in range(x1 - 1, x2):
        for k in range(y1 - 1, y2):
            
            ans += c[j][k]

    print(ans)
