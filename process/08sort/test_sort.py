import unittest
import random


def quick_sort_main(arr, lo, hi):
    if lo >= hi:
        return
    piv = random.randint(lo, hi)
    i = lo
    j = hi
    arr[piv], arr[hi] = arr[hi], arr[piv]

    while True:
        while i < hi and arr[i] <= arr[hi]:
            i += 1

        while j > lo and arr[j] >= arr[hi]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[hi], arr[i] = arr[i], arr[hi]
    quick_sort_main(arr, lo, i - 1)
    quick_sort_main(arr, i + 1, hi)


def quick_sort(arr):
    lo = 0
    hi = len(arr) - 1
    quick_sort_main(arr, lo, hi)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = [19, 13, 1, 5, 3, 4, 111, 34, 141, 22, 78, 23, 55]
        self.arr = [random.randint(1, 100) for _ in range(10)]

    def test_quick_sort(self):
        print(self.arr)
        quick_sort(self.arr)
        print(self.arr)

    def test_quick_sort2(self):
        def s1():
            lo, hi = 0, len(self.arr) - 1
            s2(self.arr, lo, hi)

        def s2(arr, lo, hi):
            if lo >= hi:
                return

            piv = random.randrange(lo, hi)
            i, j = lo, hi
            arr[hi], arr[piv] = arr[piv], arr[hi]

            while True:
                while i < hi and arr[i] <= arr[hi]:
                    i += 1

                while j > lo and arr[j] >= arr[hi]:
                    j -= 1

                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    break
            arr[i], arr[hi] = arr[hi], arr[i]
            s2(arr, lo, i - 1)
            s2(arr, i + 1, hi)

        s1()
        print(self.arr)

    def test_find_nth_largest(self):
        def find(arr, n, lo, hi):
            if lo > hi:
                return
            if lo == hi:
                return arr[lo]
            piv = random.randrange(lo, hi)
            i, j = lo, hi
            arr[piv], arr[hi] = arr[hi], arr[piv]
            while True:
                while i < hi and arr[i] <= arr[hi]:
                    i += 1

                while j > lo and arr[j] >= arr[hi]:
                    j -= 1

                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    break
            arr[i], arr[hi] = arr[hi], arr[i]

            if n < i:
                return find(arr, n, lo, i - 1)
            if n == i:
                return arr[i]
            if n > i:
                return find(arr, n, i + 1, hi)

        self.arr = [25, 65, 2, 12, 18, 98, 49, 87, 70, 55]
        print(self.arr)
        print(find(self.arr, 19, 0, len(self.arr) - 1))
        quick_sort(self.arr)
        print(self.arr)
