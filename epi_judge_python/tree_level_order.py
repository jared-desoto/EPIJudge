from test_framework import generic_test
from Lib import collections


def binary_tree_depth_order(tree):
    result, cur_que = [], collections.deque([tree])
    while cur_que:
        cur_arr, next_que = [], collections.deque([])
        while cur_que:
            current = cur_que.popleft()
            if current:
                cur_arr.append(current.data)
                next_que.append(current.left); next_que.append(current.right)
        if cur_arr:
            result.append(cur_arr)
        cur_que = next_que
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
