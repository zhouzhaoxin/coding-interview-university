import unittest


class Test(unittest.TestCase):
    def test_find_str_(self):
        origin = "abcdefg"
        find = "cd"
        for i in range(0, len(origin) - 1):
            if origin[i:i + 2] == find:
                print(i)
