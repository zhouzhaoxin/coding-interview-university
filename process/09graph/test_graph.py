import unittest
from typing import List


class AdjacencyList:
    def __init__(self, v: List):
        self.V = v
        self.Adj = {}

    def add_edge(self, x, y):

        if x not in self.V:
            raise Exception("not in graph")

        if x in self.Adj and y:
            self.Adj[x].append(y)
        elif y:
            self.Adj[x] = [y]
        else:
            self.Adj[x] = []

    def bfs(self):
        start = self.V[0]
        level = {start: 0}
        parent = {start: None}
        front = [start]
        n = 1
        while front:
            next = []
            for f in front:
                for v in self.Adj[f]:
                    if v not in parent:
                        parent[v] = f
                        next.append(v)
                        level[v] = n
            front = next
            n += 1
        print(parent)

    def dfs(self):
        parent = {}
        stack = []

        def dfs_visit(s):
            stack.append(s)
            while stack:
                for v in self.Adj[stack.pop()]:
                    if v not in parent:
                        parent[v] = s
                        dfs_visit(v)
                        stack.append(v)

        for v in self.V:
            if v not in parent:
                parent[v] = None
                dfs_visit(v)
        print(parent)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.adj = AdjacencyList(["a", "b", "c", "d", "e", "f", "g"])
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
        self.adj.bfs()

    def test_dfs(self):
        self.adj.dfs()
