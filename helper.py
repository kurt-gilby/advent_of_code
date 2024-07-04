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
