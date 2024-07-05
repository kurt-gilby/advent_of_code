import hashlib


def get_mirror_substring(Input_list: list[str]) -> list[str]:
    """
    Takes a list of three char long strings
    For each string checks if the 1st and 3rd element is the same and the middle element if different.
    Returns list of sub-strings which match the above criteria.
    """
    mirror_substring_list = []

    for sub in Input_list:
        if sub[0] == sub[2] and sub[0] != sub[1] and sub[1] != sub[2]:
            mirror_substring_list.append(sub)
    if len(mirror_substring_list) == 0:
        return None
    return mirror_substring_list


def get_substring_three_char_long(Input_string: str) -> list[str]:
    """
    Takes a string
    Gets all three character length sub-string sequencially and add to list
    Returns list of sub-strings.
    """
    sub_string_list = []
    for i in range(len(Input_string) - 2):
        sub_string = Input_string[i] + Input_string[i + 1] + Input_string[i + 2]
        sub_string_list.append(sub_string)
    return sub_string_list


def get_element_if_repeat_more_than_two_times(check_string: str) -> list[str]:
    """
    Takes a string
    Gets list of elements that repeat in sequece more than 2 times
    Returns list of elements.
    """
    more_than_two = []
    for i in range(len(check_string) - 2):
        if (
            check_string[i] == check_string[i + 1]
            and check_string[i + 1] == check_string[i + 2]
        ):
            more_than_two.append(check_string[i])
    if len(more_than_two) == 0:
        return None
    return more_than_two


def get_index_of_pair_of_elements(
    list_of_elements: list[str], index_string: str
) -> list[str]:
    """
    Takes list of pair elements and the string to check indexs
    Gets the list of all indexs for all the pairs.
    Returns list of indexs.
    """
    list_of_indexs = []
    for element in list_of_elements:
        for i in range(len(index_string) - 1):
            check_element = index_string[i] + index_string[i + 1]
            if element == check_element:
                list_of_indexs.append(str(i))
                list_of_indexs.append(str(i + 1))
    if len(list_of_indexs) == 0:
        return None
    return list_of_indexs


def get_repeated_elements(list_of_elements: list[str]) -> list[str]:
    """
    Takes list of elements.
    Checks the number of time an element repeats.
    Returns list of elements that repeats more than once.
    """
    repeated = []
    for i in range(len(list_of_elements)):
        if list_of_elements[i] in repeated:
            continue
        count = list_of_elements.count(list_of_elements[i])
        if count > 1:
            repeated.append(list_of_elements[i])
    if len(repeated) == 0:
        return None
    return repeated


def get_all_pairs(string_to_extract: str) -> list[str]:
    """
    Takes a string.
    Gets all pair of characters in a sequence.
    Returns list of pair of characters in a sequence.
    """
    str_pairs = []
    for i in range(len(string_to_extract) - 1):
        str_pair = string_to_extract[i] + string_to_extract[i + 1]
        str_pairs.append(str_pair)
    if len(str_pairs) == 0:
        return None
    return str_pairs


def get_vowels_in_string(string_to_check: str) -> dict[str:float]:
    """
    Takes a string.
    identifies the vowels in the string.
    Returns a Dict with vowels found as key and number of times found as values
    """
    vowels = ["a", "e", "i", "o", "u"]
    vowels_dict = {"a": 0.0, "e": 0.0, "i": 0.0, "o": 0.0, "u": 0.0}

    for vowel in vowels:
        for item in string_to_check:
            if vowel == item:
                vowels_dict[vowel] += 1.0
    return vowels_dict


def get_sum_of_dict_values(dict_to_sum: dict[str:float]) -> float:
    """
    Takes a dictionary of the key value format of string: float.
    Returns sum of all the values
    """
    total = sum(dict_to_sum.values())
    return total


def has_disallowed_string_list(
    disallowed_list: list[str], string_to_check: str
) -> bool:
    """
    Takes a list of substrings that are disallowed.
    Checks if the string has any of the substrings.
    Return True if the string does not have any of the substrings.
    Returns False if the string has any of the substrings.
    """
    has = False
    for item in disallowed_list:
        if item in string_to_check:
            has = True
            return has
    return has


def has_double_letters_in_string(string_to_check: str) -> bool:
    """
    Takes a string.
    checks if the string has any repeating characters,
    Return True if the string has repeating characters.
    Returns False if the string does not have repeating characters.
    """
    has = False
    for i in range(len(string_to_check) - 1):
        if string_to_check[i] == string_to_check[i + 1]:
            has = True
            return has
    return has


def generate_md5_hash(input_string):
    md5_object = hashlib.md5(input_string.encode())
    return md5_object.hexdigest()


def get_total_of_list_of_floats(list_of_floats: list[float]) -> float:
    """
    Takes a list of floats
    Returns the list of floats sum.
    """
    tot = sum(list_of_floats)
    return tot


def get_max_number_of_instance_of_split_char(
    input_lines: list[str], split_char: str
) -> int:
    """
    Take in input as a list of string values and the character to split on.
    Returns maximum number of instances in the list lines where the "split_char" is found.
    """
    max_split_char_instance = 0
    for line in input_lines:
        split_char_count = line.count(split_char)
        if split_char_count <= max_split_char_instance:
            continue
        max_split_char_instance = split_char_count
    return max_split_char_instance


def create_dict_of_n_lists(number_of_list: int) -> dict[list]:
    """
    Takes in the number of lists needed.
    Returns a dictionary having keys as the number of list needed, indexed from '0' and values as empty lists.
    """
    dict_of_lists = {}
    for n in range(number_of_list):
        dict_of_lists[n] = []
    return dict_of_lists


def split_input_lines_to_float_lists(
    input_lines: list[str], split_char: str
) -> dict[list[None | float]]:
    """
    Takes a list of input lines containing Numbers with charcter delimiter.(eg. 2x3x4 or 2+3+4+5 etc) and the split_char (in this e.g "x" or "+")
    Finds the number of list neede to hold all the numbers, one list specific to each number position, so in the case of  "2x3x4" we would need 3 lists to hold [2],[3] and [4] respectively.
    In the case of 2+3+4+5 we would need 4 lists to hold [2],[3],[4] and [5] respectively.
    Returns a dictionary of lists with the number of keys max of the number of lists needed and values in the list corresponding to the values in the input converted to float, if empty then retuns None.
    e.g:    Input: ['1x2x3','2x3x4x5','0x2','']
            Output:{0: [1.0, 2.0 , 0.0, None], 1: [2.0, 3.0, 2.0, None], 2: [3.0, 4.0, None, None], 3: [None, 5.0, None, None]}

    """

    max_split_char_instance = get_max_number_of_instance_of_split_char(
        input_lines, split_char
    )
    split_dict = create_dict_of_n_lists(max_split_char_instance + 1)

    for line in input_lines:
        items = line.split(split_char)
        max_index = len(items) - 1
        for key in split_dict.keys():
            if key <= max_index:
                if items[key].isdigit():
                    split_dict[key].append(float(items[key]))
                    continue
                else:
                    split_dict[key].append(None)
                    continue
            else:
                split_dict[key].append(None)
    return split_dict


def example_split_input_lines_to_float_lists():
    """
    Runs an example of the function split_input_lines_to_float_lists().
    """
    year = "2015"
    file = "input_example2.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    spilt_dict = split_input_lines_to_float_lists(input_lines, "x")
    print(spilt_dict)


def get_smallest_of_three(
    x: float | int, y: float | int, z: float | int
) -> float | int:
    """
    Takes in three integers or float and compares them.
    Returns the smallest value from them.
    """
    if x <= y and x <= z:
        return x
    if y <= x and y <= z:
        return y
    if z <= x and z <= y:
        return z


def get_two_smallest_of_three(
    x: float | int, y: float | int, z: float | int
) -> tuple[float | int, float | int]:
    """
    Takes in three integers or float and compares them.
    Returns the SMALLEST TWO! value from them.
    """
    smallest = get_smallest_of_three(x, y, z)
    next_smallest = float("inf")
    if smallest == x:
        next_smallest = get_smallest_of_three(next_smallest, y, z)
        return smallest, next_smallest
    if smallest == y:
        next_smallest = get_smallest_of_three(x, next_smallest, z)
        return smallest, next_smallest
    if smallest == z:
        next_smallest = get_smallest_of_three(x, y, next_smallest)
        return smallest, next_smallest


def get_input(path: str) -> list[any]:
    """
    Takes a path to a text file including the filename.
    returns the contents of the file as a list, with each item of the list the line in the file.
    """
    input_lines = []
    with open(path, "r") as file:
        input_lines = file.read().splitlines()
    return input_lines


def get_input_items(list: list[any]) -> list[any]:
    """
    Takes a list of items where may not be at granular level.
    e.g. list of lines/list of words etc,
    and gives back a list of all characters that make up the line/words
    """
    items = []
    for item in list:
        for i in item:
            items.append(i)
    return items


def example_get_input():
    """
    Runs an example of the function get_input().
    """
    year = "2015"
    file = "input_example.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    print(input_lines)
    return input_lines


def example_get_input_items(list):
    """
    Runs an example of the function get_input_items().
    """
    items = get_input_items(list)
    print(items)
    return items


if __name__ == "__main__":
    pass
