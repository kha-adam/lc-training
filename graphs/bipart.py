from collections import deque




def bfs(n, edges):

    colors = [-1] * n

    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    q = deque()

    for i in range(n):
        if colors[i] == -1:
            q.append(i)
            colors[i] = 0

        while q:
            node = q.popleft()
       
            for i in graph[node]:
                if colors[i] == -1:
                    q.append(i)
                    colors[i] = 1 - colors[node]
                elif colors[i] != 1-colors[node]:
                    return False

    return True

