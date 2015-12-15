from itertools import combinations
import re

def ord_to_chr(ord_list):
    return "".join([chr(c) for c in ord_list])


def iterate_password(pw, start_position=0):
    seq = list(reversed([ord(c) for c in pw]))
    new_seq = seq[start_position:]
    if (new_seq[0] + 1) % ord('z') == 1:
        seq[start_position] = ord('a')
        return iterate_password(reversed(ord_to_chr(seq)), start_position=start_position+1)
    else:
        seq[start_position] = new_seq[0] + 1
        return ord_to_chr(reversed(seq))


def confirm_sequence(s):
    seq = [ord(c) for c in s]
    for index, c in enumerate(seq[:-3]):
        if (c + 1 == seq[index + 1]) and (c + 2 == seq[index + 2]):
            return True
    return False


def any_bad_letters(s):
    return not any(i in ['i', 'o', 'l'] for i in s)


def two_overlapping(s):
    return len(re.findall(r'(.)\1', s)) >= 2

# numbers = [1,2,3,4]
# for item in combinations(numbers, 3):


def get_password(input):
    next_password = iterate_password(input)
    while True:
        next_password = iterate_password(next_password)
        if (confirm_sequence(next_password) and any_bad_letters(next_password) and two_overlapping(next_password)):
            return next_password

get_password("cqjxjnds")
