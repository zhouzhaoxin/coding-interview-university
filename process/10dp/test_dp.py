import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = [1, 2, 4, 1, 7, 8, 3]

    def test_1(self):
        def c(n):
            if n < 0:
                return 0

            if n == 0:
                return self.arr[0]
            if n == 1:
                return max(self.arr[0], self.arr[1])
            A = c(n - 2) + self.arr[n]
            B = c(n - 1)
            return max(A, B)

        print(c(6))

    def test_2(self):
        def c():
            opt = [0 for _ in range(len(self.arr))]
            opt[0] = self.arr[0]
            opt[1] = max(self.arr[0], self.arr[1])
            for i in range(2, len(self.arr)):
                a = opt[i - 2] + self.arr[i]
                b = opt[i - 1]
                opt[i] = max(a, b)
            print(opt[len(self.arr) - 1])

        c()

    def test_3(self):
        arr = [3, 34, 4, 12, 11, 12]

        def subset(i, s):

            if s == 0:
                return True
            if i == 0:
                return s == arr[i]
            if s < 0:
                return False

            if arr[i] > s:
                return subset(i - 1, s)
            A = subset(i - 1, s)
            B = subset(i, s - arr[i])
            return A or B

        print(subset(5, 9))

    def test_4(self):
        arr = [3, 34, 4, 12, 2, 12]

        def subset(S):
            t = [[False for _ in range(S + 1)] for _ in range(len(arr))]
            for x in t:
                x[0] = True
            for i, x in enumerate(t[0]):
                if i == arr[0]:
                    t[0][i] = True
            print(t)

            for i in range(1, len(arr)):
                for s in range(1, S + 1):
                    if arr[i] > s:
                        t[i][s] = t[i - 1][s]
                    else:
                        A = t[i - 1][s]
                        B = t[i - 1][s - arr[i]]
                        t[i][s] = A or B
            return t[len(arr) - 1][S]

        print(subset(9))
