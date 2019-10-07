# https://practice.geeksforgeeks.org/problems/search-in-a-matrix/0

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    mat = list(map(int, input().split()))
    x = int(input())

    for i in range(1, n + 1):
        # print(mat[m * i - 1])
        if x <= mat[m * i - 1]:
            for j in range(m):
                if mat[m * (i - 1) + j] == x:
                    print(1)
                    break
            else:
                print(0)
                
            break