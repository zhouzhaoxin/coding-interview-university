from typing import List


def is_valid(pre_col):
    row_id = len(pre_col) - 1
    for i in range(row_id):
        diff = abs(pre_col[i] - pre_col[row_id])
        if diff == 0 or diff == row_id - i:
            return False
    return True


def n_queen_recursive_main(n, row, pre_col: List[int], result):
    if n == row:
        result.append(list(pre_col))
    else:
        for i in range(n):
            pre_col.append(i)
            if is_valid(pre_col):
                n_queen_recursive_main(n, row + 1, pre_col, result)
            pre_col.pop()


def n_queen_recursive(n):
    result = []
    n_queen_recursive_main(n, 0, [], result)
    print(result)


n_queen_recursive(4)

# http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/

