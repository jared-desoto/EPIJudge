from test_framework import generic_test


def parity(x):

    # Brute force solution. Check every bit and store how many are 1's.
    result = 0
    while x:
        # This works because bitwise & with and integer and 1 will only return 1 if the last bit is 1
        # We XOR each time to effectively switch between true and false each time we reach a bit with last value of 1
        result ^= x & 1
        # By right shifting by 1 each time (equivalent to dividing by 2), we evaluate every bit of the integer
        x >>= 1
    return result

    # TODO Come back for more elegant solution


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
