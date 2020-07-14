# 计算中间值需要使用：left + (right - left) // 2
def bs_while(key, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > key:
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            return mid


# 递归要注意用return返回
# (left + (right - left - 1) // 2
# 在 right 和 left 相同时会出现负数导致无限递归
def bs_recursive(key, arr, left, right):
    if left > right:
        return
    mid = left + (right - left) // 2
    if arr[mid] > key:
        right = mid - 1
        return bs_recursive(key, arr, left, right)
    elif arr[mid] < key:
        left = mid + 1
        return bs_recursive(key, arr, left, right)
    else:
        return mid


assert bs_while(1, [1, 2, 3]) == 0, 'not  equal 0'
assert bs_while(4, [1, 2, 3]) is None, 'not  equal None'
assert bs_while(4, [1, 2, 3, 4]) is 3, 'not  equal 4'
assert bs_while(2, [1, 2, 3, 4]) is 1, 'not  equal 1'

assert bs_recursive(1, [1, 2, 3], 0, 2) == 0, 'not  equal 0'
assert bs_recursive(4, [1, 2, 3], 0, 2) is None, 'not  equal None'
assert bs_recursive(4, [1, 2, 3, 4], 0, 3) is 3, 'not  equal 4'
assert bs_recursive(2, [1, 2, 3, 4], 0, 3) is 1, 'not  equal 1'
