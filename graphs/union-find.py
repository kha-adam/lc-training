

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1]*n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return parent[node]

    def union(self, x, y):
        par1 = self.find(x)
        par2 = self.find(y)

        if par1 != par2:
            if size[par1] > size[par2]:
                parent[par2] = par1
                size[par1] += size[par2]
            else:
                parent[par1] = par2
                size[par2] += size[par1]

    def connected(self, x, y):
        if self.find(x) == self.find(y):
            return True
        return False
