from test_framework import generic_test, test_utils

# Number of Recursive Calls = O(2^n). Spend O(n) time in each call. Therefore time complexity = O(n*2^n)
def generate_power_set(S):
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(S):
            power_set.append(list(selected_so_far))
            return
        directed_power_set(to_be_selected + 1, selected_so_far)
        # Generate all subsets that contain S[tto_be_selected]
        directed_power_set(to_be_selected + 1, selected_so_far + [S[to_be_selected]])

    power_set = []
    directed_power_set(0, [])
    return power_set


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
