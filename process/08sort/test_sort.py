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
