class Graph:
    def __init__(self):
        self.vertices = set()
        self.graph = []
        self.weight = None
        self.parent = {}
        self.rank = {}

    def addEdge(self, u, v, w):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph.append([u, v, w])

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def KruskalMST(self):
        result = Graph()
        self.graph = sorted(self.graph, key=lambda item: item[2])

        for node in self.vertices:
            self.parent[node] = node
            self.rank[node] = 0

        e = 0
        for u, v, w in self.graph:
            x = self.find(u)
            y = self.find(v)
            if x != y:
                e += 1
                result.addEdge(u, v, w)
                self.union(x, y)

        return result

    def get_total_weight(self):
        self.weight = sum(w for u, v, w in self.graph)
        return self.weight

    def generate_DOT(self):
        res = 'digraph mlm {\n'
        for u, v, w in self.graph:
            res += f"{u} -> {v} [label=\"{w}\"]\n"
        res += '}'
        return res

if __name__ == '__main__':
    g = Graph()
    g.addEdge('a', 'b', 10)
    g.addEdge('a', 'c', 6)
    g.addEdge('b', 'c', 23)
    print(g.generate_DOT())
    print(g.get_total_weight())

    t = g.KruskalMST()
    print(t.generate_DOT())
    print(t.get_total_weight())
