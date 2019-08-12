# https://practice.geeksforgeeks.org/problems/max-distance-between-same-elements/1
def maxDistance(arr, n):
    dist = {0: 0}
    for i in range(n):
        if arr[i] in dist.keys():
            continue
        else:
            for j in range(n - 1, i, -1):
                if arr[i] == arr[j]:
                    # print(i, j)
                    dist[arr[i]] = j - i
                    break
                    # return(j - i)
    return (max(dist.values()))
    # return(0)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        # print(arr)
        print(maxDistance(arr, n))
