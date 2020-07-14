# 公式
# f(row, col) = row! / ((row - col)! * col!)
# f(row, col - 1) = row! / ((row - col + 1)! * (col - 1)!)
# 导出
# f(row, col) = f(row, col-1) * (row - col + 1) / col


# 数学方法
# O(n^2) O(n^2)
def triangle_math(n):
    for line in range(n):
        c = 1
        for i in range(line + 1):
            if i is not 0:
                c = c * (line - i + 1) / i

            print(c, end=" ")
        print()


# 容易理解 O(n^2) O(n^2)
def triangle_understand(n):
    r = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        r[i][0] = r[i][i] = 1

    for i in range(2, n):
        for j in range(1, i + 1):
            r[i][j] = r[i - 1][j - 1] + r[i - 1][j]

    for i in range(n):
        for j in range(i + 1):
            print(r[i][j], end=' ')
        print()


# 直接打印 O(n^2) O(n^2)
def triangle_direct(n):
    r = [[0 for _ in range(n)] for _ in range(n)]
    for line in range(n):
        for i in range(line + 1):
            if i in (0, line):
                r[line][i] = 1
            else:
                r[line][i] = r[line - 1][i - 1] + r[line - 1][i]
            print(r[line][i], end=" ")
        print()
