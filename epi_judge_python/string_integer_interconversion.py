from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    is_negative = False
    if x < 0:
        is_negative = True
        x *= -1

    char_arr = []
    while True:
        char_arr.append(chr(ord('0') + x % 10))  # ORD grabs the ASCII value of 0 (48). We then add to that our value
        x //= 10
        if x == 0: break

    return ('-' if is_negative else '') + ''.join(reversed(char_arr))


def string_to_int(s):

    decimal_place, result, is_negative = len(s) - 1, 0, False
    for char in s:
        if char == '-': is_negative = True
        else: result += (ord(char) - ord('0'))*pow(10, decimal_place)
        decimal_place -= 1
    if is_negative: result = -result
    return result


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
