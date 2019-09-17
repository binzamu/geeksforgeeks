# https://practice.geeksforgeeks.org/problems/print-adjacency-list/0

# import collections

t = int(input())
for _ in range(t):
    # vertex_dict = collections.defaultdict(list)
    vertex_dict = dict()
    v, e = map(int, input().split())
    for i in range(v):
        vertex_dict[i] = []
    for _ in range(e):
        a, b = map(int, input().split())
        vertex_dict[a].append(b)
        vertex_dict[b].append(a)

    for key in sorted(vertex_dict):
        print(str(key) + ''.join(map(lambda x: '-> ' + str(x), vertex_dict[key])))