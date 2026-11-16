def kruskal(n, edges):

    parents = [i for i in range(n)]
    sizes = [1] * n

    def find(node):
        while node != parents[node]:
            parents[node] = parents[parents[node]]
            node = parents[node]
        return node

    def union(x, y):
        parx, pary = find(x), find(y)
        if parx == pary:
            return False
        if sizes[parx] < sizes[pary]:
            parx, pary = pary, parx

        parents[pary] = parx
        sizes[parx] += sizes[pary]
        return True

    edges.sort(key=lambda edge: edge[2])

    ans = []
    i = 0
    while len(ans) < n - 1:
        x, y, w = edges[i]
        if union(x, y):
            ans.append((x,y,w))
        i += 1
    return ans
