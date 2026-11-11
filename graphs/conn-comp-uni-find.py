


def conn_comp(n, edges):
    
    parents = [i for i in range(n)]
    size = [1] * n

    def find(node):
        while parents[node] != node:
            parents[node] = parents[parents[node]]
       return parents[node]

    def union(x, y):
        root1 = find(x)
        root2 = find(y)
        
        if root1 == root2:
            return False

        if root1 != root2:
            if size[root1]<size[root2]:
                root1, root2 = root2, root1

        parents[root2] = root1
        size[root1] += size[root2]
        return True
    
    res = n

    for u, v in edges:
        if union(u,v):
            res-=1

        return res
