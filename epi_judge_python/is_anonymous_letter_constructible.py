from test_framework import generic_test
from Lib import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    magazine_dict = {}
    for char in magazine_text:
        if char in magazine_dict:
            magazine_dict[char] += 1
        else:
            magazine_dict[char] = 1

    result = True
    for char in letter_text:
        if char in magazine_dict:
            if magazine_dict[char] == 1:
                del magazine_dict[char]
            else:
                magazine_dict[char] -= 1
        else:
            result = False
            break

    return result

# Better Pythonic Solution using Collection.Counter
def is_letter_constructible_from_magazine_pythonic_better(letter_text, magazine_text):
    # Compute the frequencies for all chars in letter_text .
    char_frequency_for_letter = collections.Counter(letter_text)

    # Checks if characters in magazine_text can cover characters in
    # char_frequency_for_letter .
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    # All characters for letter_text are matched.
                    return True

    # Empty char_frequency_for_letter means every char in letter_text can be
    # covered by a character in magazine_text .
    return not char_frequency_for_letter

# Best Pythonic Solution using Collection.Counter:
# Note that the subtraction only keeps keys with positive counts
def is_letter_constructible_from_magazine_pythonic_best(letter_text, magazine_text):
    return (not collections.Counter(letter_text) -
                collections.Counter(magazine_text))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
