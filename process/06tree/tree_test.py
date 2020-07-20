import unittest


class Node:
    def __init__(self, x, left, right):
        self.val = x
        self.left_child = left
        self.right_child = right


class BST:
    def __init__(self, root: Node):
        self.root = root

    def traversal(self):
        """按顺序从小到大遍历"""

        def t(n: Node):
            if n:
                t(n.left_child)
                print(n.val)
                t(n.right_child)

        t(self.root)

    def traversal_bfs(self):
        a = [self.root]
        while a:
            x = a.pop()
            if x:
                print(x.val)
                a.append(x.left_child)
                a.append(x.right_child)

    def to_list(self):
        """按顺序从小到大遍历"""
        res = []

        def t(n: Node):
            if n:
                t(n.left_child)
                res.append(n.val)
                t(n.right_child)

        t(self.root)
        return res

    def find(self, x):
        current = self.root
        while current:
            if current.val == x:
                return True
            elif current.val > x:
                current = current.left_child
            else:
                current = current.right_child
        return False

    def find_recursive(self, x):

        def f(n: Node):
            if not n:
                return False
            if n.val == x:
                return True
            elif n.val > x:
                return f(n.left_child)
            else:
                return f(n.right_child)

        return f(self.root)


def init_test_tree():
    n7 = Node(13, None, None)
    n6 = Node(14, n7, None)
    n5 = Node(6, None, None)
    n4 = Node(1, None, None)
    n3 = Node(10, None, n6)
    n2 = Node(3, n4, n5)
    n1 = Node(8, n2, n3)
    return BST(n1)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = init_test_tree()

    def test_new_bst(self):
        self.tree.traversal()

    def test_find(self):
        print(self.tree.to_list())
        self.assertFalse(self.tree.find(7))
        self.assertTrue(self.tree.find(8))
        self.assertTrue(self.tree.find(14))

    def test_find_recursive(self):
        print(self.tree.to_list())
        self.assertFalse(self.tree.find_recursive(7))
        self.assertTrue(self.tree.find_recursive(8))
        self.assertTrue(self.tree.find_recursive(14))

    def test_bfs(self):
        self.tree.traversal_bfs()
