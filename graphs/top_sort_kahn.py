from collections import deque

edges = [
        (1,3),
        (2,3),
        (3,4),
        (0,1),
        (5,3),
        ]

def top_sort_kahn(n, edges):
    graph = {i: [] for i in range(n)}

    in_deg = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_deg[v] += 1

    q = deque()

    for i in range(n):
        if in_deg[i] == 0:
            q.append(i)
    
    ans = []

    while q:
        node = q.popleft()
        for child in graph[node]:
            in_deg[child] -= 1
            if in_deg[child] == 0:
                q.append(child)
        ans.append(node)
    
    if len(ans) != n:
        return []

    return ans

if __name__ == "__main__":
    print(top_sort_kahn(6, edges))


