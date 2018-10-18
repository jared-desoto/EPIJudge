from test_framework import generic_test

# Initial algorithm: O(N+M) time complexity O(N) space complexity
def intersect_two_sorted_arrays_extra_space(A, B):
    a_dict = {}
    result = []
    for i in A:
        if i not in a_dict:
            a_dict[i] = 1
    for j in B:
        if j in a_dict and (len(result) == 0 or j != result[-1]):
            result.append(j)
    return result

# For Better Space Complexity: O(1)
def intersect_two_sorted_arrays(A, B):
    result, i, j = [], 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                result.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:  # B[i] < A[i]:
            j += 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
