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

    def test_merge_two_array(self):
        first = [1, 3, 5]
        lf = len(first)
        second = [2, 4, 6, 7, 8, 9]
        ls = len(second)
        sf = ss = 0
        result = []

        while sf < lf and ss < ls:
            if first[sf] < second[ss]:
                result.append(first[sf])
                sf += 1
            else:
                result.append(second[ss])
                ss += 1
        while sf < lf:
            result.append(first[sf])
            sf += 1
        while ss < ls:
            result.append(second[ss])
            ss += 1
        print(result)

    def test_merge_two_array_use_bits(self):
        first = [1, 3, 5]
        lf = len(first)
        second = [2, 4, 6, 7, 8, 9]
        ls = len(second)
        sf = ss = 0
        result = []

        while sf < lf and ss < ls:
            cmp = first[sf] < second[ss]
            result.append(second[ss] ^ (first[sf] ^ second[ss]) & -cmp)
            sf += cmp
            ss += not cmp

        while sf < lf:
            result.append(first[sf])
            sf += 1
        while ss < ls:
            result.append(second[ss])
            ss += 1
        print(result)

    def test_bits_count_in_word(self):
        word = ord('a')
        r = 0
        while word != 0:
            r += 1
            word &= word - 1
        print(r)
