from helper import (
    get_all_pairs,
    get_element_if_repeat_more_than_two_times,
    get_input,
    get_mirror_substring,
    get_repeated_elements,
    get_substring_three_char_long,
    get_sum_of_dict_values,
    get_vowels_in_string,
    has_disallowed_string_list,
    has_double_letters_in_string,
)


def has_total_vowel_count_greater_two(line: str) -> bool:
    has = True
    vowel_dict = get_vowels_in_string(line)
    total = get_sum_of_dict_values(vowel_dict)
    if total > 2.0:
        return has
    has = False
    return has


def solved_part_one():
    year = "2015"
    file = "input_day_5.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    disallowed_list = ["ab", "cd", "pq", "xy"]
    count = 0
    nice_list = []
    naughty_list = []
    for line in input_lines:

        allowed_string = not has_disallowed_string_list(disallowed_list, line)
        if not allowed_string:
            naughty_list.append(line)
            continue

        vowels_allowed = has_total_vowel_count_greater_two(line)
        if not vowels_allowed:
            naughty_list.append(line)
            continue

        double_allowed = has_double_letters_in_string(line)
        if not double_allowed:
            naughty_list.append(line)
            continue

        nice_list.append(line)

    count = len(nice_list)
    print(f"Part One: {count} : Strings are nice!")


def has_repeated_pair_not_overlapping(check_string: str) -> bool:
    has = True

    has_pairs = get_all_pairs(check_string)
    if has_pairs == None:
        has = False
        return has

    has_repeated_pairs = get_repeated_elements(has_pairs)
    if has_repeated_pairs == None:
        has = False
        return has

    has_overlap = get_element_if_repeat_more_than_two_times(check_string)
    if has_overlap != None:
        has = False
        return has

    return has


def has_mirror_substring(line):
    has = True

    ss_list = get_substring_three_char_long(line)
    has_mirror_list = get_mirror_substring(ss_list)
    if has_mirror_list == None:
        has = False
        return has
    return has


def sloved_part_two():
    year = "2015"
    file = "input_day_5.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    nice_list = []
    naughty_list = []
    count = 0
    for line in input_lines:
        has_pair_no_overlap = has_repeated_pair_not_overlapping(line)
        if not has_pair_no_overlap:
            naughty_list.append(line)
            continue
        has_mirror = has_mirror_substring(line)
        if not has_mirror:
            naughty_list.append(line)
            continue
        nice_list.append(line)
    count = len(nice_list)
    print(f"Part Two: {count} : Strings are nice!")


if __name__ == "__main__":
    solved_part_one()
    sloved_part_two()
