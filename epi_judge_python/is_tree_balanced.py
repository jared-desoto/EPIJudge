from test_framework import generic_test
from collections import namedtuple


def is_balanced_binary_tree(tree):
    height_isbalanced = namedtuple('HeightBalanced', ('height', 'isbalanced'))

    def calculateBalance(node):
        if not node:
            return height_isbalanced(-1, True)

        left = calculateBalance(node.left)
        if not left.isbalanced:
            return height_isbalanced(left.height, left.isbalanced)
        right = calculateBalance(node.right)
        if not right.isbalanced:
            return height_isbalanced(right.height, right.isbalanced)

        max_value = max(left.height, right.height)+1
        is_balanced = False
        if abs(right.height - left.height) <= 1:
            is_balanced = True

        return height_isbalanced(max_value, is_balanced)
    return calculateBalance(tree).isbalanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
