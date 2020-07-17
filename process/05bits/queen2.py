def queen1(n):
    c = []
    done = (2 ** n) - 1
    queen1_main(0, 0, 0, done, c)
    print(len(c))


def queen1_main(ld, col, rd, done, c):
    if col == done:
        c.append(1)
    else:
        poss = ~(ld | col | rd)
        while poss & done:
            bit = poss & -poss
            poss -= bit
            queen1_main((ld | bit) >> 1, col | bit, (rd | bit) << 1, done, c)


def queen(n):
    result = []
    done = 2 ** n - 1
    queen_main(0, 0, 0, done, result)
    print(len(result))


def queen_main(A, B, C, done, result):
    if B == done:
        result.append(1)
    else:
        D = ~(A | B | C)
        while D & done:
            bit = D & -D
            D -= bit
            queen_main((A | bit) >> 1, (B | bit), (C | bit) << 1, done, result)


"""
启蒙 http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/
详情 https://blog.csdn.net/Dora_Bin/article/details/52733832
"""

queen(4)
queen1(4)
