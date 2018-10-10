from test_framework import generic_test
from test_framework.test_failure import TestFailure

# This stack is the most basic implementation. It has O(N) performance on the max function.
# To improve we can cache some Max data on every push
# TODO implement better solution with caching
class Stack:
    def __init__(self):
        self.data = []

    def empty(self):
        while True:
            if len(self.data) == 0:
                break
            self.data.pop()
        return True

    def max(self):
        return max(self.data)

    def pop(self):
        return self.data.pop()

    def push(self, x):
        self.data.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
