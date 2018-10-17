from test_framework import generic_test
from Lib import bisect


def search_first_of_k(A, k):

    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
            mid = (left + right) // 2
        elif A[mid] < k:
            left = mid + 1
            mid = (left + right) //2
        else:  # A[mid] == k:
            result = mid
            right = mid - 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
