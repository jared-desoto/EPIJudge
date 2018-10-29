from test_framework import generic_test
from collections import namedtuple


def is_balanced_binary_tree(tree):
    def check_height(node):
        if not node:
            return 0
        left_height = check_height(node.left) + 1
        right_height = check_height(node.right) + 1
        if left_height == 0 or right_height == 0:
            return -1
        if -1 <= left_height - right_height <= 1:
            return max(left_height, right_height)
        else:
            return -1
    if check_height(tree) != -1:
        return True
    else:
        return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
