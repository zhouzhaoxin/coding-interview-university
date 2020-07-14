import unittest


class Test(unittest.TestCase):
    def test_1(self):
        print(bin(3), bin(4))
        print(3 & 4)
        print(3 ^ 4)
        print("shift left", 3 << 1)
        print("shift right", 3 >> 1 >> 1)

    def test_set_bit(self, x, position):
        mask = 1 << position
        print(x | mask)

    def test_clear_bit(self, x, position):
        mask = 1 << position
        print(x & ~mask)

    def test_flip_bit(self, x, position):
        mask = 1 << position
        print(x ^ mask)

    def test_if_even(self, x):
        return not x & 1

    def test_if_is_power_of_two(self, x):
        return not x & (x - 1)

    def test_sign(self):
        sign = -1
        print(-(sign < 0))
