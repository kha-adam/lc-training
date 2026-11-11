


def find_red_conn(edges):
    parent = list(range(len(edges) + 1))

    size = [1] * (len(edges) + 1)

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
        return parent[node]

    def union(x, y):
        root1 = find(x)
        root2 = find(y)

        if root1 == root2:
            return False
        if size[root1] < size[root2]:
             root1, root2 = root2, root1

        parent[root2] = root1
        size[root1] += size[root2]
        return True
    
    for u, v in edges:
        if not union(u,v):
            return [u,v]
