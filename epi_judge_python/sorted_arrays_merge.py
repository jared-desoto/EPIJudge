from test_framework import generic_test
from Lib import heapq


def merge_sorted_arrays(sorted_arrays):
    minheap = []
    #create sorted array iterators
    sorted_iterators = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_iterators):
        first_element = next(it)
        if first_element is not None:
            heapq.heappush(minheap, (first_element, i))

    result = []
    while minheap:
        smallest_entry, smallest_array_i = heapq.heappop(minheap)
        smallest_array_iter = sorted_iterators[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None) #default value if iteration hits end value
        if next_element is not None:
            heapq.heappush(minheap, (next_element, smallest_array_i))

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
