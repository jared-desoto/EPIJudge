from test_framework import generic_test
from Lib import collections

# recursive solution utilizing property that child must exist in a range established by parent
# O(N) runtime solution with O(h) space (From recursive calls)
def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):

    if not tree:
        return True
    if low_range <= tree.data <= high_range :
        return (is_binary_tree_bst(tree.left, low_range, tree.data) and # left child
                is_binary_tree_bst(tree.right, tree.data, high_range))  # right child
    else:
        return False

# iterative solution by in order traversal and verifying keys are in ascending order
# O(N) runtime with O(N) space
def is_binary_tree_bst_iterative(tree):
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))
    bfs_queue = collections.deque(
        [QueueEntry(tree, float('-inf'), float('inf'))])
    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
                ]
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
