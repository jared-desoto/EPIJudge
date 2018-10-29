from test_framework import generic_test


def has_three_sum(A, t):
    #first implement solution for two sum problem: (sorted list. Decrease array until found solution)
    #O(n) runtime with O(1) space
    def has_two_sum(array, target):
        i, j = 0, len(array) - 1
        while i <= j:
            if array[i] + array[j] == target:
                return True
            elif array[i] + array[j] < target:
                i += 1
            else:
                j -= 1
        return False

    A.sort()
    return any(has_two_sum(A, t - a) for a in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
