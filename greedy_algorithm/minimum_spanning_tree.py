# https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1
# prim's algorythm


def spanningTree(V, E, graph):
    set_node = [0]
    total_value = 0
    # min = float("inf")
    for _ in range(V - 1):
        tmp_node = [-1, -1, float("inf")]
        for i in range(len(set_node)):
            for j in range(len(graph[i])):
                if graph[i][j] == float("inf"):
                    continue
                else:
                    if tmp_node[2] > graph[i][j]:
                        tmp_node = [i, j, graph[i][j]]

        set_node.append(tmp_node[2])
        total_value += tmp_node[2]
        graph[tmp_node[0]][tmp_node[1]] = float("inf")
        graph[tmp_node[1]][tmp_node[0]] = float("inf")
    return (total_value)


# Contributed by : Nagendra Jha
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        graph = [[float("inf") for i in range(V)] for i in range(V)]
        for i in range(0, len(info), 3):
            u, v, w = info[i] - 1, info[i + 1] - 1, info[i + 2]
            graph[u][v] = w
            graph[v][u] = w
        print(graph)
        print(spanningTree(V, E, graph))
