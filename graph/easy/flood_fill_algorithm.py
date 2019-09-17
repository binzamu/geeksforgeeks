# https://practice.geeksforgeeks.org/problems/flood-fill-algorithm/0

def paste_check(x_check, y_check, target_color, k, mat, grid_queue):
    if mat[x_check][y_check] == target_color:
        mat[x_check][y_check] = k
        grid_queue.append((x_check, y_check))


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    mat = list()
# '*' means guard 
    mat.append(['*'] * (m + 2))
    for i in range(n):
        mat.append(['*'] + a[m * i:m * (i + 1)] + ['*'])
    mat.append(['*'] * (m + 2))

    x, y, k = map(int, input().split())

    # print(mat)

    grid_queue = list()

    grid_queue.append((x + 1, y + 1))
    target_color = mat[x + 1][y + 1]
    mat[x + 1][y + 1] = k
    # print(grid_queue)
    while True:
        x_check, y_check = grid_queue.pop(0)
        paste_check(x_check, y_check - 1, target_color, k, mat, grid_queue)        
        paste_check(x_check, y_check + 1, target_color, k, mat, grid_queue)        
        paste_check(x_check - 1, y_check, target_color, k, mat, grid_queue)        
        paste_check(x_check + 1, y_check, target_color, k, mat, grid_queue)        

        # print(mat)       
        if len(grid_queue) == 0:
            break

    ans = list()
    # print(mat)
    for i in range(1, n + 1):
        ans += mat[i][1:-1]
        # ans.append(mat[i][1:-1])

    print(*ans)