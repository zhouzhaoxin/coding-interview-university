import unittest


class GR1:
    def __init__(self):
        self.Adj = {}
        self.in_degree = {}

    def add_edge(self, x, y):
        if x not in self.Adj:
            self.Adj[x] = set()
        if x not in self.in_degree:
            self.in_degree[x] = 0
        if y and y not in self.in_degree:
            self.in_degree[y] = 0
        if y:
            self.Adj[x].add(y)
            self.in_degree[y] += 1

    @property
    def vertex(self):
        return {v for v in self.Adj}

    def print_in_degree(self):
        print(self.in_degree)

    def find_zero(self, in_degree, queue):
        for key, val in in_degree.items():
            if val == 0:
                queue.append(key)

    def topological_sort(self):
        in_degree = self.in_degree
        queue = []
        self.find_zero(in_degree, queue)
        while queue:

            curr = queue.pop(0)
            if curr in in_degree:
                del in_degree[curr]
                print(curr)
            for v in self.Adj[curr]:
                if v != 0 and v in in_degree:
                    in_degree[v] -= 1
            self.find_zero(in_degree, queue)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.adj = GR1()
        self.adj.add_edge("a", "c")
        self.adj.add_edge("a", "b")
        self.adj.add_edge("b", "c")
        self.adj.add_edge("c", "d")
        self.adj.add_edge("d", "b")
        self.adj.add_edge("d", "g")
        self.adj.add_edge("e", "d")
        self.adj.add_edge("e", "f")
        self.adj.add_edge("f", None)
        self.adj.add_edge("g", None)

    def test_bfs(self):
        self.adj.topological_sort()

    def test_print_in_degree(self):
        self.adj.print_in_degree()
