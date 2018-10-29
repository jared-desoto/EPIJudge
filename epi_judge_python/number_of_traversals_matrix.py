from test_framework import generic_test


def number_of_ways(n, m):
    def recursive_stuff(x, y):
        if x == y == 0:
            return 1

        if num_ways_dict[x][y] == 0:
            if x > 0 and y > 0:
                num_ways_dict[x][y] = recursive_stuff(x - 1, y) + recursive_stuff(x, y - 1)
            elif x > 0:
                num_ways_dict[x][y] = recursive_stuff(x - 1, y)
            else:  # y > 0
                num_ways_dict[x][y] =  recursive_stuff(x, y - 1)
        return num_ways_dict[x][y]

    max_paths = 0
    num_ways_dict = [[0] * m for _ in range(n)]
    max_paths = recursive_stuff(n - 1, m - 1)
    return max_paths


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
