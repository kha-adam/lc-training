edges = [
        (0,1),
        (1,2),
        (2,3),
        (4,3),
        (3,5),
        (4,6),
        ]

def topol_order(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)

    state = [0] * n

    ans = []

    def dfs(node):
        state[node] = 1

        for neighbor in graph[node]:
           if state[neighbor] == 0:
                if not dfs(neighbor):
                    return False 
           elif state[neighbor] == 1:
                return False
        state[node] = 2
        ans.append(node)
        return True

    for node in graph:
        if state[node] == 0:
            if not dfs(node):
                return []
    return ans[::-1] 

if __name__ == "__main__":
    print(topol_order(7, edges))
