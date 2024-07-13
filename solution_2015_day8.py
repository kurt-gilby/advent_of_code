from helper import get_input


def find_all(string: str, sub_string: str) -> object:
    start = 0
    while True:
        start = string.find(sub_string, start)

        if start == -1:
            break
        yield start
        start += len(sub_string)


def get_replace_list(string: str, sub_string: str, num_chars: int) -> list[str]:
    replace_list = []
    idx_generator = find_all(string, sub_string)
    for idx in idx_generator:
        replace_list.append(string[idx : idx + num_chars])
    return replace_list


def get_list_sum_diff(
    num_list: list[int | float], another_num_list: list[int | float]
) -> int | float:
    num_list_tot = sum(num_list)
    another_num_list_tot = sum(another_num_list)
    diff = num_list_tot - another_num_list_tot
    return diff


def solved_part_one():
    year = "2015"
    file = "input_day_8.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    string_code_len_list = []
    string_values_len_list = []
    for line in input_lines:
        string_code_len_list.append(len(line[1:-1]) + 2)
        x_list = get_replace_list(line, r"\x", 4)
        q_list = get_replace_list(line, r"\"", 2)
        bs_list = get_replace_list(line, r"\\", 2)
        final_set = set(x_list + q_list + bs_list)
        for element in final_set:
            line = line.replace(element, "X")
        string_values_len_list.append(len(line[1:-1]))
    diff = get_list_sum_diff(string_code_len_list, string_values_len_list)
    print(f"Difference post removing escape characters: {diff}")


def solved_part_two():
    year = "2015"
    file = "input_day_8.txt"
    path = f"./{year}/{file}"
    input_lines = get_input(path)
    string_code_len_list = []
    string_encode_len_list = []
    for line in input_lines:
        count = 0
        string_code_len_list.append(len(line[1:-1]) + 2)
        line = line.replace('"', "XX")
        line = line.replace(r"\x", "XXX")
        line = line.replace("\\", "XX")
        string_encode_len_list.append(len(line) + 2)
    diff = get_list_sum_diff(string_encode_len_list, string_code_len_list)
    print(f"Difference counting all escape characters: {diff}")


if __name__ == "__main__":
    solved_part_one()
    solved_part_two()
